import random
from brain_games import engine

def round_generator():
    question = random.randint(0, 100)
    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer


def main():
    rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    engine.game_engine(rule, round_generator)