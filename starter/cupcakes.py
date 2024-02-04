from abc import ABC, abstractmethod
import csv
from pprint import pprint

class Cupcake(ABC):
    size = 'regular'
    def __init__(self, name, price, flavor, frosting, filling, sprinkles):
        self.name = name
        self.price = price
        self.flavor =flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []

    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)

    @abstractmethod 
    def calculate_price(self, quantity):
        return quantity * self.price
    
    
class Mini(Cupcake):
    size = 'mini'

    def __init__(self, name, price, flavor, frosting):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []

    def calculate_price(self, quantity):
        return quantity * self.price

class Large(Cupcake):
    size = 'large'

    def __init__(self, name, price, flavor, frosting, filling, sprinkles):
        self.name = name
        self.price = price
        self.flavor =flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []

    def calculate_price(self, quantity):
        return quantity * self.price
    
    def custom_filling(self, str):
        self.filling = str

class Doughnut(Cupcake):
    size = 'regular'

    def __init__(self, name, price, flavor, frosting, filling, sprinkles):
        self.name = name
        self.price = price
        self.flavor =flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []

    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)
            self.price += 0.99

    def calculate_price(self, quantity):
        return quantity * self.price

#this_cupcake = Cupcake("cheesecake", 3.59, "cheesecake", 'strawberry', 'strawberry', True)
#
#this_cupcake.frosting = 'chocolate'
#this_cupcake.filling = 'chocolate'
#this_cupcake.name = 'chocolate cheesecake'
#
#this_cupcake.add_sprinkles("oreo", 'butterscotch', 'vanilla')

#print(this_cupcake.sprinkles)

this_cupcake_mini = Mini('chocolate', 1.99, 'chocolate', 'white')
#print(this_cupcake_mini.calculate_price(2))
#print(this_cupcake_mini.name)
#print(this_cupcake_mini.price)
#print(this_cupcake_mini.size)

this_cupcake_large = Large("cheesecake", 3.59, "cheesecake", 'strawberry', 'strawberry', None)

#this_cupcake_large.custom_filling('water')
#print(this_cupcake_large.filling)

the_doughnut = Doughnut('maple bar', 2.99, 'plain', 'maple', 'vanilla', True)

#the_doughnut.add_sprinkles('this', 'that', 'them')
#
#print(the_doughnut.sprinkles)

cupcake1 = Doughnut("Stars and Stripes", 2.98, "Vanilla", "Vanilla", "Chocolate", True)
cupcake1.add_sprinkles("Red", "White", "Blue")
cupcake2 = Mini("Oreo", .99, "Chocolate", "Cookies and Cream")
cupcake2.add_sprinkles("Oreo pieces")
cupcake3 = Large("Red Velvet", 3.99, "Red Velvet", "Cream Cheese", None, None)
cupcake4 = Large("strawberry", 3.99, "vanilla", "strawberry", None, None)
cupcake5 = Doughnut("Starwars", 5.99, "Chocolate", "Vanilla", "Chocolate", False)

cupcake_list = [cupcake1, cupcake2, cupcake3, cupcake4, cupcake5]


def read_csv(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            pprint(row)
#read_csv('sample.csv')

def write_new_csv(file, cupcakes):
    with open(file, 'w', newline='\n') as csvfile:
        fieldnames = ['size', 'name', 'price', 'flavor', 'frosting', 'sprinkles', 'filling']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for cupcake in cupcakes:
            if hasattr(cupcake, 'filling'):
                writer.writerow({'size': cupcake.size, 'name': cupcake.name,'price': cupcake.price,'flavor': cupcake.flavor,'frosting': cupcake.frosting,'filling': cupcake.filling,'sprinkles': cupcake.sprinkles})
            else:
                writer.writerow({'size': cupcake.size, 'name': cupcake.name,'price': cupcake.price,'flavor': cupcake.flavor,'frosting': cupcake.frosting,'sprinkles': cupcake.sprinkles})

#write_new_csv('cupcakes.csv', cupcake_list)
                
def add_cupcake(file, cupcake):
    with open(file, 'a', newline='\n') as csvfile:
        fieldnames = ['size', 'name', 'price', 'flavor', 'frosting', 'sprinkles', 'filling']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if hasattr(cupcake, 'filling'):
            writer.writerow({'size': cupcake.size, 'name': cupcake.name,'price': cupcake.price,'flavor': cupcake.flavor,'frosting': cupcake.frosting,'filling': cupcake.filling,'sprinkles': cupcake.sprinkles})
        else:
            writer.writerow({'size': cupcake.size, 'name': cupcake.name,'price': cupcake.price,'flavor': cupcake.flavor,'frosting': cupcake.frosting,'sprinkles': cupcake.sprinkles})

def delete_one_cupcake(file, cupcake_name):
    with open(file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        cupcakes_new_list = []
        for row in reader:
            cupcakes_new_list.append(row)

        new_cupcake_list = [cupcake for cupcake in cupcakes_new_list if cupcake['name'] != cupcake_name]

        pprint(new_cupcake_list)
        with open(file, 'w', newline='') as csvfile:
            fieldnames = ['size', 'name', 'price', 'flavor', 'frosting', 'sprinkles', 'filling']

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(new_cupcake_list)


def get_cupcakes(file):
    with open(file) as csvfile:
        read = csv.DictReader(csvfile)
        read = list(read)
        return read

def cupcake_search(file, cupcake_name):
    for cupcake in get_cupcakes(file):
        if cupcake['name'] == cupcake_name:
            return cupcake
        
def add_cupcake_dictionary(file, cupcake):
    with open(file, 'a', newline='\n') as csvfile:
        fieldnames = ['size', 'name', 'price', 'flavor', 'frosting', 'sprinkles', 'filling']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(cupcake)

#delete_cupcake('sample.csv', 'Oreo')
#watch out for capitalization