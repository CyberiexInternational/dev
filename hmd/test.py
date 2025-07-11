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
    image1 = Image.new("RGB", (disp.width,disp.height ), "WHITE")
    draw = ImageDraw.Draw(image1)

    logging.info("draw point")

    draw.rectangle((15,10,6,11), fill = "BLACK")
    draw.rectangle((15,25,7,27), fill = "BLACK")
    draw.rectangle((15,40,8,43), fill = "BLACK")
    draw.rectangle((15,55,9,59), fill = "BLACK")

    logging.info("draw rectangle")
    draw.rectangle([(20,10),(70,60)],fill = "WHITE",outline="BLUE")
    draw.rectangle([(85,10),(130,60)],fill = "BLUE")

    logging.info("draw line")
    draw.line([(20, 10),(70, 60)], fill = "RED",width = 1)
    draw.line([(70, 10),(20, 60)], fill = "RED",width = 1)
    draw.line([(110,65),(110,115)], fill = "RED",width = 1)
    draw.line([(85,90),(135,90)], fill = "RED",width = 1)


    logging.info("draw circle")
    draw.arc((85,65,135,115),0, 360, fill =(0,255,0))
    draw.ellipse((20,65,70,115), fill = (0,255,0))

    logging.info("draw text")
    Font1 = ImageFont.truetype("../Font/Font01.ttf",25)
    Font2 = ImageFont.truetype("../Font/Font01.ttf",35)
    Font3 = ImageFont.truetype("../Font/Font02.ttf",32)

    draw.rectangle([(0,120),(155,153)],fill = "BLUE")
    draw.text((15, 120), 'Hello world', fill = "RED",font=Font1)
    draw.rectangle([(0,155),(200,195)],fill = "RED")
    draw.text((15, 155), 'WaveShare', fill = "WHITE",font=Font2)
    draw.text((15, 190), '1234567890', fill = "GREEN",font=Font3)
    text= u"微雪电子"
    draw.text((15, 230),text, fill = "BLUE",font=Font3)
    image1=image1.rotate(0)
    disp.ShowImage(image1)
    time.sleep(3)
    disp.clear()
    image = Image.open('../pic/LCD_1inch5.jpg')	
    image = image.rotate(0)
    disp.ShowImage(image)
    time.sleep(3)
    image1 = Image.new("RGB", (disp.width,disp.height ), "BLACK")
    draw = ImageDraw.Draw(image1)

    
    disp.module_exit()
    logging.info("quit:")
except IOError as e:
    logging.info(e)    
except KeyboardInterrupt:
    disp.module_exit()
    logging.info("quit:")
    exit()
