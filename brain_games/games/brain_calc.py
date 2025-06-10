import random

from brain_games import engine


def calculate_expression(number_1, operation, number_2):
    match operation:
        case '+':
            return number_1 + number_2
        case '-':
            return number_1 - number_2
        case '*':
            return number_1 * number_2


def calculate():
    number_1 = random.randint(0, 100)
    operations = ['+', '-', '*']
    random_operation = random.choice(operations)
    match random_operation:
        case '+':
            number_2 = random.randint(0, 100)
        case '-':
            number_2 = random.randint(0, number_1)
        case '*':
            number_2 = random.randint(0, 10)
    correct_answer = calculate_expression(number_1, random_operation, number_2)
    question = f'{number_1} {random_operation} {number_2}'
    return question, correct_answer