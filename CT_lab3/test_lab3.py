from CT_lab3.functions import *


def test_lab3_part_1(r):
    print("Код Хэмминга (обычный)")

    n = 2 ** r - 1
    k = 2 ** r - r - 1
    d = 3
    G, H = create_g_h_s(n, k, d)

    print(f"{r=}, {n=}, {k=}, {d=}\n")
    print(f"G=\n{G}\n")
    print(f"H=\n{H}\n")

    e_1 = all_e(1, len(H))
    e_2 = all_e(2, len(H))
    e_3 = all_e(3, len(H))

    code_words = LinearCode.get_all_code_words(k, G)

    v = code_words[random.randint(0, len(code_words) - 1)]

    test_seek_error(v, e_1, H)
    test_seek_error(v, e_2, H)
    test_seek_error(v, e_3, H)
    print('-'*30, '\n')


def test_lab3_part_2(r):
    print("Расширенный код Хэмминга)")

    n = 2 ** r - 1
    k = 2 ** r - r - 1
    d = 3
    G_star, H_star = create_g_h_s_expanded(n, k, d)

    print(f"{r=}, n={len(G_star[0])}, {k=}, {d=}\n")
    print(f"G*=\n{G_star}\n")
    print(f"H*=\n{H_star}\n")

    e_1 = all_e(1, len(H_star))
    e_2 = all_e(2, len(H_star))
    e_3 = all_e(3, len(H_star))

    code_words = LinearCode.get_all_code_words(k, G_star)

    v = code_words[random.randint(0, len(code_words) - 1)]

    e_1_and_2 = np.append(e_1, e_2, axis=0)
    test_seek_error(v, e_1_and_2, H_star)
    # test_seek_error(v, e_2 + e, H_star)
    test_seek_error(v, e_3, H_star)
    print('-' * 30, '\n')
