import numpy as np


def ref(matrix):
    m = np.array(matrix)
    if len(m) == 0:
        print("ERROR, matrix size are 0")
        exit(-1)

    main_rows_ids = []
    for j in range(len(m[0])):
        if len(main_rows_ids) == len(m):
            break
        main_row_id = 0
        for i in range(len(m)):
            if i in main_rows_ids:
                continue
            if m[i][j]:
                main_row_id = i
                break

        if main_row_id not in main_rows_ids:
            main_rows_ids.append(main_row_id)

            for i in range(len(m)):
                if i in main_rows_ids:
                    continue
                if m[i][j]:
                    m[i] = (m[main_row_id] + m[i]) % 2

    result = []
    for i in main_rows_ids:
        result.append(m[i])

    for i in range(len(m)):
        if i not in main_rows_ids:
            result.append(m[i])

    return np.array(result, dtype=int)


def rref(matrix):
    m = matrix.copy()
    main_rows_ids = []
    for j in range(len(m[0])):
        if len(main_rows_ids) == len(m):
            break

        main_row_id = 0
        for i in range(len(m)):
            if i in main_rows_ids:
                continue
            if m[i][j]:
                main_row_id = i
                break

        if main_row_id not in main_rows_ids:
            main_rows_ids.append(main_row_id)

            for i in range(len(m)):
                if i == main_row_id:
                    continue
                if m[i][j]:
                    m[i] = (m[main_row_id] + m[i]) % 2

    result = []
    for i in main_rows_ids:
        result.append(m[i])
    for i in range(len(m)):
        if i not in main_rows_ids:
            result.append(m[i])

    return np.array(result, dtype=int)
