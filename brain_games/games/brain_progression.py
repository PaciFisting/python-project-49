import random

from brain_games.scripts import engine


def find_progression_number():
    start = random.randint(1, 10)
    length = random.randint(5, 15)
    step = random.randint(1, 10)
    sequence = []
    for index in range(length):
        current_element = start + index * step
        sequence.append(current_element)
    correct_index = random.randint(0, length - 1)
    correct_answer = sequence[correct_index]
    sequence[correct_index] = '..'
    question = ' '.join(map(str, sequence))
    return question, correct_answer
    

def main():
    RULE = 'What number is missing in the progression?'
    engine.game_engine(RULE, find_progression_number)


if __name__ == "__main__":    
    main()