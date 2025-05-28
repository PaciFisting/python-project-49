import random
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_anwers = 0
    for round in range(0,3):
        number = random.randint(1, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if number % 2 == 0: 
            if answer.lower() == 'yes':
                print('Correct!')
                correct_anwers += 1
            else: 
                print (f'{answer} is wrong answer ;(. Correct answer was "yes".\nLet\'s try again, {name}!')
                break
        if number % 2 != 0: 
            if answer.lower() == 'no':
                print('Correct!')
                correct_anwers += 1
            else: 
                print (f'{answer} is wrong answer ;(. Correct answer was "no".\nLet\'s try again, {name}!')
                break
    if correct_anwers == 3:
        print(f'Congratulations, {name}!')