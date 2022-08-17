'''
Pyhton allows us to use negative indexing to retrieve values from the end indexable object
'''

users = ['Anna', 'Jack', 'Elanor']
latest = users[-1]
second = users[-3] # if out of range we will receive an error
print(latest)
print(second)
# negative indexing means that we retrieve an element from most side of a list
# we can do this to tupple because immutable and so cannt be modified

# the (del) allows us to delate object
users = ['Anna', 'Jack', 'Elanor']
del users[-2]
print(users)

latters = {'a', 'b', 'c'}
del latters # we delate the whole object
# print(latters) # it will return error to us becasue variable latters is gone

product = {
    "category" : 'book',
    "price" : 4.99,
    "market_place" : True
}

del product['market_place']
print(product)

'''
we can also use a format with two colons [start:stop:step]
'''
alphabet = ['a', 'b', 'c', 'd', 'e', 'f']
print(alphabet[1:6:2])
print(alphabet[::2]) 
# we can use step or stop or start with no value 
# By default this will work from the start to the end of the full original list

print('---------------PRACTICE TIME--------------')
calls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

staff = ["anna", "ben", "cherry"]
staff_count = len(staff)
early_staff = 2
early_calls = calls[:5]

early_allocation = {}
for employee in staff[:early_staff]:
  position = staff.index(employee)
  early_allocation[employee] = early_calls[position::early_staff]

print(early_allocation)

late_calls = calls[5:]
late_staff = staff[::-1]
late_allocation = {}


for employee in late_staff:
  position = late_staff.index(employee)
  late_allocation[employee] = late_calls[position::staff_count]

print(late_allocation)


print('---------------PRACTICE TIME--------------')


bpm = [122, 136, 150, 123, 
       138, 157, 165, 142, 
       132, 148, 162, 146, 
       170, 187, 185, 158,        
       165, 182, 193, 167, 
       158, 167, 182, 169]

total = len(bpm)

half_way = int(total / 2)
first_half = bpm[:half_way]
second_half = bpm[half_way:]

first_avg = sum(first_half) / half_way
second_avg = sum(second_half) / half_way

print("First half average: "+ str(first_avg))
print("Second half average: "+ str(second_avg))

final_mins = bpm[2::4]
breaks = bpm[3::4]
print("During breaks: " + str(breaks))
print("During final minutes: " + str(final_mins))

max_index = bpm.index(max(bpm))
print("Recovery from maximum: " + str(bpm[max_index:]))


print('---------------PRACTICE TIME--------------')


hobbies = ["Archery", "Bowling", "Canoeing", "Dance", "Embroidery", "Flute", "Gymnastics"]

while hobbies[-1] != "Dance":
  del hobbies[-1]

number = str(len(hobbies))
print("These are your " + number + " favourite hobbies:")
print(hobbies)

extras = ["Gym", "Cinema", "Restaurants", "Jewellery", "Coffee", "Netflix", "Bingo"]

costs = [50, 20, 80, 30, 40, 10, 25]
to_save = 100
savings = 0 

while to_save > 0:
  to_save -= costs[-1]
  savings += costs[-1]
  del costs[-1]
  del extras[-1] 

savings = str(savings)
print("You'll save " + savings + " euros by sticking to these extras:")
print(extras)

next_saving = extras[-1]
print('If you need to save more money, take some time off ' + next_saving + '.')


print('---------------PRACTICE TIME--------------')


answers = ["C", "B", "C", "A", "D", "A", "B", "D", "D", "C"]

responses = ["C", "B", "C", "A", "D", "A", "B", "D", "D", "C"]

if responses[-1] == answers[len(responses)-1]:
  correct = True
else:
  correct = False

if not correct:
  del responses[-1]
  print("Sorry, please try the last question again!")

elif len(responses) < len(answers):
  print('Quiz not complete.')
  correct = str(len(responses))
  print("You've got " + correct + " answers correct so far, please add an answer for the next question.")

else:
  print("Well done, you have completed the quiz!")