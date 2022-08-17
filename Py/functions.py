'''
Instead of rewriting the same code, we can use FUNCTIONS to group related code and 
perform the task in one place 
'''
# reusing code with functions
def first_world():
    print('Hello')
    print('world')

first_world()

# creating parameters
def weather_update(weather):
    print(f'Today weather : {weather}')

weather_update("light rain")

# return values and using multiple parameters
def calculator(first,second,jenis):
    total = 0
    first = int(first) # you cannt accses variable inside this because it is inside functions
    second = int(second)
    if jenis == "*" :
        total = first * second
        return total 
    elif jenis == "/" :
        total = first / second
        return total
    elif jenis == "+" :
        total = first + second
        return total
    elif jenis == "-" :
        total = first - second
        return total
    else :
        return 'Your input is wrong'

first = input("angka pertama ? ")
second = input("angka kedua ? ")
kind = input("jenis hasil dari ? ")

print(calculator(first,second,kind))

# functions with lists 

def is_multiplayer(players):
    is_true = len(players) > 1
    return is_true

players = ["amy", 'mateo', "rufus"]
is_multiplayer = is_multiplayer(players)
print(f"Team have more than one people {is_multiplayer}")

def change_team(player_in,player_out,team):
    team = " ".join(team)
    team = team.replace(player_out,player_in)
    team = team.split()
    return team

team = ['asep', 'wildan', 'ujang']
player1 = "kevin"
player2 = "asep"
print(change_team(player1,player2,team))

# function with for loop

def display_progress(total_files):
    for i in range(total_files):
        print(f'Downloading file {i} out of {total_files}')

display_progress(2)


def schedule_classes(classes, times):
  schedule = []

  index = 0
  while index < len(classes):
    scheduled_class = classes[index] + ": " + times[index]
    schedule.append(scheduled_class)
    index += 1

  return schedule


classes = ["seni budaya", "bahasa jepang"]
times = [ "1p.m.", "3p.m."]
schedule = schedule_classes(classes, times)
print(f"Monday's schedule: {schedule}")











