#!/usr/bin/python
# -*- coding: UTF-8 -*-
#import chardet
import os
import sys 
import time
import logging
import spidev as SPI
sys.path.append("..")
from lib import LCD_0inch85
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
    #disp = LCD_0inch85.LCD_0inch85(spi=SPI.SpiDev(bus, device),spi_freq=10000000,rst=RST,dc=DC,bl=BL)
    disp = LCD_0inch85.LCD_0inch85()
    # Initialize library.
    disp.Init()
    # Clear display.
    disp.clear()

    # Create blank image for drawing.
    image1 = Image.new("RGB", (disp.width,disp.height ), "WHITE")
    draw = ImageDraw.Draw(image1)

    logging.info("draw text")
    Font1 = ImageFont.truetype("../Font/Font01.ttf",20)
    Font2 = ImageFont.truetype("../Font/Font01.ttf",25)
    Font3 = ImageFont.truetype("../Font/Font02.ttf",30)

    draw.rectangle([(0,0),(128,25)],fill = "BLUE")
    draw.text((13, 0), 'Hello world', fill = "RED",font=Font1)
    draw.rectangle([(0,25),(128,55)],fill = "RED")
    draw.text((3, 25), 'WaveShare', fill = "WHITE",font=Font2)
    draw.text((0, 55), '12345678', fill = "GREEN",font=Font3)
    text= u"微雪电子"
    draw.text((0, 85),text, fill = "BLUE",font=Font3)
    image1=image1.rotate(0)
    disp.ShowImage(image1)
    time.sleep(3)
    image = Image.open('../pic/LCD_0inch85.jpg')	
    image = image.rotate(0)
    disp.ShowImage(image)
    time.sleep(3)
    disp.module_exit()
    logging.info("quit:")
except IOError as e:
    logging.info(e)    
except KeyboardInterrupt:
    disp.module_exit()
    logging.info("quit:")
    exit()