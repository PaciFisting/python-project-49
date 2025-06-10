import random

from brain_games import engine


def calculate_progression_number(start, length, step):
    sequence = []
    for index in range(length):
        current_element = start + index * step
        sequence.append(current_element)
    correct_index = random.randint(0, length - 1)
    correct_answer = sequence[correct_index]
    sequence[correct_index] = '..'
    return sequence, correct_answer


def find_progression_number():
    start = random.randint(1, 10)
    length = random.randint(5, 15)
    step = random.randint(1, 10)
    sequence, correct_answer = calculate_progression_number(start, length, step)    
    question = ' '.join(map(str, sequence))
    return question, correct_answer