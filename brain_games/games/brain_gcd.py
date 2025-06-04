import random

from brain_games import engine


def round_generator():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    question = f'{number_1} {number_2}'
    while number_2 != 0:
        number_1, number_2 = number_2, number_1 % number_2
        if number_2 == 0:
            correct_answer = number_1
    return question, correct_answer


def main():
    rule = 'Find the greatest common divisor of given numbers.'
    engine.game_engine(rule, round_generator)


if __name__ == "__main__":    
    main()