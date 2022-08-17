movies = ["yesterday", "take this waltz", 2008, 2019]
# this list contains movies like "vertigo" and release dates like 1958
# but it'nt clear which date belongs to which movie

movies_tuples = [("take this waltz", 2008), ("yesterday", 2019)]
# tuples help us group diffrent pieces of data belong together 
print(movies_tuples)

# we create tuples similoarly to lists but we use ()
movie = ("take this waltz", 2008)
print(movie)

scores = [("mia",90),("leo",85)]
# we can stores tuple in list 
print(len(scores))
print(scores[0])
mia_score = scores[0]# we can save this in variable
print(mia_score)

# we use for/while
for user_score in scores :
    print(f'result {user_score}')

index =  0
while index < len(scores):
  print(f'result {scores[index]}')
  index += 1


# the main diffrence is that unlike lits we can't update, add, or delate values from tuples
movie = ("take this waltz", 2008)
# movie.append("wall-e") make error
# movie[0] = ("wall-e") make error
# since tuples are immutable,we use them to store information that shouldnt be modified 

print("-----------       -----------------")

# Tiples are useful because they allow us to return multiple values from function 
# using LIST to allow ypu change the value
def get_top_three(players):
  return players[0], players[1], players[2]

players = ["Sue", "Ed", "Ann", "Ty"]
top_three = get_top_three(players)
print(f"First: {top_three[0]}")
print(f"Second: {top_three[1]}")
print(f"Third: {top_three[2]}")

# using list when you want to change the value
def form_team(players):
  team = []
  team.append(players[0])
  team.append(players[2])
  return team

players = ["Sue", "Ed", "Ann", "Ty"]
team = form_team(players)
team[0] = "Chloe"
print(team)



def get_scores_data(score_list):
    small = min(score_list)
    high = max(score_list)
    return small,high

scores_int = input("input your number ? ")
scores_list = scores_int.split()
data = get_scores_data(scores_list)

smallest = data[0]
highest = data[1]

print(f'smallest number is {smallest}')
print(f'highest number is {highest}')


# this is the efficient from the get_score_data()
def get_number_data():
    scores_int = input("input your number ? ")
    scores_list = scores_int.split()
    small = min(scores_list)
    high = max(scores_list)
    print(f'smallest number is {small}')
    print(f'highest number is {high}')





















