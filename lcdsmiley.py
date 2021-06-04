from RPLCD.gpio import CharLCD;
from RPLCD import cleared,cursor;
import RPi.GPIO as GPIO;

lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 36],numbering_mode=GPIO.BOARD);


lcd.clear(); #just to clear previous
lcd.clear();

smiley = (
    0b00000,
    0b01010,
    0b01010,
    0b00000,
    0b10001,
    0b10001,
    0b01110,
    0b00000,
)

lcd.create_char(0,smiley);
lcd.write_string(unichr(0));

