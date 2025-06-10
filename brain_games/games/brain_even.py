import random

from brain_games import engine


def is_even(number):
    return number % 2 == 0


def is_it_even():
    question = random.randint(1, 100)
    if is_even(question) is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer