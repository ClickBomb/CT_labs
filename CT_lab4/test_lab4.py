import random

import numpy as np

from CT_lab1.linear_code import LinearCode
from CT_lab4.functions import *


# 4.1 и 4.2
def test_lab4_part1():
    print(f"G_golay = \n{G_golay}\n")
    print(f"H_golay = \n{H_golay}\n")

    e_1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    e_2 = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    e_3 = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
    e_4 = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]

    code_words = LinearCode.get_all_code_words(len(G_golay), G_golay)

    v = code_words[random.randint(0, len(code_words) - 1)]
    v_with_error = (v + e_1) % 2
    err_pose = decode_word(v_with_error)
    v_without_error = (v_with_error + err_pose) % 2
    if np.array_equal(v, v_without_error):
        print("Обнаружена и исправлена 1-кратная ошибка")
    else:
        print("1-кратная ошибка не исправлена")

    v_with_error = (v + e_2) % 2
    err_pose = decode_word(v_with_error)
    v_without_error = (v_with_error + err_pose) % 2
    if np.array_equal(v, v_without_error):
        print("Обнаружена и исправлена 2-кратная ошибка")
    else:
        print("2-кратная ошибка не исправлена")

    v_with_error = (v + e_3) % 2
    err_pose = decode_word(v_with_error)
    v_without_error = (v_with_error + err_pose) % 2
    if np.array_equal(v, v_without_error):
        print("Обнаружена и исправлена 3-кратная ошибка")
    else:
        print("3-кратная ошибка не исправлена")

    v_with_error = (v + e_4) % 2
    err_pose = decode_word(v_with_error)
    if err_pose is not None:
        v_without_error = (v_with_error + err_pose) % 2
        if np.array_equal(v, v_without_error):
            print("Обнаружена и исправлена 4-кратная ошибка")
        else:
            print("4-кратная ошибка не исправлена")


# 4.3, 4.4, 4.5
def test_lab4_part2():
    r_m = [(0, 1), (1, 1), (0, 2), (1, 2), (2, 2), (0, 3), (1, 3), (1, 4)]
    for r, m in r_m:
        res = G(r, m)
        print(f"G({r}, {m}) =")
        for row in res:
            if isinstance(row, int):
                print(res)
                break
            print(row)
        print('\n')
    G_1_3 = G(1, 3)
    G_1_4 = G(1, 4)

    H_test = H(1, 3)
    for row in H_test:
        print(row)
