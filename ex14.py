from sys import argv

script = argv
prompt = '^'
username = input("Hi, What is your name?\n")

print("Hi %s, I'm the %s script." % (username,script))
print("I'd like to ask you few questions.")
print("Do you like me %s?" % (username))
likes = input(prompt)

print("Where do you live %s?" % (username))
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print ("""
Alright, so you said %r about liking me.
You live in %r, Not sure where that is.
And you have %r computer. Nice.
""" % (likes, lives, computer))
