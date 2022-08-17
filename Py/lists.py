# i[0] bisa dipanggil
#pop() bisa dipanggil di variable
#.insert(0,) tidak bisa dipanggil di variable 
#.append() tidak bisa dipanggil di variable
a = ["baca","buku"]
a.append(10)
appen = a.append(1)
print(a)
print(appen)

b = ["vas","kaka"]
b.insert(0,10)
inser = b.insert(0,11)
print(b)
print(inser)

c = ["appel", 11, 10]
c.pop()
po = c.pop(1)
print(c)
print(po)


print('''-------------LIST OF DATA-------------''')
"""
 if we had to create a variable for every piece of new data
our code would get very long and complicated
 """

todo_1 = "read"
todo_2 = "work"
todo_3 = "exercise"

""" 
rather than creating a variable for each new data we can collect 
reraleted data inside a list using [ and ] 
"""

todo = ["read","work","excercise"]# inside this is elements
print(todo)

to_do = [todo_1, todo_2, todo_3]
print(to_do)

print('''----------CHANGE DATA--------------''')

lists = ["string", 10, 11.1, True, "london"]# you can fill it with every type 
print(lists)

#IN THERE(elements) has a numbered posisition called an index
print(lists[1] + 1)
print(lists[1] - 10)
print(lists[0],"is")
print(lists[3]== True)
# index start from zero
lists[1]= 100
print(lists)

valid = True
trough = [valid == True]
print(trough)

total = lists[1] - 90
print(total)

city = lists[4]
print(f"{city} is in english")

print('------------UPDATING LISTS-------------')
''' rules : you can only add one type in them '''


lists = ["alpen", 24,]
a = lists.append(False) # you can do with or without variable (a)
print(lists)
print(a)
# .append() to add thing in last list

city = ["tokyo"]
city.insert(1,"is a city")
print(city)
# .insert(0,) meanns add in zero index


work = ["wasihg laundry","clean myroom"]
a = work.pop()#example you can add in () number for index you would like
print(work)#pop() remove last elements
print(a)# JUST for pop you can call the elements you remove
## add.pop() for remove element you would like


initials = ["RM", "LP"]
a = initials.append("LC")
b = initials.insert(1, "LS")
c = initials.pop(0)
print(initials)
print(a)#hasil none
print(b)#hasil none
print(c)#hasil sesuai dimita


print("___--___LOOPING OVER LISTS____--____")

"""
there is an easy way to loop through all the elements of lists by using 
(for) loop
"""

score_test = [75,90,80,85]
attitude = int(input("nilai ?... "))
for i in score_test : 
  i += attitude
  print(i)#the loop will run as many elements as there are in the list
  print(score_test)
 
print("___DECIDING WITH LISTS________")
''' we can count elements in lists and use them '''
  
items = ["book","laptop","food"]

much = len(items)  #len will count how many elements in your lists
if much > 2 :
  print(f"you bring {much} items :")
  for i in items:
    print(i)
  print("bring a bag! ")
if much < 2 : 
  print(f"you only buy {much} items pick it with hands")

print("-------exercise time ___________")
  
  
nilai = [80,55,70,90,80]  
nilai_tertinggi = nilai[0]  
  
for i in nilai :
  if i > nilai_tertinggi :
    nilai_tertinggi = i
print(f"the highest level is {nilai_tertinggi}")      
  
  