'''Order of Operations PEMDAS - Parentheses (simplify inside 'em), Exponents, Multiplication, Modulus and Division (from left to right),
Addition and Subtraction (from left to right)'''

print ("I will now count my chickens:")
# divides and adds
print ("Hens", float(25 + 30 / 6))
# multiplies, mods and then subtracts
print ("Roosters", float(100 - 25 * 3 % 4))

print ("Now I will count the eggs:")
#mods,divides,adds and then subtracts
print (float(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6))

#adds, subtracts and then weighs
print ("Is it true that 3 + 2 < 5 - 7?")
print (3 + 2 < 5 - 7)

print ("What is 3 + 2?", 3 + 2)
print ("What is 5 - 7?", 5 - 7)

print ("Oh, that's why it's False.")

print ("How about some more.")

print ("Is it greater?", 5 > -2)
print ("Is it greater or equal?", 5 >= -2)
print ("Is it less or equal?", 5 <= -2)
