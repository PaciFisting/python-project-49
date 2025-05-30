import prompt

def game_engine(rules, correct_answer, question):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(rules)

    correct_answers = 0
    operations = ['+', '-', '*']

    for round in range(0,3):
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == str(correct_answer):
            print ('Correct!')
            correct_answers += 1
        else:
            print ((f'{user_answer} is wrong answer ;(. Correct answer was "{correct_answer}".\nLet\'s try again, {name}!'))
            break
    
    if correct_answers == 3:
        print(f'Congratulations, {name}!')