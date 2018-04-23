#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import sys
import csv
sys.path.insert(0, "/home/pi/Adafruit_Python_GPIO")
sys.path.insert(0, "/home/pi/Adafruit_Python_PureIO")
sys.path.insert(0, "/home/pi/Adafruit_Python_SSD1306")
import Adafruit_SSD1306
import Adafruit_GPIO.SPI as SPI


from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess

from hx711 import HX711
from flask import Flask, request, redirect, render_template

# Raspberry Pi pin configuration:
RST = None     # on the PiOLED this pin isnt used
# Note the following are only used with SPI:
#DC = 23
#SPI_PORT = 0
#SPI_DEVICE = 0

# 128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Load default font.
font = ImageFont.load_default()

# Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
# font = ImageFont.truetype('Minecraftia.ttf', 8)

def cleanAndExit():
	print ("Cleaning...")
	draw.rectangle((0,0,width,height), outline=0, fill=0)
	GPIO.cleanup()
	print ("Bye")
	sys.exit()

hx = HX711(21,20)
#hx.set_reading_format("MSB","LSB")
hx.set_reading_format("LSB","MSB")
#calibrate to generate the reference unit value
hx.set_reference_unit(250)
#mis en commentaire car peu utile
#hx.reset()
hx.tare()
#pour l instant sauvegarde prévue sur le serveur
#dataFile = open('loadData.csv', 'w')
while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    # Shell scripts for system monitoring from here : https://unix.stackexchange.com/questions/119126/command-to-display-memory-usage-disk-usage-and-cpu-load
    cmd = "hostname -I | cut -d\' \' -f1"
    IP = subprocess.check_output(cmd, shell = True )
##    cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
##    CPU = subprocess.check_output(cmd, shell = True )
##    cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
##    MemUsage = subprocess.check_output(cmd, shell = True )
##    cmd = "df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB %s\", $3,$2,$5}'"
##    Disk = subprocess.check_output(cmd, shell = True )
   
    try:
		val = hx.get_weight(5)
		print (val, " g")
		draw.text((x, top),       "IP: " + str(IP),  font=font, fill=255)
                draw.text((x, top+8),     "Pression: "+str(val/1000)+" bars", font=font, fill=255)
                draw.text((x, top+16),    "Masse: "+str(val)+" g",  font=font, fill=255)
  
                disp.image(image)
                disp.display()
	
		hx.power_down()
		time.sleep(1)
		hx.power_up()
    except (KeyboardInterrupt, SystemExit):
		cleanAndExit()
