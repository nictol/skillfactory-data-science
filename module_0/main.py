# coding=utf-8
import numpy as np

from module_0.constant import AMOUNT_OF_GAMES, MIN_SECRET_NUMBER, MAX_SECRET_NUMBER


def game_core(secret_number):
    predict_number = int((MAX_SECRET_NUMBER + MIN_SECRET_NUMBER) / 2)
    left = MIN_SECRET_NUMBER
    right = MAX_SECRET_NUMBER
    amount_of_attempts = 1

    while secret_number != predict_number:
        if secret_number > predict_number:
            left = predict_number + 1
        else:
            right = predict_number - 1
        predict_number = int((left + right) / 2)
        amount_of_attempts += 1

    return amount_of_attempts


def score_game():
    attempts_result = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    secret_numbers = np.random.randint(MIN_SECRET_NUMBER, MAX_SECRET_NUMBER + 1, size=AMOUNT_OF_GAMES)
    for number in secret_numbers:
        attempts_result.append(game_core(number))
    average_attempts = int(np.mean(attempts_result))
    print(f"Ваш алгоритм угадывает число в среднем за {average_attempts} попыток")
    return average_attempts


if __name__ == '__main__':
    score_game()
