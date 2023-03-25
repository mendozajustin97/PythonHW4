#!/usr/bin/env python
# coding: utf-8

# # Object-Oriented-Programming (OOP)

# ## Tasks Today:
# 
#    
# 
# 1) <b>Creating a Class (Initializing/Declaring)</b> <br>
# 2) <b>Using a Class (Instantiating)</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Creating One Instance <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Creating Multiple Instances <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) In-Class Exercise #1 - Create a Class 'Car' and instantiate three different makes of cars <br>
# 3) <b>The \__init\__() Method</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) The 'self' Attribute <br>
# 4) <b>Class Attributes</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Initializing Attributes <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Setting an Attribute Outside of the \__init\__() Method <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Setting Defaults for Attributes <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) Accessing Class Attributes <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) Changing Class Attributes <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; f) In-Class Exercise #2 - Add a color and wheels attribute to your 'Car' class <br>
# 5) <b>Class Methods</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Creating <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Calling <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Modifying an Attribute's Value Through a Method <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) Incrementing an Attribute's Value Through a Method <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) In-Class Exercise #3 - Add a method that prints the cars color and wheel number, then call them <br>
# 6) <b>Inheritance</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Syntax for Inheriting from a Parent Class <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) The \__init\__() Method for a Child Class (super()) <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Defining Attributes and Methods for the Child Class <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) Method Overriding <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) In-Class Exercise #4 - Create a class 'Ford' that inherits from 'Car' class and initialize it as a Blue Ford Explorer with 4 wheels using the super() method <br>
# 7) <b>Classes as Attributes</b> <br>
# 8) <b>Exercises</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Exercise #1 - Turn the shopping cart program from yesterday into an object-oriented program <br>

# ## Creating a Class (Initializing/Declaring)
# <p>When creating a class, function, or even a variable you are initializing that object. Initializing and Declaring occur at the same time in Python, whereas in lower level languages you have to declare an object before initializing it. This is the first step in the process of using a class.</p>

# In[4]:


class Car():
    wheels = 4
    color = 'blue'


# ## Using a Class (Instantiating)
# <p>The process of creating a class is called <i>Instantiating</i>. Each time you create a variable of that type of class, it is referred to as an <i>Instance</i> of that class. This is the second step in the process of using a class.</p>

# ##### Creating One Instance

# In[ ]:


ford = Car()

print(ford.color)


# ##### Creating Multiple Instances

# In[ ]:


chevrolet = Car()
honda = Car()
porsche = Car()

print(type(porsche.color))


# ##### In-Class Exercise #1 - Create a Class 'Car' and Instantiate three different makes of cars

# In[ ]:


class Car ():
    doors = 4
    wheels = 4
    color = 'red'
    
honda = Car()
toyota = Car()
acura = Car()

print(honda.color)
print(toyota.wheels)
print(acura.doors)


# ## The \__init\__() Method <br>
# <p>This method is used in almost every created class, and called only once upon the creation of the class instance. This method will initialize all variables needed for the object.</p>

# In[ ]:


class Car():
    engine = '4.7L'  # Global within class - any method inside the class can call upon this variable
    
    def __init__ (self, color, wheels):
        self.color = color
        self.wheels = wheels
    
mazda = Car('black', 4)
subaru = Car('blue', 6)

print(mazda.color)
print(subaru.color)


# ##### The 'self' Attribute <br>
# <p>This attribute is required to keep track of specific instance's attributes. Without the self attribute, the program would not know how to reference or keep track of an instance's attributes.</p>

# In[ ]:


# see above

class House():
    
    def __init__(self, dishes, wall):
        self.wall = wall
        self.dishes = dishes
        
    def washDishes(self):
        if self.dishes.lower() == 'dirty':
            print(self.wall)
    
    def rockClimbingWall(self):
        if self.wall.lower() == 'yes':
            return 'rock on, climber!'
        else:
            return 'why on earth would you not want a rock climbing wall in your house'
        
justins_house = House('dirty', 'no')

justins_house.washDishes()
justins_house.rockClimbingWall()


# ## Class Attributes <br>
# <p>While variables are inside of a class, they are referred to as attributes and not variables. When someone says 'attribute' you know they're speaking about a class. Attributes can be initialized through the init method, or outside of it.</p>

# ##### Initializing Attributes

# In[ ]:


# see above
class Toy():
    kind = 'car' # This is called a constant
    
    def __init__(self, rooftop, horn, wheels):
        self.rooftop = rooftop #These are our attributes
        self.horn = horn
        self.wheels = wheels
        
tonka_truck = Toy(1,1,4) # 1 Rooftop, 1 horn, 4 wheels
hotwheels_car = Toy(2, 3, 8) # 2 Rooftop, 3 horns, 8 wheels


# ##### Accessing Class Attributes

# In[ ]:


# See Above
tonka_truck.rooftop
hotwheels_car.wheels


# ##### Setting Defaults for Attributes

# In[ ]:


class Car():
    engine = '4.7L' 
    
    def __init__(self, wheels):
        self.wheels = wheels
        self.color = 'Blue'
honda = Car(4)
honda.color


# ##### Changing Class Attributes <br>
# <p>Keep in mind there are global class attributes and then there are attributes only available to each class instance which won't effect other classes.</p>

# In[ ]:


jeep = Car(8)

print(f'Before change: {jeep.color}')

jeep.color = 'White'

print(f'\nAfter Change: {jeep.color}')
print(honda.color)


# In[ ]:





# ##### In-Class Exercise #2 - Add a doors and seats attribute to your 'Car' class then print out two different instances with different doors and seats

# In[ ]:



class Car():
    
    def __init__(self, doors, seats = 4):
        self.doors = doors
        self.seats = seats

toyota = Car(2,2)
porsche = Car(4)

print(f'Toyota seats: {toyota.seats} and Toyota doors: {toyota.doors}')
print(f'Porsche seats: {porsche.seats} and Porsche: {porsche.doors}')


# ## Class Methods <br>
# <p>While inside of a class, functions are referred to as 'methods'. If you hear someone mention methods, they're speaking about classes. Methods are essentially functions, but only callable on the instances of a class.</p>

# ##### Creating

# In[ ]:


class ShoppingBag():
    """
        The ShoppingBag class wil have handles, capacity, 
        and items to place inside.
        
        Attributes for the class:
        - handles: expected to be an integer
        - capacity: expected to be a string OR an integer
        - items: expected to be a list
    """
    
    def __init__(self, handles, capacity, items):
        self.handles = handles
        self.capacity = capacity
        self.items = items
        
    #Write a method that shows the items in our ShoppingBag / this is our items list
    def showShoppingBag(self):
        print("You have items in your bag!")
        for item in self.items:
            print(item)
                
    #Show capacity of ShoppingBag - how much room is left
    def showCapacity(self):
        print(f'Your capacity is: {self.capacity}')
        
    #Add item(s) to the items list for the ShoppingBag
    def addToShoppingBag(self):
        products = input('What would you like to add? ')
        self.items.append(products)
            
    #Change the capacity of the ShoppingBag
    def changeBagCapacity(self, capacity):
        self.capacity = capacity
            
    #Increase the capacity of the ShoppingBag by a default amount that we set to 10
    def increaseCapacity(self, changed_capacity = 10):
        if self.capacity == isinstance(self.capacity, str):
            print("We can't add that here")
                
        else:
            self.capacity += changed_capacity


# ##### Calling

# In[ ]:


# See Above

wholeFoods_bag = ShoppingBag(2,10,[])

#Create a function to run the ShoppingBag methods on our wholeFoods_bag instance

def run():
    while True:
        response = input('What do you want to do? add/show/quit ')
        
        if response.lower() == 'quit':
            wholeFoods_bag.showShoppingBag()
            print('Thanks for shopping')
            break 
        elif response.lower == 'add':
            wholeFoods_bag.addToShoppingBag()
        elif response.lower() == 'show':
            wholeFoods_bag.showShoppingBag()
        else:
            print('Try another command')
            
run()


# ##### Modifying an Attribute's Value Through a Method

# In[ ]:


#show the capacity

wholeFoods_bag.showCapacity()
print('Capacity AFTER the change...')
wholeFoods_bag.changeBagCapacity(40)
wholeFoods_bag.showCapacity()


# ##### Incrementing an Attribute's Value Through a Method

# In[ ]:


wholeFoods_bag.showCapacity()
print('After increase: ')
wholeFoods_bag.increaseCapacity()
wholeFoods_bag.showCapacity()


# ##### In-Class Exercise #3 - Add a method that takes in three parameters of year, doors and seats and prints out a formatted print statement with make, model, year, seats, and doors

# In[ ]:


# Create class with 2 paramters inside of the __init__ which are make and model

# Inside of the Car class create a method that has 4 parameter in total (self,year,door,seats)

# Output: This car is from 2019 and is a Ford Expolorer and has 4 doors and 5 seats


# ## Inheritance <br>
# <p>You can create a child-parent relationship between two classes by using inheritance. What this allows you to do is have overriding methods, but also inherit traits from the parent class. Think of it as an actual parent and child, the child will inherit the parent's genes, as will the classes in OOP</p>

# ##### Syntax for Inheriting from a Parent Class

# In[ ]:


# Create a parent class and call it Animal
class Animal():
    acceleration =  9.8
    
    def __init__(self, name, species, legs = 4):
        self.name = name
        self.species = species
        self.legs = legs
        
    #Generic Parent Method -This is not overriding anything
    def makeSound(self):
        print('Make some generic sound')
        
#Now we are making our child class... Dog
class Dog(Animal):
    speed = 15
    
    def printInfo(self):
        print(f'The dog has {self.speed}mph in speed and {self.acceleration}')

#Creation of our Grand-Child Class --Mutt
class Mutt(Dog):
    color = "Tan"
    
    #Override the ANIMAL class - using the Dog class to override the __init__ from Animal
    def __init__(self, name, species, eye_color, legs = 4):
        Dog.__init__(self,name,species,legs)
        self.eye_color = eye_color
        
    #Override the makeSound method (which is coming from... Animal)
    def makeSound(self):
        noise = 'Bark'
        return noise
    
lassie = Dog('Lassie', 'Dog')
basic_animal = Animal('Generic Animal Name', 'Generic Animal Species')
buster = Mutt('Buster', 'Mutt', 'Brown')

print(buster.makeSound())
print(lassie.makeSound())
print(buster.acceleration)
print(buster.speed)


# ##### The \__init\__() Method for a Child Class - super()

# In[ ]:


class Puppy(Dog):
    color = 'black and brown'
    
    #Override the Animal class __init__ (via Dog class)
    def __init__(self, name, species, eye_color, legs = 4):
        super().__init__(name,species,legs)
        self.eye_color = eye_color
        
    #Override the makeSound method
    def makeSound(self):
        noise = 'Bark'
        return noise

lassie = Dog('Lassie', 'Dog')
basic_animal = Animal('Generic Animal Name', 'Generic Animal Species')
buster = Mutt('Buster', 'Mutt', 'Brown')

print(buster.makeSound())
print(lassie.makeSound())
print(buster.acceleration)
print(buster.speed)    


# ##### Defining Attributes and Methods for the Child Class

# In[ ]:


# See Above


# ##### Method Overriding

# In[ ]:


# See Above


# ## Classes as Attributes <br>
# <p>Classes can also be used as attributes within another class. This is useful in situations where you need to keep variables locally stored, instead of globally stored.</p>

# In[ ]:


class Battery():
    volts = 7.8
    
    def __init__(self, cells):
        self.cells = cells
        
class Car():
    def __init__(self, year, make, model, battery):
        self.year = year
        self.make = make
        self.model = model
        self.battery = battery
        
        
    def printInfo(self):
        return f'{self.year} {self.make} {self.model} {self.battery.cells}'
        
my_battery = Battery(20)
tesla = Car(2019, 'Tesla', 'Model X', my_battery)

print(tesla.battery.cells)
tesla.printInfo()


# # Exercises

# ### Exercise 1 - Turn the shopping cart program from yesterday into an object-oriented program
# 
# The comments in the cell below are there as a guide for thinking about the problem. However, if you feel a different way is best for you and your own thought process, please do what feels best for you by all means.

# In[ ]:


# Create a class called cart that retains items and has methods to add, remove, and show

class Cart():
    
    def __init__(self, items):
        self.items = items
        
    def showCart(self):
        print("You have the following items in your bag: ")
        for item in self.items:
            print(item)
    
    def addCart(self):
        products = input('What would you like to add? ')
        self.items.append(products)
    def removeCart(self):
        remove = input('What would you like to remove? ')
        self.items.remove(remove)
        
bag = Cart([])

def run():
    while True:
        response = input('What do you want to do? add/show/remove or quit: ')
        
        if response.lower() == 'quit':
            bag.showCart()
            print('Thanks for shopping')
            break
        elif response.lower() == 'add':
            bag.addCart()
         
        elif response.lower() == 'show':
            bag.showCart()
        
        elif response.lower() == 'remove':
            bag.removeCart()
            
run()
    


# ### Exercise 2 - Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case

# In[ ]:


class IOString():
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input()

    def print_String(self):
        print(self.str1.upper())

str1 = IOString()
str1.get_String()
str1.print_String()

