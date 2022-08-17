''' loops'''
print("lagi")
print("lagi")
print("lagi")
print("lagi")
""" 
one way to repeat lines of codes is to writes them over and over 
again but it took really long time
"""

'''
while True :
  print("ngulang");
# the result we print that for iternity

while False:
  print("ngak kebaca dong");
# it is like if elif else while false they never run
'''

''' now let's focus how to create a loop stop'''

# too stop a loop we start create a variable outside them her name is counter

keep = True 

while keep == True :
  print("terus melangakah")
  # the loop print the entire block
  keep = False
  print("sekali lagi asik")


# too control the times a while loop repeats, we can do with counter again

counter =  1
while counter < 4:
    print(f"test {counter} succses")
    counter += 1
#ini counter dibawah dengan hasil 123
print("_____-------______")
#ini counter diatas dengan hasil 234
counter =  1
while counter < 4:
    counter += 1
    print(f"test {counter} succses")
    
#exercise

days = 1
value = 3

while days < 4 :
    print(f"The value days {days} is ${value}")
    value *= 1.5
    days += 1 
print(f"final value : ${value}")

print("--------------------------")

''' for loops '''
""" we can build with much less code and make it esier to write with"""

print("zero to four")

for repetition in range(5):
    print(repetition)

for i in range(5):
    print("loading page")


print("look!")

line = 0

for i in range(4):
    line += line + i
    print(f"line {line}")
print(f"final line : {line}")









