from time import sleep
from LCD_ST7066U import lcd


def test_something():
    h = lcd.LCD(d4=23, d5=18, d6=15, d7=14, en=24, rs=25)
    h.writeMessage("hola que tal\nyo bien")
    sleep(2)


if __name__ == '__main__':
    lcd.logger.setLevel(lcd.logging.DEBUG)
    test_something()
