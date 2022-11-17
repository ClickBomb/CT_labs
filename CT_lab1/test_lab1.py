import numpy as np
from CT_lab1.linear_code import LinearCode


def test_lab1():
    S = [
        [1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1],
        [0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
        [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0]
    ]
    S = np.array(S, dtype=int)
    S_ref = LinearCode.REF(S)
    print(f"S_ref = \n{S_ref}\n\n")
    n, k, G = LinearCode.get_n_k(S_ref)
    print(f"G = \n{G}\n{n=}, {k=}\n\n")
    G_rref = LinearCode.RREF(G)
    print(f"G_rref = \n{G_rref}\n")
    lead = LinearCode.get_lead_columns(G_rref)
    print(f"lead = {lead}\n\n")
    X = LinearCode.compress(lead, G_rref)
    print(f"X = \n{X}\n\n")
    H = LinearCode.append_i(X, lead)
    print(f"H = \n{H}\n\n")

    # 1.4.2 (cложить все слова из порождающего множества, оставить неповторяющиеся)
    code_words = LinearCode.get_all_code_words(k, G)
    code_words = np.array([list(word) for word in code_words])
    print("Checking code words...")
    for word in code_words:
        res = np.matmul(word, H) % 2
        if sum(res) > 0:
            print(f"Illegal code word = {word}, res = {res}")
            break
    print("Checking done!\n")

    d, t = LinearCode.find_min_d(G)
    print(f"{d=}, {t=}\n\n")

    v = code_words[0]
    LinearCode.show_error(v, t, H)
    err = LinearCode.find_error(v, t, H)
    print("\nНеобнаруживаемая ошибка:")
    print(f"v = {v}")
    print(f"e = {err}")
    v_p_err = (v + err) % 2
    print(f"v + e = {v_p_err}")
    print(f"(v + e) * H = {np.matmul(v_p_err, H) % 2}")
