# These are examples of OOP
class Soda_Machine:
  paid = False
  balance = 0

  def eject_soda(self):
    if self.paid == False:
      print('Please insert money')
    else:
      print('Enjoy the soda!')

  def pay(self, amount):
    self.balance += amount
    
  def select_soda(self):
    if self.balance >= 1:
      self.paid = True
      self.balance -= 1
    else:
      self.paid = False

soda = Soda_Machine()
soda.pay(2)
soda.select_soda()
soda.eject_soda()

class Archer:
  arrows = 10
  points = 0
  empty = False
  def shoot(self):
    if self.arrows > 0:
      print('Aim... and shoot!')
      self.arrows -= 1
    else:
      self.empty = True

  def bullseye(self):
    self.points += 3
    
  def reload(self):
    if self.empty == True:
      self.arrows = 10
      self.empty = False

game = Archer()
game.shoot()
game.bullseye()   

class Player:
  def __init__(self, name):
    self.name = name

class Computer(Player):
  def __init__(self):
    super().__init__("NPC")

  def respond(self, player):
    print("Hello", player.name, "I am", self.name)

class User(Player):
  def __init__(self, name, level):
    super().__init__(name)
    self.level = level

  def greet(self):
    print("Hi! What is your name?")

computer = Computer()
user = User("Kevin", 1)
user.greet()
computer.respond(user)

class Automobile:
  def go(self):
    print("Moving forward")

  def stop(self):
    print("Stopping")

class Motorcycle(Automobile):
  def wheelie(self):
    print("Popping a wheelie")

class Racecar(Automobile):
  def reverse(self):
    print("Reversing")

  def goTo100(self):
    print("Increasing to 100 mph")

motorcycle = Motorcycle()
motorcycle.go()
motorcycle.wheelie()
racecar = Racecar()
racecar.goTo100()

class FoodDelivery: 
  def __init__(self, number, items): 
    self.number = number 
    self.items = items 
 
  def submit_order(self): 
    print(f"Submitting order: {self.number}") 
 
  def make_food(self, item): 
    print(f"Made {item}") 
 
  def package_item(self, item): 
    print(f"Packaging {item}") 
     
  def complete_order(self): 
    self.submit_order() 
    for i in self.items: 
      self.make_food(i) 
      self.package_item(i) 
    print("Delivering order", self.number)
    print("Hope you enjoy the food")

gofood = FoodDelivery("Room 3", ["Sate seporsi", 'Sop Iga', 'Nasi putih'])
gofood.complete_order()

class Polygon:
  def perimeter(self):
    print("Perimeter")

class Rectangle(Polygon):
  def __init__(self, length, width):
    self.length = length
    self.width = width
  def perimeter(self):
    return 2 * self.length * self.width

class Square(Polygon):
  def __init__(self, side):
    self.side = side

  def perimeter(self):
    return 4 * self.side

class Triangle(Polygon):
  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c
    
  def perimeter(self):
    return self.a + self.b + self.c

persegi_panjang = Rectangle(10,23)
print(persegi_panjang.perimeter())
persegi = Square(20)
print(persegi.perimeter())
segitiga = Triangle(10,5,5)
print(segitiga.perimeter())

class Employee: 
  def __init__(self, name, job): 
    self.name = name 
    self.job = job 
     
  def tasks(self): 
    print("Tasks are:") 
    
class Manager(Employee): 
  def __init__(self, name, job, staff): 
    super().__init__(name, job) 
    self.staff = staff 
 
  def tasks(self): 
    print("Oversees:") 
    print(self.staff) 
 
class Associate(Employee): 
  def tasks(self): 
    print("Take orders from manager")

manager = Manager("Kevin", "Data analysts", "Project")
manager.tasks()