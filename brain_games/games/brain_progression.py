import random

RULE = 'What number is missing in the progression?'


def create_progression(start, length, step):
    sequence = []
    for index in range(length):
        current_element = start + index * step
        sequence.append(current_element)
    return sequence


def generate_round():
    start = random.randint(1, 10)
    length = random.randint(5, 15)
    step = random.randint(1, 10)
    correct_index = random.randint(0, length - 1)
    sequence = create_progression(start, length, step)
    correct_answer = sequence[correct_index]
    sequence[correct_index] = '..'    
    question = ' '.join(map(str, sequence))
    return question, correct_answer