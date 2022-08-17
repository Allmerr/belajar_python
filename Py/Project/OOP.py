# In OOP, we use methos to update existing values of an object

# like this
class Piggy :
    value = 0

    def addMoney(self, amount):
        self.value += amount

    def displayMoney(self):
        print(f'Your balance on your account is {self.value}')    

myPiggy = Piggy()
myPiggy.addMoney(25)
myPiggy.displayMoney()

# when we create ojects one by one we run into the problem having duplicate code 
class Person1:
  name = "Sam"
  def greet(self):
    print("Hi!")

class Person2:
  name = "Mike"
  def greet(self):
    print("Hi!")

class Person3:
  name = "Jane"
  def greet(self):
    print("Hi!")

# we use inheritance to make our code efficient. through inheritance, classes receive methods from other classes

class Greetings:
    def greet(self):
        print("Hi!") 

class Person(Greetings): # this was inheritance
    name = "George"

p = Person()
p.greet() # so we can accses variable and functions there


# we can create object that own properties and inherit methods from both

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self): 
    print("Hi!")

class Student(Person):
  def __init__(self, name, age, major):
      super().__init__(name,age) # this means accses inherited functon name __init__
      self.major = major

nama = input("masukan nama anda? ")
umur = int(input("masukan umur anda? "))
jurusan = input("masukan jurusan anda? ")

student = Student(nama, umur, jurusan)
print(f"Hello! {student.name} dari jurusan {student.major}")

'''
imagine a car drive in road, a car does a lot of things at the same time. 
for example, a car injects and ignites fuel thousands of times a minute just to say running
'''
class Car:
  def injectFuel(self):
    print("Spraying fuel")
  def igniteFuel(self):
    print("Boom!")  


car = Car()
car.injectFuel()
car.igniteFuel()
car.injectFuel()
car.igniteFuel()    
# but it's hard to read and use and maybe will incrase the chance we'll make a mistake

class Mobil:
  on = False
  
  def injectFuel(self):
    print("Spraying fuel")
  
  def ignitefuel(self):
    print("Boom!")  

  def stopEngine(self):
    self.on = False

  def startUp(self):
    self.on = True
    while self.on:
      self.injectFuel()
      self.ignitefuel()

mobil = Mobil()
# mobil.startUp() this will make infinate loop but it is work 

class Slideshow: 
  def __init__(self, slides): 
    self.slides = slides 
    self.current = 1 
  
  def viewNextSlide(self): 
    self.current += 1 
  
  def play(self): 
    while self.current <= self.slides: 
      print('Slide', self.current, 'show!') 
      self.viewNextSlide() 
 
slideshow = Slideshow(5) 
slideshow.play()


class Feline:
  def speak(self):
    print("Meow")

class Cat(Feline):
  def lick(self):
    print("Licking paw")

class Lion(Feline):
  def prey(self):
    print("Pounces on prey")
  def speak(self): # though before we have made speak function in feline class the real is we use / his own def we use if we met the same function
      print("ROAR!")

cat = Cat()
cat.speak()
lion = Lion()
lion.speak()