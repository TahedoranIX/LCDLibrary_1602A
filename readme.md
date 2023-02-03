# LCD Library
LCD chipset ST7066U 1602a library for raspberry pi using 4 data pins.

# How to install:
Place at the root of the folder and execute the following command: 
```Shell
$ pip install .
```


# Basic use of the Library
This library uses python's builtin logging system. To enable it use the following command:
  ```
  import lcd
 lcd.logger.setLevel(lcd.logging.DEBUG)
 ```
This will set the logger in Debug level.


```
Declaration: LCD(d4, d5, d6, d7, en, rs)
```

- `writeMessage(string message) `: Way to go function.
- `writeRAM(boolean data[8])`: Write directly to the LCD, read Datasheet to know the char-ascii encode.
- `home()`: Return cursor to home.
- `display(boolean display, boolean cursor, boolean blink) 
  `: Configure cursor and display components, enabling or disabling the display, enabling or disabling the cursor visualizer and enabling or disabling the blincking cursor.
- `moveCursor(boolean direction, int times) `: Move cursor in a direction a certain amount of times.
- `clearDisplay() `: Clean every information of the screen *important*.
- `textLeftRight() `: Writing left to right (right one ;-)).
- `textRightLeft() `: Writing right to left.