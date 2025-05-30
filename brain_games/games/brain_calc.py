import random
import brain_games.engine


def main():
    rules = 'What is the result of the expression?'
    operations = ['+', '-', '*']
    for i in range(0,3):
        number_1 = random.randint(1, 100)
        random_operation = random.choice(operations)
        match random_operation:
            case '+':
                number_2 = random.randint(1, 100)
                correct_answer = number_1 + number_2
            case '-':
                number_2 = random.randint(1, number_1)
                correct_answer = number_1 - number_2
            case '*':
                number_2 = random.randint(1, 10)
                correct_answer = number_1 * number_2
        equasion = f'Question: {number_1} {random_operation} {number_2}'
    brain_games.engine.game_engine(rules, correct_answer, equasion)