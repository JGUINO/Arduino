import shlex
import subprocess
from time import sleep
import RPi.GPIO as GPIO
from gpiozero import LED


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
        sleep(5)
