from RPLCD.gpio import CharLCD;
import time;
import RPi.GPIO as GPIO;

lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 36],numbering_mode=GPIO.BOARD);


lcd.clear(); #just to clear previous

while True:
 lcd.write_string("Time: %s" %time.strftime("%H:%M:%S"));
 lcd.cursor_pos=(1,0);
 lcd.write_string("Date: %s" %time.strftime("%m/%d/%Y")); 

