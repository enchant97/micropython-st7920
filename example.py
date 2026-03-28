"""
A simple test example. Assumes running on a Raspberry Pi Pico and the following pins are connected:

GND -> GND
VCC -> VBUS
RS  -> GP17 (SPI0 CSn)
R/W -> GP19 (SPI0 TX)
E   -> GP18 (SPI0 SCK)
PSB -> GND
BLA -> 3V3(OUT)
BLK -> GND
"""

from machine import Pin, SPI

from st7920 import ST7920_SPI


screen = ST7920_SPI(
    SPI(0, baudrate=1_000_000),
    Pin(17),
    partial_updates=True,
)
screen.init()
screen.clear()
screen.text("Hello World!", 0, 0)
screen.show()
