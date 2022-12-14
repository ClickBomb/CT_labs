import random
from CT_lab1.linear_code import LinearCode

import numpy as np

B = np.array([
    [1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1],
    [0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1],
    [0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1],
    [0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1],
    [0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
], dtype=int)

I = np.eye(len(B), dtype=int)

G_golay = []

for row_i, row_b in zip(I, B):
    G_golay.append((list(row_i) + list(row_b)))

H_golay = []
for row in I:
    H_golay.append(row)
for row in B:
    H_golay.append(row)

np.array(G_golay, dtype=int)
np.array(H_golay, dtype=int)


def decode_word(w):
    s = np.matmul(w, H_golay) % 2
    if sum(s) <= 3:
        return list(s) + [0] * (len(w) - len(s))

    for i in range(len(B)):
        val = (s + B[i]) % 2
        if sum(val) <= 2:
            return list(val) + list(I[i])

    sB = np.matmul(s, B) % 2
    if sum(sB) <= 3:
        u = [0] * (len(w) - len(sB))
        u + list(sB)
        return u

    for i in range(len(B)):
        val = (sB + B[i]) % 2
        if sum(val) <= 2:
            return list(I[i]) + list(val)

    print("Can't recognize error")


# функция для приведения всех вложенных массивов к одному уровню: [[[1, 1], [1, 1]], [1, 1]] -> [[1, 1], [1, 1], [1, 1]]
# это чтобы хранить все матрицы построчно
def fill_array(arr: list):
    filled_array = []

    def fill(matrix):
        for block in matrix:
            if isinstance(block, list) and isinstance(block[0], list):
                fill(block)
            else:
                filled_array.append(block)

    fill(arr)
    return filled_array


# функция формирования порождающей матрицы кода Рида-Маллера
def G(r, m):
    to_return = None
    if 0 < r < m:
        block_1 = G(r, m - 1)
        block_2 = G(r - 1, m - 1)
        zero_block = [0] * (2 ** m - len(block_2))
        up_block = []
        for block_row in block_1:
            up_block.append(block_row + block_row)

        to_return = [
            up_block,
            zero_block + block_2
        ]
    if r == 0:
        to_return = [1] * (2 ** m)
    if r == m:
        row = [0] * 2 ** m
        row[len(row) - 1] = 1

        to_return = [G(m - 1, m), row]
    to_return = fill_array(to_return)
    return to_return


def Kronker_mul(A, B):
    B = np.array(B, dtype=int)
    res = []
    for row in A:
        new_row = []
        for elem in row:
            if not isinstance(elem, list):
                val = np.multiply(elem, B)
                new_row.append(val)
        for i in range(len(new_row[0])):
            temp = []
            for j in range(len(new_row)):
                if i >= len(new_row[j]):
                    continue
                temp += list(new_row[j][i])
            res.append(temp)
    return res

# функция формирования проверочной матрицы кода Рида-Маллера
def H(i, m):
    H = [[1, 1], [1, -1]]
    I_test = [[1, 0], [0, 1]]
    first_I = np.eye(2 ** (m - i), dtype=int)
    second_I = np.eye(2 ** (i - 1), dtype=int)

    # test_mul = Kronker_mul(I_test, H)
    # print(f"H_test =")
    # for row in test_mul:
    #     print(row)
    # print('\n')

    res = Kronker_mul(first_I, H)
    res = Kronker_mul(res, second_I)
    return res


def fast_decode_algorithm(m, w):
    w_hat = [-1 if elem == 0 else elem for elem in w]

    w_1 = np.matmul(np.array(w_hat, dtype=int), np.array(H(1, m), dtype=int))
    w_i = [w_1]
    for i in range(2, m + 1):
        w_i.append(np.matmul(w_i[i - 2], np.array(H(i, m), dtype=int)))

    max_elem = max(w_i[m - 1], key=abs)
    j = list(w_i[m - 1]).index(max_elem)
    bin_j = LinearCode.int_to_bin_word_array(j, m)
    bin_j.reverse()

    if max_elem >= 0:
        v = [1] + bin_j
    else:
        v = [0] + bin_j
    return np.array(v)
