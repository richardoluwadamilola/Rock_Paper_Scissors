import random

# -: Asking user input :-
user_choice = input('Type your choice for Rock "R" for paper "P" for scissors "S" : ')
computer_choice = random.choice(["P", "R", "S"])

# -: Checking user input valid or not if valid then tell him/her what he/she choose :-
print('\n')

if 'R' in user_choice:
    print('You(Rock).')
elif "P" in user_choice:
    print('You(Paper).')
elif "S" in user_choice:
    print('You(Scissors).')
else:
    print('Invalid Choice.')

# -: Tell user what computer choose :-
if "R" in computer_choice:
    print('Computer(Rock).')
elif "P" in computer_choice:
    print('Computer(Paper).')
else:
    print('Computer(Scissors).')


#  -: Check Who won computer or user :- 
print('\n')
    # if user choose Rock as "R"
if user_choice == 'R':
    if computer_choice == "R":
        print('Tie.')
    elif computer_choice == "P":
        print('Computer Won.')
    else:
        print('You won.')


    # if user choose Paper as "P"

elif user_choice == 'P':
    if computer_choice == 'P':
        print('Tie.')
    elif computer_choice == 'R':
        print('You won.')
    else:
        print('Computer won.')

 
    # if user choose Scissors as "S"

else:
    if computer_choice == 'S':
        print('Tie.')
    elif computer_choice == 'R':
        print('You won.')
    else:
        print('Computer Won.')