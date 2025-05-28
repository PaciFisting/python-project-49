import random
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('What is the result of the expression?')
    correct_answers = 0
    operations = ['+', '-', '*']
    for round in range(0,3):
        number_1 = random.randint(0, 100)
        random_operation = random.choice(operations)
        if random_operation == '+':
            number_2 = random.randint(0, 100)
            right_answer = number_1 + number_2
        if random_operation == '-':
            number_2 = random.randint(0, number_1)
            right_answer = number_1 - number_2
        if random_operation == '*':
            number_2 = random.randint(0, 10)
            right_answer = number_1 * number_2
        print(f'Question: {number_1} {random_operation} {number_2}')
        answer = prompt.string('Your answer: ')

        if answer == str(right_answer):
            print('Correct!')
            correct_answers += 1
        else:
            print(f'{answer} is wrong answer ;(. Correct answer was {right_answer}.\nLet\'s try again, {name}!')
            break
    if correct_answers == 3:
        print(f'Congratulations, {name}!') 