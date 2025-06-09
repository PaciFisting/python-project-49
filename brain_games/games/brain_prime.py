import random

from brain_games.scripts import engine


def round_generator():
    question = random.randint(2, 100)
    dividers = 0
    for number in range(2, question):
        if question % number == 0:
            dividers += 1
    if dividers == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer


def main():
    rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    engine.game_engine(rule, round_generator)


if __name__ == "__main__":    
    main()