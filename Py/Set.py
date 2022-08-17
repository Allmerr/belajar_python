'''
when we want make sure that a collection of values can't have any duplicate
we store it in a set
'''
cities = {"Kyoto","Kyoto","Oslo"}# automatically he will update only one "Kyoto"
print(cities)

# to add a new value to a set 
cities.add("Shanghai")
print(cities)

'''
in list we can access and update elements like cities[0]
but we cant do that in set 
we can only check an elemnets using in
'''
print("bogor" in cities)

# we can also use for loop
for destination in cities:
    print(f'My destination city is {destination}')

# to remove a set 
cities.remove('Kyoto')
print(cities)

# if value didn't in set  we will get an error
if "bogor" in cities :
    cities.remove('bogor') 

print('----------______________-----------')  

grocery_list = ["kunyit", "bawang merah", "bawang putih", "kunyit"]
# to eliminate duplicates from a list like grocery_list we can transform it to set
grocery_set = set(grocery_list)
grocery = list(grocery_set)
print(grocery)


'''
when all elements of a set like "chat" are present in another set like "friends"
we say 'chat' is subset to 'friends'
'''

friends = {"Emma", "Jen", "Rob", "Ed"} 
chat = {'Jen', 'Ed'}# jadi semua yang ada di chat harus ada di friends
is_subset = chat.issubset(friends)
print(is_subset)


# we can join two sets 
friends = {"Emma", "Rob", "Ed"} 
chat = {'Jen', 'Ed', 'ujang'}
All_friends = chat.union(friends)# kita masukan friends ke chat dan otomatis ngehapus yang ada
print(All_friends)

#to see whetever from two set have a simmiliarty
friends = {"Emma", "Rob", "Ed"} 
chat = {'Jen', 'Ed', 'ujang'}
best_friend = friends.intersection(chat)
print(best_friend)

# to get a set of elements that are present in classmates but not in friends
classmates = {'allia', 'raka', 'valliant', 'raffly'}
friends = {'riffky', 'zaka', 'raffly'}

classmates_only = classmates.difference(friends)
print(classmates_only)
























