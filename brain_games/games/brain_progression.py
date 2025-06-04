import random

from brain_games import engine


def round_generator():
    start = random.randint(1, 10)
    length = random.randint(5, 15)
    step = random.randint(1, 10)
    sequence = []
    for index in range(length):
        current_element = start + index * step
        sequence.append(current_element)
    correct_answer = random.choice(sequence)
    for index, element in enumerate(sequence):
        if element == correct_answer:
            sequence[index] = ".."
    question = ' '.join(map(str, sequence))
    return question, correct_answer
    

def main():
    rule = 'What number is missing in the progression?'
    engine.game_engine(rule, round_generator)


if __name__ == "__main__":    
    main()