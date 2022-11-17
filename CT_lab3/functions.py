from CT_lab1.linear_code import LinearCode
from CT_lab2.functions import *


def all_e(k, n):
    if k == 1:
        return np.eye(n, n, dtype=int)  # список ошибок кратности 1
    else:
        e = []  # список ошибок кратности 2
        max_i = 2 << (n - 1)
        for i in range(max_i):
            bin_word = LinearCode.int_to_bin_word_array(i, n)
            if sum(bin_word) == 2:
                e.append(bin_word)
        return np.array(e)


def create_g_h_s_1(r):
    n = 2 ** r - 1
    k = 2 ** r - r - 1
    d = 3

    X = None

    if n - k < d - 1:
        print("error")
        exit(-1)
    cols_num = n - k
    max_i = 2 << (cols_num - 1)

    words = []
    for i in range(max_i):
        bin_word = LinearCode.int_to_bin_word_array(i, cols_num)
        if sum(bin_word) >= d - 1:
            words.append(bin_word)
    words = np.array(words, dtype=int)

    matrixes = list(combinations(words, k))

    for matrix in matrixes:
        rows_2 = combinations(list(matrix), 2)
        for rows in rows_2:
            if sum(sum(rows) % 2) == 0:
                continue
        X = matrix
        break

    G = create_g(k, X)
    H = create_h(n, k, X)

    e_1 = all_e(1, n)
    syndromes = []
    for error in e_1:
        syndromes.append(np.matmul(error, H) % 2)

    return G, H, syndromes
