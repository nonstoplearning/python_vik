from sys import argv

script, filename = argv

txt = open(filename)

print ("Here's your file %r:" % filename)
print (txt.read()) #reads the content from what is passed to variable txt
txt.close()

print ("Type the filename again:")
file_again = input("> ") #prompts user to type a file name

txt_again = open(file_again)

print (txt_again.read())
txt_again.close()
