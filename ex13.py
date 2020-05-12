from sys import argv

script, first, second, third = argv

fourth = input("Enter your fourth variable: ")
fifth = input("Enter your fifth variable: ")

print ("Together, your first variable is %r, your second variable is %r, your third variable is %r, "
       "your fourth variable is %r, your fifth variable is %r" % (first, second, third, fourth, fifth))

"""
github vikram.talware$ python ex13.py stuff things
Traceback (most recent call last):
  File "ex13.py", line 3, in <module>
    script, first, second, third = argv
ValueError: not enough values to unpack (expected 4, got 3)
"""

"""
vikram.talware$ python ex13.py stuff things that vik
Traceback (most recent call last):
  File "ex13.py", line 3, in <module>
    script, first, second, third = argv
ValueError: too many values to unpack (expected 4)
"""

script, first, second, third = argv, input("Enter your first variable: "), input("Enter your second variable: "), input("Enter your third variable: ")

print ("The script is called:", script)
print ("Your first variable is:", first)
print ("Your second variable is:", second)
print ("Your third variable is:", third)
