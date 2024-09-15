import numpy as np

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    
    
def game_core_v3(number: int = 1) -> int:
    """Функция угадывания числа
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    start = 1
    finish = 101
    predict = 0
    
    # Составим условие нахождения числа на подобие метода дихотомии
    while number != predict:
        count += 1
        predict = np.random.randint(start, finish)        
        if predict > number:
            finish = predict
        else:
            start = predict

    return count

print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)