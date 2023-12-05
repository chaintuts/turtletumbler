# This file contains code for iterating over password hashes for a PIN
#
# Author: Josh McIntyre
#
import pwhash

# A simple construct for attempt information
class Attempt:

    # Initialize a simple Attempt
    def __init__(self, pin_tried, pin_hash, found):
        
        self.pin_tried = pin_tried
        self.pin_hash = pin_hash
        self.shortened_pin_hash = Attempt.get_shortened_hash(self.pin_hash)
        self.found = found

    # Show a shortened representation of the password hash
    @staticmethod
    def get_shortened_hash(password_hash):

        return password_hash[:10] + "..."

# Define a simple class for iterating over PINs
class BruteForcePIN:

    # Class constants
    MIN_PIN = 0
    MAX_PIN = 10000

    FORMAT_STRING = "{:04}"

    # Initialize the cracker
    def __init__(self, password_hash):

        self.password_hash = password_hash

    # Run the cracking attempts
    # This function is a generator that yields each attempt,
    # and exits when the correct hash is found or if MAX_PIN is reached
    def run(self):

        found = False
        for pin in range(self.MIN_PIN, self.MAX_PIN):
            
            pin_attempt = self._pad_pin_string(pin)
            password_hash = pwhash.PWHash(pin_attempt).password_hash

            if password_hash == self.password_hash:
                found = True

            yield Attempt(pin_attempt, password_hash, found)

            if found:
                break

    # Define the 
    # Format string construction
    def _pad_pin_string(self, pin):

        return self.FORMAT_STRING.format(pin)
