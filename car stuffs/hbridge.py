import RPi.GPIO as GPIO;
import time;


def initial():
 GPIO.setmode(GPIO.BCM);
 GPIO.setup(17, GPIO.OUT);
 GPIO.setup(22, GPIO.OUT);
 GPIO.setup(23, GPIO.OUT);
 GPIO.setup(24, GPIO.OUT);

def go(IN1,IN2,IN3,IN4):
 initial();
 GPIO.output(17, IN1);
 GPIO.output(22, IN2);
 GPIO.output(23, IN3);
 GPIO.output(24, IN4);
 time.sleep(2);
 GPIO.cleanup();


#IN1,IN2,IN3,IN4 -> GPIO17,GPIO22,GPIO23,GPIO24
#for forward IN2,IN4 active
print("forward");
go(1,0,0,1);
print("backward");
go(0,1,1,0);
print("left")
go(1,0,0,0);
print("right")
go(0,0,0,1);


