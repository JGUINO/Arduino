import shlex
import subprocess
import time
import RPI.GPIO as GPIO


def ping (a):
	cmd=shlex.split("ping -c1 %s" % a)
	try:
	   output = subprocess.check_output(cmd)
	except subprocess.CalledProcessError,e:
		return False
	else:
		return True

while True:
    if ping('192.168.1.124'):
        sleep(0.5)
    else:
        LED(16).off()
        sleep(5)