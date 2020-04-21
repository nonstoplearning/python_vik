x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary, do_not)

# prints the value 10 in place of %d
print (x)
# prints the value from variables binary and do_not
print (y)

# prints the raw data of variable x in place of %r
print ("I said: %r." % x)
# prints the value of variable y in pace of %s but the quotes around '%s' makes it look like %r string formatter
print ("I also said: '%s'." % y)

hillarious = True
joke_evaluation = "Isn't that joke so funny?! %r"

# prints the value of variable 'hillarious', but as its a boolean value you don't need quotes hence in the output you don't see them.
print (joke_evaluation % hillarious)

w = "This is the left side of..."
e = "a string with a right side."

# prints the concatenation of two variables.
print (w + e)
