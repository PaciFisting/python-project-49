import random

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    """
    Возвращает проверку простоты числа
    
    Аргументы:
    number: случайно сгенерированное число
    """
    dividers = 0
    for i in range(2, number):
        if number % i == 0:
            dividers += 1
    return dividers == 0


def generate_round():
    """"
    Возвращает вопрос для вывода на экран и правильный ответ, 
    который должен назвать пользователь
    """
    question = random.randint(2, 100)
    correct_answer = 'yes' if is_prime(question) is True else 'no'
    return question, correct_answer