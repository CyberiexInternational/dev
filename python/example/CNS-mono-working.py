#!/usr/bin/python
# -*- coding: UTF-8 -*-
#import chardet
import os
import sys 
import time
import logging
import spidev as SPI
import datetime
import re, subprocess
import random

sys.path.append("..")
from lib import LCD_1inch5
from PIL import Image,ImageDraw,ImageFont
from gpiozero import CPUTemperature

# Raspberry Pi pin configuration:
RST = 27
DC = 25
BL = 18
bus = 0 
device = 0 
logging.basicConfig(level=logging.DEBUG)

#Working display area top left and bottom right co-ords on screen
tlx=10
tly=30
brx=220
bry=250
cpu = CPUTemperature()

try:
    # display with hardware SPI:
    disp = LCD_1inch5.LCD_1inch5()
    # Initialize library.
    disp.Init()
    # Clear display.
    disp.clear()

     #Set up fonts
    Font1 = ImageFont.truetype("../Font/Font00.ttf",10)
    Font2 = ImageFont.truetype("../Font/Font00.ttf",10)
    Font3 = ImageFont.truetype("../Font/Font00.ttf",50)

    #Loop forever, once per quarter second, updating display each time
    while True:
        image1 = Image.new("RGB", (disp.width,disp.height ), "BLACK")
        draw = ImageDraw.Draw(image1)
        draw.rectangle([(tlx-10, tly-10), (brx+10, bry+10)], fill = "#007700", outline="#005500")
        draw.rectangle([(tlx, tly), (brx, bry)], fill = "BLACK", outline="#005500")
        currenttime = datetime.datetime.now()
        logging.info(currenttime)
        timenow=currenttime.strftime("%H") + ":" + currenttime.strftime("%M") + ":" + currenttime.strftime("%S") + "    " + currenttime.strftime("%d") + " " + currenttime.strftime("%b") + " " + currenttime.strftime("%Y")
        tempinfo=str(cpu.temperature)       
        draw.text((tlx+5, tly + 15), timenow , fill = "#99ff99",font=Font1)
        draw.text((tlx+5, tly + 25), "CPU Temp : " + tempinfo + "'C", fill = "#99ff99",font=Font2)                
        image1 = image1.rotate(90)
        disp.ShowImage(image1)
        time.sleep(0.25)  
    time.sleep(2)
    disp.module_exit()
    logging.info("quit:")
except IOError as e:
    logging.info(e)    
except KeyboardInterrupt:
    disp.module_exit()
    logging.info("quit:")
    exit()



    
