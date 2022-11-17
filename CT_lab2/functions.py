import numpy as np
from itertools import combinations
from CT_lab1.linear_code import LinearCode


def create_g(k, X):
    I_k = np.eye(k, k, dtype=int)
    G = []
    for row1, row2 in zip(I_k, X):
        row1 = list(row1)
        row2 = list(row2)
        G.append(row1 + row2)
    return np.array(G)


def create_h(n, k, X):
    I_n_k = np.eye(n - k, n - k, dtype=int)
    H = []
    for row in X:
        H.append(row)

    for row in I_n_k:
        H.append(row)

    return H


def create_x(n, k, d=5):
    if n - k < 4:
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
            if sum(sum(rows) % 2) < 3:
                continue
        rows_3 = combinations(matrix, 3)
        for rows in rows_3:
            if sum(sum(rows) % 2) < 2:
                continue
        rows_4 = combinations(matrix, 4)
        for rows in rows_4:
            if sum(sum(rows) % 2) < 1:
                continue
        return matrix
