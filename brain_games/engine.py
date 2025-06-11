import prompt

RULE = 'Find the greatest common divisor of given numbers.'


def game_engine(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULE)

    correct_answers = 0

    for round in range(0, 3):
        question, correct_answer = game.generate_round()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer.lower() == str(correct_answer):
            print('Correct!')
            correct_answers += 1
        else:
            print(f'{user_answer} is wrong answer ;(.', end=' ')
            print(f'Correct answer was "{correct_answer}".')
            print(f"Let\'s try again, {name}!")
            break
    
    if correct_answers == 3:
        print(f'Congratulations, {name}!')