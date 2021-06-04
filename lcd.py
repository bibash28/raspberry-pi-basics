import time
from RPLCD.gpio import CharLCD
import RPi.GPIO as GPIO
lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 36],numbering_mode=GPIO.BOARD)

lcd.clear()   #to clear the screen
lcd.clear()
lcd.clear()
#lcd.cursor_pos =(1,3)     just to position the text
lcd.write_string(u' Happy New Year      2075')


