import RPi.GPIO as GPIO;
import time;

GPIO.setmode(GPIO.BCM);    #setmode 
GPIO.setup(18, GPIO.OUT);  #pin 18 used as output
GPIO.output(18, True);     #turn ON led
time.sleep(3);             #sleep for 3 sec
GPIO.output(18,False);     #turn OFF led
