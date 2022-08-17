'''
 A list comprehension is a way to create a new list by applying an expresion on each element
'''

# we know this way before
prices = [10, 34, 34, 12]
half = []

for price in prices :
    half_price = price/2 
    half.append(half_price)

print(half)

# we can build the half list as before using list comprehension
prices = [10, 34, 34, 12]
half = [price/2 for price in prices]
print(half)

# to create a copy of original list
prices = [10, 34, 34, 12]
price_copy = [price for price in prices] # just never put anything after first (price)
print(price_copy)

words = ["apple", "samsung", "infinix"]
a_count = [word.count('a')for word in words]
print(a_count)

# function as expressions
prices = [10, 34, 34, 12]
def half(num):
    return num/2 # we only use return for list comp

setengah = [half(price) for price in prices]
print(setengah)

authors = ["Rowling JK", "christie Agatha"]

def reserve(name):
    parts = name.split()
    return parts[1] + ' ' + parts[0]

authors_update = [reserve(name) for name in authors]
print(authors_update)

# if statments with list comp
scores = [12, 23, 34, 25 ,13]
high = scores[0]
high_scores = [score for score in scores if score > 20 and score < 30]
print(high_scores)
