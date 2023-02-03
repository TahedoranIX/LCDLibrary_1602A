import RPi.GPIO as GPIO
from time import sleep
import logging

LOW_TIME = 0.00004
HIGH_TIME = 0.00153
GPIO.setwarnings(False)
logger = logging.getLogger(__name__)


class LCD:

    def __init__(self, d4, d5, d6, d7, en, rs):
        logger.info("=====LCDLibrary starting...=====")

        GPIO.setmode(GPIO.BCM)
        self.__data = [d7, d6, d5, d4]
        self.__en = en
        self.__rs = rs
        for pin in (rs, en, d4, d5, d6, d7):
            GPIO.setup(pin, GPIO.OUT)
        logger.debug('All pins set to output')

        logger.info('Beginning lcd init.')
        self.__sendCommand(rs=0, data=[0, 0, 1, 1, 0, 0, 1, 1], time=LOW_TIME)
        self.__sendCommand(rs=0, data=[0, 0, 1, 1, 0, 0, 1, 0], time=LOW_TIME)

        logger.debug('Function Set 1 Completed.')

        self.__functionSet()
        logger.debug('Function Set 2 Completed.')

        self.__functionSet()
        logger.debug('Function Set 3 Completed.')

        self.display()
        logger.debug('Display on Completed.')

        self.clearDisplay()
        logger.debug('Display cleared Completed.')

        self.__entryMode()
        logger.debug('Display EntryMode Completed.')

        logger.info('=====Library initialized=====')

    def __del__(self):
        self.clearDisplay()
        # GPIO.cleanup()

    def __enviar(self):
        ''' Trigger PIN ENABLE'''
        GPIO.output(self.__en, 0)
        GPIO.output(self.__en, 1)
        GPIO.output(self.__en, 0)

    def __sendCommand(self, rs, data, time):
        """
        SendCommand to LCD

        :param rs: Pin RS (instruction/data register)
        :param data: 8bit list data.
        :param time: HIGH_TIME/LOW_TIME
        """
        logger.info('Sending data: ' + str(data))
        GPIO.output(self.__rs, rs)
        GPIO.output(self.__data, data[:4])
        self.__enviar()
        logger.debug('first data half sent.')
        GPIO.output(self.__data, data[4:])
        self.__enviar()
        logger.debug('second data half sent.')
        sleep(time)

    def __functionSet(self):
        """ Set bit mode LCD, only used in init"""
        self.__sendCommand(rs=0, data=[0, 0, 1, 0, 1, 0, 0, 0], time=LOW_TIME)

    def __setCGRAM(self, address):
        """
        Set CGRAM address to AC (custom chars)

        :param address: 6bit Address(5-0)
        """
        self.__sendCommand(rs=0, data=[0, 1, [0], address[1], address[2], address[3], address[4], address[5]],
                           time=LOW_TIME)

    def __setDDRAM(self, address):
        """
        Set DDRAM addresss to AC ('\ n' for example)

        :param address: 7bit Address(6-0)
        """
        self.__sendCommand(rs=0,
                           data=[1, address[0], address[1], address[2], address[3], address[4], address[5], address[6]],
                           time=LOW_TIME)

    def writeRAM(self, data):
        """
        Write data in RAM, show chars.

        :param data: 8bit data package.
        """
        self.__sendCommand(rs=1, data=data, time=LOW_TIME)

    def __entryMode(self, cursor=1, display=0):
        """
        Set moving direction of cursor and display.

        :param cursor: set orientation of cursor
        :param display: shift entire display
        """
        self.__sendCommand(rs=0, data=[0, 0, 0, 0, 0, 1, cursor, display], time=LOW_TIME)

    def clearDisplay(self):
        """ Clear all display data"""
        self.__sendCommand(rs=0, data=[0, 0, 0, 0, 0, 0, 0, 1], time=HIGH_TIME)

    def home(self):
        """ Return cursor to home"""
        self.__sendCommand(rs=0, data=[0, 0, 0, 0, 0, 0, 1, 0], time=HIGH_TIME)

    def display(self, display=1, cursor=0, blink=0):
        """
        View options

        :param display: Show messages in display
        :param cursor: Show cursor
        :param blink: Show blinking cursor
        """
        self.__sendCommand(rs=0, data=[0, 0, 0, 0, 1, display, cursor, blink], time=LOW_TIME)

    def moveCursor(self, cursor=0, direction=1, times=1):
        """
        View options

        :param cursor: Shift cursor(0) display(1)
        :param direction: Direction right(1) left(0)
        :param times: Times to move
        """
        for i in range(times):
            self.__sendCommand(rs=0, data=[0, 0, 0, 1, cursor, direction, 0, 0], time=LOW_TIME)

    def textLeftRight(self):
        """ Writes to the right (Normal)"""

        self.__sendCommand(rs=0, data=[0, 0, 0, 0, 0, 1, 1, 0], time=LOW_TIME)

    def textRightLeft(self):
        """ Writes to the left ¿?"""
        self.__sendCommand(rs=0, data=[0, 0, 0, 0, 0, 1, 0, 0], time=LOW_TIME)

    def writeMessage(self, message):
        """Write message in display """
        for char in message:
            if char == '\n':
                self.__setDDRAM([1, 0, 0, 0, 0, 0, 0])
            else:
                dataMessage = []
                letra = bin(ord(char))[2:].zfill(8)
                for binario in letra:
                    dataMessage.append(int(binario))
                logger.debug('Binary conversion of '+char+' -> '+str(dataMessage))
                self.writeRAM(dataMessage)
