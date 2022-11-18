import random

import numpy as np

from CT_lab1.linear_code import LinearCode
from CT_lab3.functions import all_e, test_seek_error
from CT_lab4.functions import *


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


def test_lab4_part2():
    r = 1
    m = 3
    res = G(r, m)

    norm_matrix = []

    def refactor_matrix(matrix):
        for block in matrix:
            if isinstance(block, list) and isinstance(block[0], list):
                refactor_matrix(block)
            else:
                norm_matrix.append(block)
    refactor_matrix(res)
    print(norm_matrix)
