# Cinema Booking System

films = {
    "Finding Dory": [3,5],
    "Avengers": [10,5],
    "Tarzan": [5, 5],
    "Ghost Busters": [7,5]
         }

while True:
    
    choice = input("Which movie would you like to watch?: ").strip().title()

    if choice in films:
        age = int(input("How old are you?").strip())

        if age >= films[choice][0]:
            num_seats = films[choice][1]
            if num_seats > 0:
                     print("Enjoy the film!")
                     films[choice][1] = films[choice][1]-1
            else:
                print("Sorry, the tickets are sold out")
        else:
            print("Sorry, you're too young to watch this film")

    else:
        print("Sorry, we do not have that film yet")
