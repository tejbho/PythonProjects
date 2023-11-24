class Employee:
    domains = set()
    allowed_domains = {'yahoo.com', 'gmail.com', 'outlook.com'}

    def __init__(self,name,email):
        self.name = name
        self.email = email
        Employee.domains.add(self)
   
    def display(self):
       print(self.name, self.email)

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        x = new_email[new_email.index('@')+1 : ]
        if x in Employee.allowed_domains:
                      self._email = new_email
        else:
            raise RuntimeError("this domain isn't allowed")
            
e1 = Employee('John','john@gmail.com')
e2 = Employee('Jack','jack@yahoo.com')
e3 = Employee('Jill','jill@outlook.com')
e4 = Employee('Ted','ted@yahoo.com')
e5 = Employee('Tim','tim@gmail.com')
e6 = Employee('Mike','mike@yahoo.com')

e1.display()
e2.display()
e3.display()

