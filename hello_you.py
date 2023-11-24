# How to use user input and string formatting
name = input("What is your name?: ")
age = input("How old are you?: ")
city = input("Where do you live?: ")
love = input("What do you love to do?: ")

string = "Your name is {} and you are {} years old. You live in {} and you love to {}."
output = string.format(name, age, city, love)
print(output)
