import random

class Money:
    def __init__(self, rare = False, clean = True, heads =True, **kwargs):

        for key,value in kwargs.items():
            setattr(self,key,value)
        
        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads

        if self.is_rare:
            self.value = self.original_value*2
        else:
            self.value = self.original_value

        if self.is_clean:
            self.color = self.clean_color
        else:
            self.color = self.rusty_color

    def rust(self):
        self.color = self.rusty_color

    def clean(self):
        self.color = self.clean_color

    def __del__(self):
        print("Coin Spent!")

    def flip(self):
        heads_options = [True,False]
        choice = random.choice(heads_options)
        self.heads = choice

    def __str__(self):
        if self.original_value >= 1:
            return "${} bill".format(self.original_value)
        elif self.original_value == 0.01:
            return "Penny"
        elif self.original_value == 0.05:
            return "Nickel"
        elif self.original_value == 0.10:
            return "Dime"
        elif self.original_value == 0.25:
            return "Quarter"



class Penny(Money):
    def __init__(self):
        data= {
            "original_value": 0.01,
            "clean_color": "bronze",
            "rusty_color": "brownish",
            "num_edges": 1,
            "length": 19.05,
            "thickness": 1.52,
            "mass": 2.5
            }
        super().__init__(**data)

class Nickel(Money):
    def __init__(self):
        data= {
            "original_value": 0.05,
            "clean_color": "silver",
            "rusty_color": "dark gray",
            "num_edges": 1,
            "length": 21.21,
            "thickness": 1.95,
            "mass": 5
            }
        super().__init__(**data)


class Dime(Money):
    def __init__(self):
        data= {
            "original_value": 0.10,
            "clean_color": "silver",
            "rusty_color": "dark gray",
            "num_edges": 1,
            "length": 17.91,
            "thickness": 1.35,
            "mass": 2.268
            }
        super().__init__(**data)


class Quarter(Money):
    def __init__(self):
        data= {
            "original_value": 0.25,
            "clean_color": "silver",
            "rusty_color": "dark gray",
            "num_edges": 1,
            "length": 24.26,
            "thickness": 1.75,
            "mass": 5.67
            }
        super().__init__(**data)


class One_Dollar_Bill(Money):
    def __init__(self):
        data= {
            "original_value": 1,
            "clean_color": "light green",
            "rusty_color": None,
            "num_edges": 4,
            "length": 156,
            "thickness": 0.11,
            "mass": 1
            }
        super().__init__(**data)


class Five_Dollar_Bill(Money):
    def __init__(self):
        data= {
            "original_value": 5,
            "clean_color": "light green",
            "rusty_color": None,
            "num_edges": 4,
            "length": 156,
            "thickness": 0.11,
            "mass": 1
            }
        super().__init__(**data)


class Ten_Dollar_Bill(Money):
    def __init__(self):
        data= {
            "original_value": 10,
            "clean_color": "light green",
            "rusty_color": None,
            "num_edges": 4,
            "length": 156,
            "thickness": 0.11,
            "mass": 1
            }
        super().__init__(**data)


class Twenty_Dollar_Bill(Money):
    def __init__(self):
        data= {
            "original_value": 20,
            "clean_color": "light green",
            "rusty_color": None,
            "num_edges": 4,
            "length": 156,
            "thickness": 0.11,
            "mass": 1
            }
        super().__init__(**data)
        

money = [Penny(), Nickel(), Dime(), Quarter(), One_Dollar_Bill(),
         Five_Dollar_Bill(), Ten_Dollar_Bill(), Twenty_Dollar_Bill()]

for item in money:
    arguments = [item, item.value, item.color,item.num_edges,
                 item.length, item.thickness, item.mass]

    string = "{} - Value: ${}, Color: {}, Number of Edges: {}, Length(mm): {}, Thickness(mm): {}, Mass(grams): {}".format(*arguments)
    print(string)
