'''The waitKey(0) function returns -1 when no input is made whatsoever. As soon the event occurs i.e. a Button is pressed it returns a 32-bit integer value of button.

The 0xFF in this scenario is representing binary 11111111 a 8 bit binary, since we only require 8 bits to represent a character we AND waitKey(0) to 0xFF. It gives 8 bit value of button. 

ord(char) returns the ASCII value of the character which would be again maximum 255.

Hence by comparing the integer to the ord(char) value, we can check for a key pressed event and break the loop.'''