from CT_lab1.linear_code import LinearCode
from .functions import *
import numpy as np


def find_error_pos(v_syndrom, syndromes):
    pos = 0
    for s in syndromes:
        if np.array_equal(v_syndrom, s):
            return pos
        pos += 1


def test_lab2_part_1():
    X = np.array([
        [1, 1, 1],
        [1, 0, 1],
        [0, 1, 1],
        [1, 1, 0]
    ])

    n = len(X[0]) + len(X)
    k = len(X)
    G = np.array(create_g(len(X), X))
    d, t = LinearCode.find_min_d(G)
    for row in G:
        print(np.array(row))
    print('\n\n')
    H = create_h(n, k, X)
    for row in H:
        print(np.array(row))
    print('\n\n')

    # 2.4
    e = np.eye(n, n, dtype=int)  # список ошибок кратности 1
    syndromes = []
    for error in e:
        syndromes.append(np.matmul(error, H) % 2)
    for row in syndromes:
        print(np.array(row))
    print('\n\n')

    code_words = LinearCode.get_all_code_words(k, G)
    code_words = np.array([list(word) for word in code_words])
    v = code_words[0]
    v_p_e = (v + e[0]) % 2
    v_syndrom = np.matmul(v_p_e, H) % 2
    pos = find_error_pos(v_syndrom, syndromes)

    # исправление ошибки
    print(f"v = {v}")
    print(f"err = {e[0]}")
    v_p_e += e[pos]
    v_p_e %= 2
    print(f"v without err = {v_p_e}\n")

    # 2.5
    e = []  # список ошибок кратности 2
    max_i = 2 << (n - 1)
    for i in range(max_i):
        bin_word = LinearCode.int_to_bin_word_array(i, n)
        if sum(bin_word) == 2:
            e.append(bin_word)
    e = np.array(e)

    syndromes = np.matmul(e, H) % 2
    v = code_words[0]
    v_p_e = (v + e[0]) % 2
    v_syndrom = np.matmul(v_p_e, H) % 2
    pos = find_error_pos(v_syndrom, H)

    # исправление ошибки
    print(f"v = {v}")
    print(f"err = {e[0]}")
    print(f"v with err = {v_p_e}")
    v_p_e += e[pos]
    v_p_e %= 2
    print(f"v without err = {v_p_e}")


def test_lab2_part_2():
    n = 9
    k = 4

    # 2.6
    X = create_x(n, k)
    G = create_g(k, X)
    print("G = ")
    for row in G:
        print(np.array(row))
    print('\n\n')

    # 2.7
    H = create_h(n, k, X)
    print("H = ")
    for row in H:
        print(np.array(row))
    print('\n\n')

    # 2.8
    e_1 = np.eye(n, n, dtype=int)  # список ошибок кратности 1
    e_2 = []  # список ошибок кратности 2
    max_i = 2 << (n - 1)
    for i in range(max_i):
        bin_word = LinearCode.int_to_bin_word_array(i, n)
        if sum(bin_word) == 2:
            e_2.append(bin_word)
    e_2 = np.array(e_2)

    print(e_1)
    print('\n\n')
    print(e_2)
    print('\n\n')
    all_errors = np.concatenate((e_1, e_2), axis=0)
    syndromes = []
    for error in all_errors:
        syndromes.append(np.matmul(error, H) % 2)
    print("Syndromes = ")
    for row in syndromes:
        print(np.array(row))
    print('\n\n')

    code_words = LinearCode.get_all_code_words(k, G)
    code_words = np.array([list(word) for word in code_words])

    v = code_words[0]

    # 2.9
    err_1 = e_1[0]
    v_p_e_1 = (v + err_1) % 2
    v_syndrom_1 = np.matmul(v_p_e_1, H) % 2
    pos_e_1 = find_error_pos(v_syndrom_1, syndromes)

    # исправление ошибки кратности 1
    print(f"v = {v}")
    print(f"err = {err_1}")
    print(f"v + err = {v_p_e_1}")
    print(f"syndrom = {v_syndrom_1}")
    print(f"error pose = {pos_e_1}")
    v_wthout_e_1 = (v_p_e_1 + all_errors[pos_e_1]) % 2
    print(f"v without err = {v_wthout_e_1}\n")

    # 2.10
    err_2 = e_2[0]
    v_p_e_2 = (v + err_2) % 2
    v_syndrom_2 = np.matmul(v_p_e_2, H) % 2
    pos_e_2 = find_error_pos(v_syndrom_2, syndromes)

    # исправление ошибки кратности 2
    print(f"v = {v}")
    print(f"err = {err_2}")
    print(f"v + err = {v_p_e_2}")
    print(f"syndrom = {v_syndrom_2}")
    print(f"error pose = {pos_e_2}")
    v_wthout_e_2 = (v_p_e_2 + all_errors[pos_e_2]) % 2
    print(f"v without err = {v_wthout_e_2}\n")

    # 2.11
    err_3 = e_2[0]
    err_3[0] = 1
    if sum(err_3) != 3:
        print("error")
        exit(-1)

    v_p_e_3 = (v + err_3) % 2
    v_syndrom_3 = np.matmul(v_p_e_3, H) % 2
    pos_e_3 = find_error_pos(v_syndrom_3, syndromes)

    # попытка исправления ошибки кратности 3
    print(f"v = {v}")
    print(f"err = {err_3}")
    print(f"v + err = {v_p_e_3}")
    print(f"syndrom = {v_syndrom_3}")
    print(f"error pose = {pos_e_3}")
    v_wthout_e_3 = (v_p_e_3 + all_errors[pos_e_3]) % 2
    print(f"v without err = {v_wthout_e_3}\n")
