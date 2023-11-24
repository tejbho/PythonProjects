students = {
    "male": ["Alex", "Bob", "Chris", "Daniel"],
    "female":["Alice", "Bethany", "Claire", "Drusila", "Elly"]
    }

for key in students.keys():
    for name in students[key]:
        if"c" in name.lower():
            print(name)
