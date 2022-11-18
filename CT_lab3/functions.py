import random
from CT_lab2.functions import *
from CT_lab2.test_lab2 import find_error_pos


def all_e(k, n):
    if k == 1:
        return np.eye(n, n, dtype=int)  # список ошибок кратности 1
    else:
        e = []  # список ошибок кратности k > 1
        max_i = 2 << (n - 1)
        for i in range(max_i):
            bin_word = LinearCode.int_to_bin_word_array(i, n)
            if sum(bin_word) == k:
                e.append(bin_word)
        return np.array(e)


# 3.1
def create_g_h_s(n, k, d):
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

    matrices = list(combinations(words, k))

    for matrix in matrices:
        rows_2 = combinations(list(matrix), 2)
        for rows in rows_2:
            if sum(sum(rows) % 2) == 0:
                continue
        X = matrix
        break

    G = create_g(k, X)
    H = create_h(n, k, X)

    return np.array(G), np.array(H)


# 3.2
def test_seek_error(v, all_errors, H):
    Synd = []
    for error in all_errors:
        Synd.append(np.matmul(error, H) % 2)

    error = all_errors[0]
    v_p_e = (v + error) % 2
    syndrome_of_v_p_e = np.matmul(v_p_e, H) % 2
    error_position = find_error_pos(syndrome_of_v_p_e, Synd)
    if error_position == -1:
        print(f"Can't find syndrome={syndrome_of_v_p_e} for err={error}")
        return
    v_without_error = (v_p_e + all_errors[error_position]) % 2
    is_v_w_e_correct = np.array_equal(v, v_without_error)

    print(f"v = \n{v}")
    print(f"err = \n{error}")
    print(f"v + err = \n{v_p_e}")
    print(f"syndrome = \n{syndrome_of_v_p_e}")
    print(f"error positions = \n{all_errors[error_position]}")
    print(f"v without err = \n{v_without_error}")
    print(f"is it correct?: {is_v_w_e_correct}\n")

    error = all_errors[len(all_errors) - 1]
    v_p_e = (v + error) % 2
    syndrome_of_v_p_e = np.matmul(v_p_e, H) % 2
    error_position = find_error_pos(syndrome_of_v_p_e, Synd)
    if error_position == -1:
        print(f"Can't find syndrome={syndrome_of_v_p_e} for err={error}")
        return
    v_without_error = (v_p_e + all_errors[error_position]) % 2
    is_v_w_e_correct = np.array_equal(v, v_without_error)

    print(f"v = \n{v}")
    print(f"err = \n{error}")
    print(f"v + err = \n{v_p_e}")
    print(f"syndrome = \n{syndrome_of_v_p_e}")
    print(f"error positions = \n{all_errors[error_position]}")
    print(f"v without err = \n{v_without_error}")
    print(f"is it correct?: {is_v_w_e_correct}\n")


def create_g_h_s_expanded(n, k, d):
    G, H = create_g_h_s(n, k, d)
    H_star = []
    for i in range(len(H)):
        new_row = list(H[i])
        new_row.append(1)
        H_star.append(new_row)
    last_row = [0] * len(H[0])
    last_row.append(1)
    H_star.append(last_row)

    G_star = []
    for i in range(len(G)):
        new_row = list(G[i])
        new_row.append(sum(G[i]) % 2)
        G_star.append(new_row)

    return np.array(G_star), np.array(H_star)
