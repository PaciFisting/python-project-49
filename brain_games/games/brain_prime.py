import random

from brain_games.scripts import engine


def is_prime(number):
    dividers = 0
    for i in range(2, number):
        if number % i == 0:
            dividers += 1
    return dividers == 0

def is_it_prime():
    question = random.randint(2, 100)
    if is_prime(question) is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer


def main():
    RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    engine.game_engine(RULE, is_it_prime)


if __name__ == "__main__":    
    main()