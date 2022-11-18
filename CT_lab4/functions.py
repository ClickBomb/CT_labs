import random

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


def G(r, m):
    if 0 < r < m:
        block_1 = G(r, m - 1)
        block_2 = G(r - 1, m - 1)
        zero_block = [0] * (len(block_1[0]) * 2 - len(block_2))
        up_block = []
        for row in block_1:
            up_block.append(row + row)

        return [
            up_block,
            [zero_block + block_2]
        ]
    if r == 0:
        return [1] * 2 ** m
    if r == m:
        row = [0] * 2 ** m
        row[len(row) - 1] = 1
        return [G(m - 1, m), row]
