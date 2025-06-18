#!/usr/bin/python
# -*- coding: UTF-8 -*-
#import chardet
import os
import sys 
import time
import logging
import spidev as SPI
sys.path.append("..")
from lib import LCD_1inch5
from PIL import Image,ImageDraw,ImageFont

# Raspberry Pi pin configuration:
RST = 27
DC = 25
BL = 18
bus = 0 
device = 0 
logging.basicConfig(level=logging.DEBUG)
try:
    # display with hardware SPI:
    ''' Warning!!!Don't  creation of multiple displayer objects!!! '''
    #disp = LCD_1inch5.LCD_1inch5(spi=SPI.SpiDev(bus, device),spi_freq=10000000,rst=RST,dc=DC,bl=BL)
    disp = LCD_1inch5.LCD_1inch5()
    # Initialize library.
    disp.Init()
    # Clear display.
    disp.clear()

    # Create blank image for drawing.
    image1 = Image.new("RGB", (disp.width,disp.height ), "BLACK")
    draw = ImageDraw.Draw(image1)

    #
    draw.text((0, 20), 'WaveShare', fill = "GREEN",font=Font2)
    image1=image1.rotate(0)
    draw = ImageDraw.Draw(image1)
    disp.ShowImage(image1)

    disp.module_exit()
    logging.info("quit:")
except IOError as e:
    logging.info(e)    
except KeyboardInterrupt:
    disp.module_exit()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    logging.info("quit:")
    exit()
 
