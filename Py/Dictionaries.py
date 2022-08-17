car_data = ["suzuki",1960,True,1980,2009]
# the name of car is suzuki the year buy is 1960 and is_ranted is true
# but we cann't know by just looking the car_data 

'''To associate a meaning to each value in a collection of values, we use dictinory'''
car_data = {
    "brand" : 'suzuki', # brand is key
    'year'  : 1960, # 1960 is value and you can only input once
    ('ranted','is_sell'): True, # we can set key str,int,bool
    'restoration' : [1980,2018] # value can be any type
}

print(car_data)

# we access dictinory values by their key
actor_bio = {
    'name' : "BIll murray",
    'known for' : ["Lost in Translation", "Rushmore"],
    'sallary' : "$180 million"
}

print(actor_bio['known for'])

# using for loop
for i in actor_bio:
    print(f"{i} : {actor_bio[i]}")

    
# to update the value 
actor_bio["age"] = 71
print(actor_bio)


#to check if a dictinory containes a certain key
print('age' in actor_bio)

def is_old():
    betul = "age" in actor_bio
    if betul :
        age = actor_bio["age"]
        if age >= 60 :
            print("he is old man")
        else : 
            print("he is young man ")

is_old()

#to remove a value 
ticket = {
    "seat no." : 23,
    "window" : True
}
ticket.pop("window")
print(ticket)

#attempt to remove a key that doesnt't exist gives us an error
#to avoid that we ue if
if "destination" in ticket:
    ticket.pop("destination")

print(ticket)








