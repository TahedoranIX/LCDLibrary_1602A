# LCD Library
LCD chipset ST7066U 1602a library for raspberry pi using 4 data pins.

# How to install:
Place at the root of the folder and execute the following command:
`pip install .`

# Basic use of the Library

`Declaration: LCD(d4, d5, d6, d7, en, rs)`

- `writeMessage(string message) `: Way to go function.
- `writeRAM(data=8bit array)`: Write directly to the LCD, read Datasheet to know the char-ascii encode.
- `home()`: Return cursor to home.
- `display(display="activa/desactiva pantalla", cursor="activa/desactiva vision del cursor", blink="activa/desactiva cursor blinking") 
  `: Configure cursor and display components.
- `moveCursor(direction="dirección a la que mover el cursor", times="veces que movemos el cursor") `: Move cursor between screen positions.
- `clearDisplay() `: Clean every information of the screen *important*.
- `textLeftRight() `: Writing left to right (right one ;-)).
- `textRightLeft() `: Writing right to left.