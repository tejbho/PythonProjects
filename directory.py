directory = {}
people = directory.keys()
numbers = directory.values()
p= []
for x in people:
    p.append(x)

class PhoneBook:

    def addnumber(self, name, number):
        directory.update({name: number})

    def removenumber(self, name):
        directory.pop(name)

    def getnumber(self, name):
        print(("{}'s phone number is {}.").format(name, directory.get(name)))

    def findnumber(self, name):
        for x in directory:
            if x.find(name) >= 0:
                print (("{}'s phone number is {}.").format(name, directory.get(x)))

    def binary_search(self, x):
        low = 0
        high = len(directory)-1

        while low<= high:
            mid = (high + low) // 2

            if x in str(p[mid]):
                print(p[mid])

            elif ord(x[0]) > ord(p[mid]):
                low = mid + 1

            else:
                low = mid-1

            

        

    def display(self):
        print(directory)
        
x = PhoneBook()
x.addnumber("Bob Peterson", "1234567890")
x.addnumber("Carl Junior", "9876543210")
x.display()
x.removenumber("Carl Junior")
x.display()
x.getnumber("Bob Peterson")
x.findnumber("Bob")
x.addnumber("Jimmy Johnson", "2468101214")
x.findnumber("Jimmy")
x.findnumber("Peterson")
x.binary_search("Bob")
