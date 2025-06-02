import random
from brain_games import engine


def round_generator():
    number_1 = random.randint(0, 100)
    operations = ['+', '-', '*']
    random_operation = random.choice(operations)
    match random_operation:
        case '+':
            number_2 = random.randint(0, 100)
            correct_answer = number_1 + number_2
        case '-':
            number_2 = random.randint(0, number_1)
            correct_answer = number_1 - number_2
        case '*':
            number_2 = random.randint(0, 10)
            correct_answer = number_1 * number_2
    question = f'{number_1} {random_operation} {number_2}'
    return question, correct_answer


def main():
    rules = 'What is the result of the expression?'
    engine.game_engine(rules, round_generator)