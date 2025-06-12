import random

RULE = 'Find the greatest common divisor of given numbers.'


def calculate_gcd(number_1, number_2):
    """
    Возвращает наибольший общий делитель двух чисел
    
    Аргументы:
    number_1: первое случайно сгенерированное число
    number_2: второе случайно сгенерированное число
    """
    gcd = 1
    while number_2 != 0:
        number_1, number_2 = number_2, number_1 % number_2
        if number_2 == 0:
            gcd = number_1
    return gcd


def generate_round():
    """"
    Возвращает вопрос для вывода на экран и правильный ответ, 
    который должен назвать пользователь
    """
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    question = f'{number_1} {number_2}'
    correct_answer = calculate_gcd(number_1, number_2)
    return question, correct_answer