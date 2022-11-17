from .functions import *


def test_lab3():
    r = 2
    G, H, syndromes = create_g_h_s_1(r)
    print(list(G), "\n\n")
    print(list(H), "\n\n")
    print(list(syndromes), "\n\n")

    e_1 = all_e(1, len(H))
    e_2 = all_e(2, len(H))
