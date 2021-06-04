import RPi.GPIO as GPIO;
import time;
import sys;
import Tkinter as tk;

def initial():
 GPIO.setmode(GPIO.BCM);
 GPIO.setup(17, GPIO.OUT);
 GPIO.setup(22, GPIO.OUT);
 GPIO.setup(23, GPIO.OUT);
 GPIO.setup(24, GPIO.OUT);

def go(tf,IN1,IN2,IN3,IN4):
 #initial();
 GPIO.output(17, IN1);
 GPIO.output(22, IN2);
 GPIO.output(23, IN3);
 GPIO.output(24, IN4);
 time.sleep(tf);
 GPIO.cleanup();

def key_input(event):
 initial();
 print "Key:", event.char;
 key_press = event.char;
 #sleep_time = 0.030;

 if key_press.lower() == 'w':
   go(1,1,0,0,1);
 elif key_press.lower() == 'a':
   go(1,1,0,0,0);
 elif key_press.lower() == 's':
   go(1,0,1,1,0);
 elif key_press.lower() == 'd':
   go(1,0,0,0,1);

#IN1,IN2,IN3,IN4 -> GPIO17,GPIO22,GPIO23,GPIO24
#for forward IN2,IN4 active


a = tk.Tk();
a.bind('<KeyPress>',key_input);
a.mainloop();

