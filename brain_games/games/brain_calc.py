import random

RULE = 'What is the result of the expression?'


def calculate_expression(number_1, operation, number_2):
    """
    Возвращает арифметическое выражение
    
    Аргументы:
    number_1: Первое случайно сгенерированное число
    number_2: Второе случайно сгенерированное число
    """
    match operation:
        case '+':
            return number_1 + number_2
        case '-':
            return number_1 - number_2
        case '*':
            return number_1 * number_2
        

def create_numbers(operation):
    """
    Возвращает два числа для создания арифметического выражения
    
    Аргументы:
    operation: случайно выбранный оператор
    """
    number_1 = random.randint(1, 100)
    match operation:
        case '+':
            # Если оператор +, то второе число может быть любым
            number_2 = random.randint(0, 100)
        case '-':
            # Если оператор -, то второе число не превышает первое, 
            # чтобы избежать отрицательного ответа
            number_2 = random.randint(0, number_1)
        case '*':
            # Если оператор *, то второе число не превышает 10, 
            # чтобы избежать слишком больших чисел
            number_2 = random.randint(0, 10)
    return number_1, number_2


def generate_round():
    """"
    Возвращает вопрос для вывода на экран и правильный ответ, 
    который должен назвать пользователь
    """
    operations = ['+', '-', '*']
    random_operation = random.choice(operations)
    number_1, number_2 = create_numbers(random_operation)
    correct_answer = calculate_expression(number_1, random_operation, number_2)
    question = f'{number_1} {random_operation} {number_2}'
    return question, correct_answer