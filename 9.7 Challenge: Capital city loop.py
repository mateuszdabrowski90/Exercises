import random

capitals_dict = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
}

state = random.choice(list(capitals_dict))
capital = capitals_dict[state]

print(state)
answer = ""
a = 0
while a != 1:
    answer = input(f"What is a capital of {state}? ").lower()
    if answer == capital.lower():
        print("Correct")
        a = 1
    elif answer == "exit":
        print("Goodbye")
        a = 1