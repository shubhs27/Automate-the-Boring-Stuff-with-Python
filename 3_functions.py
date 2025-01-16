import random 
print(random.randint(1,10))
from random import *
print(randint(1,10))    # no need to specify randint is in which module    
print()


import sys
print("yo, bitches")
# sys.exit()
# print("bye, bitches")
print()


import pyperclip 
pyperclip.copy("Hello...")

print(pyperclip.paste())
print()


# print returns a special type of value of data type None 
# every function has a return value (print has None, by default it is None)


# print adds a newline character to the end of the string
print("Hello", end='')
print("World")

print("messi", "is", "the", "goat")
print("messi", "is", "the", "goat", sep='')
print()