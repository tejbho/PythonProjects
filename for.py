# count the vowels and consonants in a word

vowels = 0
consonants = 0

for letter in "Experimentl":
    if letter.lower() in "aeiou":
        vowels = vowels + 1

    elif letter == " ":
        pass

    else:
        consonants = consonants + 1

print("There are {} vowels".format(vowels))
print("There are {} consonants".format(consonants))


students = {
    "male": ["Alex", "Bob", "Chris", "Daniel"],
    "female":["Alice", "Bethany", "Claire", "Drusila", "Elly"]
    }

for key in students.keys():
    for name in students[key]:
        if"b" in name.lower():
            print(name)
