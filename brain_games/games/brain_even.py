import random
import brain_games.engine


def main():
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    question = random.randint(0, 100)
    if question % 2 == 0:
        correct_answer  = 'yes'
    else:
        correct_answer = 'no'
    brain_games.engine.game_engine(rules, correct_answer, question)