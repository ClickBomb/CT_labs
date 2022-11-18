import numpy as np
from CT_lab1.functions import ref, rref


class LinearCode:
    # 1.3.1 (формируем порождающую матрицу в ступенчатом виде S_ref на основе входной матрицы S)
    @staticmethod
    def REF(S):
        return ref(S)

    # 1.3.2
    @staticmethod
    def get_n_k(S_ref):
        G = []
        for row in S_ref:
            if np.sum(row) > 0:
                G.append(row)

        k = len(G)
        n = len(G[0])

        return n, k, np.array(G, dtype=int)

    # 1.3.3, step №1 (приводим матрицу G к ступенчатому виду -> G_rref)
    @staticmethod
    def RREF(G):
        return rref(G)

    # 1.3.3, step №2 (фиксируем ведущие столбцы lead матрицы G_rref)
    @staticmethod
    def get_lead_columns(G_rref):
        lead = []
        for row in G_rref:
            for j in range(len(row)):
                if row[j] > 0:
                    lead.append(j)
                    break
        return lead

    # 1.3.3, step №3 (удаляем ведущие столбцы из матрицы G_rref)
    @staticmethod
    def compress(lead, G_rref):
        X = []
        for row in G_rref:
            new_row = []
            for j in range(len(row)):
                if j not in lead:
                    new_row.append(row[j])
            X.append(new_row)

        X = np.array(X, dtype=int)
        return X

    # 1.3.3, step №4 (формируем матрицу H)
    @staticmethod
    def append_i(X, lead):
        E = np.eye(len(X[0]))  # типо единичная матрица

        n = len(E) + len(X)
        H = []
        E_counter = 0
        X_counter = 0
        for i in range(n):
            if i in lead:
                H.append(X[X_counter])
                X_counter += 1
            else:
                H.append(E[E_counter])
                E_counter += 1

        return np.array(H, dtype=int)

    @staticmethod
    def int_to_bin_word_array(i: int, k: int):
        bin_str = format(i, 'b')
        n = k - len(bin_str)
        if n > 0:
            bin_str = ''.zfill(n) + bin_str
        return [int(digit_char) for digit_char in bin_str]

    # 1.4.1 (skip)
    # 1.4.2 (взять все двоичные слова длины k, умножить каждое на G)
    @staticmethod
    def get_all_code_words(k, G):
        G = np.array(G, dtype=int)
        if k != G.shape[0]:
            print("ERROR")
            exit(-1)

        max_i = 2 << (k - 1)

        words = []
        for i in range(max_i):
            words.append(LinearCode.int_to_bin_word_array(i, k))
        words = np.array(words, dtype=int)

        code_words = []
        for word in words:
            res = np.matmul(word, G) % 2
            code_words.append(res)

        code_words = set(tuple(code_word) for code_word in code_words)  # убираю повторяющиеся слова
        return np.array([list(word) for word in code_words])

    # 1.5.1
    @staticmethod
    def find_min_d(code_words):
        size = len(code_words[0])
        d = len(code_words[0])
        for i in range(len(code_words)):
            for j in range(i + 1, len(code_words)):
                same = 0
                for a, b in zip(code_words[i], code_words[j]):
                    if a == b:
                        same += 1  # считаю количество повторяющихся элементов
                d_curr_min = size - same  # расстояние Хэмминга между i и j кодовым словом
                if d_curr_min < d:
                    d = d_curr_min

        return d, d-1

    @staticmethod
    def show_error(code_word, t, H):
        print(f"v = {code_word}")
        e = []  # список ошибок кратности t + 1
        k = len(code_word)
        max_i = 2 << (k - 1)
        for i in range(max_i):
            bin_word = LinearCode.int_to_bin_word_array(i, k)
            if sum(bin_word) == t:
                e.append(bin_word)
        e = np.array(e)
        for err in e:
            v_p_err = (code_word + err) % 2
            print(f"err = {err}")
            print(f"v + err = {v_p_err}")
            print(f"(v + e) * H = {np.matmul(v_p_err, H) % 2}\n")

    # 1.5.2
    @staticmethod
    def find_error(code_word, t, H):
        e = []  # список ошибок кратности t + 1
        k = len(code_word)
        max_i = 2 << (k - 1)
        for i in range(max_i):
            bin_word = LinearCode.int_to_bin_word_array(i, k)
            if sum(bin_word) == t + 1:
                e.append(bin_word)
        e = np.array(e)

        for err in e:
            v_p_err = (code_word + err) % 2
            if sum(np.matmul(v_p_err, H) % 2) == 0:
                return err
        return code_word
