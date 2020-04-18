name = 'Vikram Talware'
age = 33 # not a lie
height = 71 # inches
weight = 176 # lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'
inches_to_cms = height / 0.39370
pounds_to_kgs = weight / 2.2046

print ("Let's talk about %s." % name)
print ("Let's talk about %r." % name) # prints everything no matter what
print ("I'm %d inches tall." % height)
print ("I'm %d centimeters tall." % inches_to_cms)
print ("I'm %d pounds heavy." % weight)
print ("I'm %d kgs heavy." % pounds_to_kgs)
print ("Actually that's not too heavy.")
print ("I've got %s eyes and %s hair." % (eyes, hair))
print ("My teeth are usually %s." % teeth)

print ("If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight))

# Python Format Characters
# Link - https://docs.python.org/2.4/lib/typesseq-strings.html
