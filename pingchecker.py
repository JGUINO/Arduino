import shlex
import subprocess
from time import sleep
import RPi.GPIO as GPIO
from gpiozero import LED
import time


def ping (a):
	cmd=shlex.split("ping -c1 %s" % a)
	try:
	   output = subprocess.check_output(cmd)
	except subprocess.CalledProcessError as e:
		return False
	else:
		return True

while True:
    if ping('192.168.1.124'):
        print ('Bonne connexion')
        sleep(0.5)
    else:
        LED(16).off()
        print('Perte de connexion')
        file=open('log.txt')
        file.write(time.strftime("%H:%M:%S"))
        file.close
        sleep(5)
