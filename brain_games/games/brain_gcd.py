import random

RULE = 'Find the greatest common divisor of given numbers.'


def calculate_gcd(number_1, number_2):
    gcd = 1
    while number_2 != 0:
        number_1, number_2 = number_2, number_1 % number_2
        if number_2 == 0:
            gcd = number_1
    return gcd


def generate_round():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    question = f'{number_1} {number_2}'
    correct_answer = calculate_gcd(number_1, number_2)
    return question, correct_answer