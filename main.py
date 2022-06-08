# import library
import random
from time import sleep


# Ask how many people will participate on the game.


def people_will_enjoy():
    try:
        print('-=' * 20)
        how_many = int(input('How many people will play it? \nmin 4 people and max 10 people: '))
        check(how_many)
        #users_name(how_many)
        who_will_pay(users_name(how_many))
    except ValueError:
        print('-=' * 20)
        print('Sorry but what you typed is not acceptable, try again. ')
        sleep(1)
        people_will_enjoy()
        return


# Check if the total of players is accept.

def check(total):
    if total == 0:
        finish()
    while total < 4 or total > 10:
        print('-=' * 20)
        print('Invalid option, TRY AGAIN...')
        people_will_enjoy()
        break


# Get names of the players.

def users_name(name):
    people_names = []

    while True:
        print('-=' * 10)
        people = input('Name: ')

        if not people.isalpha():
            print("Sorry should be a letter, this was not save.\nTry again...")
            sleep(1)
        else:
            people_names.append(people)

        if len(people_names) == name:

            return people_names


# Random the names of the players and show who will pay.

def who_will_pay(name):
    print('-=' * 20)
    choice = random.choice(name)
    print('Who will pay is: ', end='')
    sleep(1)
    print(f'{choice}'.title())
    question()
    return


# Check if the player will play again.

def question():
   pass


# Finish the game.

def finish():
  pass


people_will_enjoy()
