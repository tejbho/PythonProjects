# Print the odd numbers from 1 to 100

number = 1

while number <= 100:
    if number % 2 != 0:
     print(number)
    number = number + 1

# Create a list of names

L = []

while len(L) < 5:
    new_name = input("Enter a name: ").strip().title()
    L.append(new_name)

print("List is full")
print(L)
