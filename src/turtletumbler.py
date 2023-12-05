# This file contains code for displaying password cracking operations
#
# Author: Josh McIntyre
#
import time

import board
import busio
import adafruit_character_lcd.character_lcd_i2c as character_lcd

import pwhash
import slowcrack

# Module constants
ATTEMPT_FORMAT = "Att: {}\nHsh: {}\nTgt: {}\nFnd: {}"
TRUE_FMT = "Yes!"
FALSE_FMT = "No"
LOG_FORMAT = "Attempt: {} Hash: {} Target: {} Found: {}"

SLEEP = 1

PIN = "0010"

# The main entry point for the program
def main():

    # Initialize the display
    i2c = busio.I2C(board.SCL, board.SDA)
    cols = 16
    rows = 4
    lcd = character_lcd.Character_LCD_I2C(i2c, cols, rows)

    # Initialize a password cracking demo
    pw = pwhash.PWHash(PIN)
    sc = slowcrack.BruteForcePIN(pw.password_hash)
    
    # run() is a generator that yields Attempt objects
    for attempt in sc.run():

        # Format the attempt data
        msg = ATTEMPT_FORMAT.format(attempt.pin_tried,
                                    attempt.shortened_pin_hash,
                                    slowcrack.Attempt.get_shortened_hash(pw.password_hash),
                                    TRUE_FMT if attempt.found else FALSE_FMT)

        msg_log = LOG_FORMAT.format(attempt.pin_tried,
                                    attempt.shortened_pin_hash,
                                    slowcrack.Attempt.get_shortened_hash(pw.password_hash),
                                    TRUE_FMT if attempt.found else FALSE_FMT)

        # Display the attempt data
        # Don't need to clear the LCD - just updating the message will only
        # update the relevant rows/columns and looks nicer in this context
        # Also log a message to the console
        lcd.message = msg
        print(msg_log)

        # Sleep a reasonable amount of time so the user can see the attempts
        time.sleep(SLEEP)

if __name__ == "__main__":

    main()
