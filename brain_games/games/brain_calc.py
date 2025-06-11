import random

RULE = 'What is the result of the expression?'


def calculate_expression(number_1, operation, number_2):
    match operation:
        case '+':
            return number_1 + number_2
        case '-':
            return number_1 - number_2
        case '*':
            return number_1 * number_2
        

def create_numbers(operation):
    number_1 = random.randint(1, 100)
    match operation:
        case '+':
            number_2 = random.randint(0, 100)
        case '-':
            number_2 = random.randint(0, number_1)
        case '*':
            number_2 = random.randint(0, 10)
    return number_1, number_2


def generate_round():
    operations = ['+', '-', '*']
    random_operation = random.choice(operations)
    number_1, number_2 = create_numbers(random_operation)
    correct_answer = calculate_expression(number_1, random_operation, number_2)
    question = f'{number_1} {random_operation} {number_2}'
    return question, correct_answer