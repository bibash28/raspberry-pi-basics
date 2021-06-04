from RPLCD.gpio import CharLCD;
import time;
import RPi.GPIO as GPIO;

lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 36],numbering_mode=GPIO.BOARD);


lcd.clear(); #just to clear previous
#blinking
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

lcd.create_char(0, smiley);
#lcd.write_string(unichr(0))

while True:
 lcd.write_string(u' Happy New Year    '     +unichr(0)+'  2075  '+unichr(0));
 time.sleep(0.5);
 lcd.clear();
 time.sleep(0.5);
