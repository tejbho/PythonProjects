#Travis the ridiculous security system

known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "George", "Harry"]
print(len(known_users))

while True:
    print("Hi! My name is Travis!")
    name = input("What is your name?: ").strip().capitalize()

    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the system?(Y/N): ").strip().lower()
        
        if remove == "y":
            known_users.remove(name)
        elif remove == "n":
            print("No problem, I didn't want you to leave anyway!")

    else:
        print("Hmm... I don't think I've met you yet {}".format(name))
        add_me = input("Would you like to be added to the system?(Y/N): ").strip().lower()

        if add_me == "y":
            known_users.append(name)
            
        elif add_me == "n":
            print("No worries, see you around")
