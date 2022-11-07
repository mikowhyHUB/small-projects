# Guess the number game
# In this game, computer will pick a random number then player would try to guess what number is it

from random import randint
'''
dodać opcje:
1. zabezpieczyć przed wpisaniem stringów
2. zabezpieczyć try except
'''

def computer_pick(range_num):
    return randint(0,range_num)
    

def user_range():
    return int(input('How hard game should be (pick highest number): '))
    
def main():
    print('----' *7)
    print('Welcome to the Guess The Number Game!')

    user_rng = user_range()
    comp = computer_pick(user_rng)
    

    while True:
        user = int(input(f'What number would you lick to pick in {user_rng} range: '))
        counter = 1
        if user == comp:
            print(f'Congratz you succed in {counter} moves!')
            break
        elif user > comp:
            counter +=1
            print('You picked too high number')
            
        else:
            counter +=1
            print('You picked to low number')
            

main()