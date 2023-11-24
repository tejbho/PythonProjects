from random import choice
class HotelBooking:
    def __init__(self, npeople, date, hotel):
        self.npeople = npeople
        self.date = date
        self.hotel = hotel

    def trybooking(self):
        booked ={}
        dates = booked.keys()
        x = choice(self.hotel.rooms)
        while self.npeople < x.capacity == False:
            x = choice(self.hotel.rooms)
        while self. date in dates and booked.get(self.date) > 0:
            x = choice(self.hotel.rooms)
        print("Room booked")
        booked.update({self.date:self.npeople})
        x.people = self.npeople
        print(booked)
        
class Hotel:
    def __init__(self, name, address, rooms):
        self.name = name
        self.address = address
        self.rooms = rooms


class Room:
    def __init__(self, rm_number, capacity, people):
        self.rm_number = rm_number
        self.capacity = capacity
        self.people = people
        
    def roomnumber(self):
        print(self.rm_nmbr)

    def capacity(self):
        print(self.capacity)

    def num_people(self):
        print(self.people)


class Address:
    def __init__(self, number, street, city, state, zipcode):
        self.number = number
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode
        

    def address(self):
        print(str(self.number) + " " +  self.street + ", " + self.city + ", " + self.state + " " + str(self.zipcode))

x = Address(3558, "Dunbar Ct", "Fremont", "CA", 94536)
r1 = Room(432, 3, 0)
r2 = Room(173, 4, 0)
h = Hotel("HOTEL",x, [r1,r2])
b= HotelBooking(4, "July 23, 2022", h)
b.trybooking()
r1.num_people()
r2.num_people()
