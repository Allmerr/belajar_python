'''
By using a class we can build diffrent configurations without having to create each individual
'''

class Flower :
    name = 'edelwise' # we can add statment print and will be do the same and noting change
    color = ["white", "red"]
    
# how to accses
bunga = Flower() # it is means we call this class in this variable
print(bunga.name) # this means call class from variable bunga and print variavle name
print(bunga.color)
print(bunga.color[0])

# using def in class
class virtual_pet :
    name = "doggy"
    color = 'brown'

    def bark(self): # self is way to be a part of this class
        print("gug gug")

    def display_color(self):
        print(self.color) # self here is a way to accesse the class 

    def change_color(self, new_color): 
        print('Change color from ' ,self.color)
        self.color = new_color
        print('to ', self.color)


hewan = virtual_pet()
hewan.bark()# we just using like usual
hewan.display_color()
hewan.change_color("black")
hewan.display_color()

print('---------------------------------')

'''
There is a method we can use to make class more easy to use, it is called constructor
'''
class Pie :
    def __init__(self, flavor, ingredients): #first accses you have to add variable that needed
        self.flavor = flavor
        self.ingredients = ingredients

    def print_ingredients(self):
        for i in self.ingredients:
            print(i)

applePie = Pie('apple', ['flour', 'eggs', 'apples', 'butter']) # like this
applePie.print_ingredients()

# exemple 

class Character :
    def __init__(self, name, phrase, level, health):
        self.name = name
        self.phrase = phrase
        self.level = level
        self.healh = health

    def greet(self):
        print(self.phrase)

    def level_up(self):
        self.level += 1
        print("Leveled up to" ,self.level)            
    
    def dec_health(self, damage):
        print('Health decresed from', self.healh)
        self.healh -= damage
        print("To", self.healh)

mario = Character('Mario', "It's a me, Mario", 1, 100)
mario.greet()
mario.level_up()
mario.dec_health(25)

























