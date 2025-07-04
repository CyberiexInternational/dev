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
#import digidevice 
sys.path.append("..")
from lib import LCD_1inch5
from PIL import Image,ImageDraw,ImageFont
from gpiozero import CPUTemperature
#from digidevice import location


# Raspberry Pi pin configuration:
RST = 27
DC = 25
BL = 18
bus = 0 
device = 0 
logging.basicConfig(level=logging.DEBUG)

#Working display area top left and bottom right co-ords on screen
watlx=10
watly=30
wabrx=220
wabry=250
cpu = CPUTemperature()

def getTime(): 
        currenttime = datetime.datetime.now()
        logging.info(currenttime)
        timenow=str(currenttime.hour) + ":" + str(currenttime.minute) + ":" + str(currenttime.second)
        logging.info(timenow)
        return timenow


try:
    # display with hardware SPI:
    ''' Warning!!!Don't  creation of multiple displayer objects!!! '''
    #disp = LCD_1inch5.LCD_1inch5(spi=SPI.SpiDev(bus, device),spi_freq=10000000,rst=RST,dc=DC,bl=BL)
    disp = LCD_1inch5.LCD_1inch5()
    # Initialize library.
    disp.Init()
    # Clear display.
    disp.clear()

   
    logging.info("draw text")
    
    # Create blank image for drawing.
    Font1 = ImageFont.truetype("../Font/Font00.ttf",10)
    Font2 = ImageFont.truetype("../Font/Font00.ttf",10)
    Font3 = ImageFont.truetype("../Font/Font00.ttf",50)
    
    i=0
    logging.info("Start loop")
        
    #Loop forever, once per quarter second, updating display each time
    while True:
            
        ImagePath = "../pic/logo.png"
        image = Image.open(ImagePath)	
        # image = image.rotate(0)
        disp.ShowImage(image)
        time.sleep(3)    
        image1 = Image.new("RGB", (disp.width,disp.height ), "BLACK")
        draw = ImageDraw.Draw(image1)
        draw.rectangle([(watlx-10, watly-10), (wabrx+10, wabry+10)], fill = "#007700", outline="#005500")
        draw.rectangle([(watlx, watly), (wabrx, wabry)], fill = "BLACK", outline="#005500")
        
        logging.info("loop : " + str(i))
        currenttime = datetime.datetime.now()
        logging.info(currenttime)
        timenow=currenttime.strftime("%H") + ":" + currenttime.strftime("%M") + ":" + currenttime.strftime("%S") + "    " + currenttime.strftime("%d") + " " + currenttime.strftime("%b") + " " + currenttime.strftime("%Y")
        tempinfo=str(cpu.temperature)
        
        draw.text((watlx+5, watly + 15), timenow , fill = "#99ff99",font=Font1)
        draw.text((watlx+5, watly + 25), "CPU Temp : " + tempinfo + "'C", fill = "#99ff99",font=Font2)
                
        image1 = image1.rotate(90)
        disp.ShowImage(image1)

       
        time.sleep(2)
        
        
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
