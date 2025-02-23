def input_matrix(label):
    """
    Accept matrix elements from user.
    Return tuple (rows, cols, matrix).
    """
    while True:
        try:
            print(f"Input dimensions  with space for {label} matrix (rows cols) (el+space+el...+ENTER:):")
            rows, cols = map(int, input().split())

            if rows <= 0 or cols <= 0:
                raise ValueError("Matrix dimensions must be positive integers.")

            print(f"Enter {rows} rows with {cols} element (el+space+el...+ENTER:)")
            matrix = []
            for _ in range(rows):
                while True:
                    try:
                        row = list(map(float, input().split()))
                        if len(row) != cols:
                            raise ValueError(f"Each row must contain exactly {cols} numbers.")
                        matrix.append(row)
                        break
                    except ValueError as e:
                        print(f"Invalid row: {e}. Try again.")  # Ввод повторяем, если кол-во эл не совпадает
            return rows, cols, matrix

        except ValueError as e:
            print(f"Invalid input: {e}. Try again.\n")


def matrix_addition():
    """
    Read two matrix, check sizes
    Prints result or an error message
    """
    r1, c1, mat1 = input_matrix("first")
    r2, c2, mat2 = input_matrix("second")

    if (r1, c1) != (r2, c2):
        print("Matrix addition not possible.")  # cлож невозможно, размеры разные
        return

    result = [[mat1[i][j] + mat2[i][j] for j in range(c1)] for i in range(r1)]  # склад элементы по инд.

    print("Result matrix:")
    for row in result:
        print(*row)


def const_multiplication():
    """
    Read matrix and a const, multipl his element.
    Print result.
    """
    r, c, mat = input_matrix("target")

    while True:
        try:
            const = float(input("Enter const value: "))  # просим  число (конст)
            break
        except ValueError:
            print("Invalid input! Enter a number.")  # ошибка, если не число

    result = [[mat[i][j] * const for j in range(c)] for i in range(r)]  # кажд элт матр умн на число

    print("Result matrix:")
    for row in result:
        print(*row)


def matrix_multiplication():
    """
    Read two matrix and multipl if posible
    Print result or  error message
    """
    r1, c1, mat1 = input_matrix("first")
    r2, c2, mat2 = input_matrix("second")

    if c1 != r2:
        print("Matrix multiplication not posible")  # умнож невозможно,  колво столб 1-й не = стр 2-й
        return

    result = [[sum(mat1[i][k] * mat2[k][j] for k in range(c1)) for j in range(c2)] for i in range(r1)]  # умн строк на столбцы

    print("Resultt matrix:")
    for row in result:
        print(*row)


def trans_matrix():
    """
    Read matrix and allows user to choose transpos metod
    Print the trans matrix
    """
    r, c, mat = input_matrix("original")

    print("Select transpose method:")
    print("1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")

    while True:
        option = input("> ").strip()
        if option in {"1", "2", "3", "4"}:
            break
        print("Invalid choice. Enter 1, 2, 3, or 4.")  # ош,  несущ вар

    if option == "1":
        result = [[mat[j][i] for j in range(r)] for i in range(c)]  # транспон  главндиаг
    elif option == "2":
        result = [[mat[r - 1 - j][c - 1 - i] for j in range(r)] for i in range(c)]  # транс отн побочдиаг
    elif option == "3":
        result = [row[::-1] for row in mat]  # зеркальное отраж относ верт
    elif option == "4":
        result = mat[::-1]  # зеркал отраж гориз-ли

    print("Transposed matrix:")
    for row in result:
        print(*row)


def determinant_recursive(matrix):
    """
    Recursiv determinant square matrix.
    """
    size = len(matrix)
    if size == 1:
        return matrix[0][0]  # опрль 1×1 = самому элементу
    if size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]  # формула 2×2

    det = 0
    for col in range(size):
        pod_matrix = [row[:col] + row[col + 1:] for row in matrix[1:]]  # берем рядки с индекса 1 и до конца (минор)
        det += (-1) ** col * matrix[0][col] * determinant_recursive(pod_matrix)  # разложение по первой строке
    return det


def calc_determinant():
    """
    Read square matrix calc determinant
    """
    r, c, mat = input_matrix("target")

    if r != c:
        print("Determinant can only calc for square matrix")  # опред. можн считать только для кв матр
        return

    print("Determinant:", determinant_recursive(mat))


def invert_matrix():
    """
    Read square matrix inverse if determinant not 0
    """
    r, c, mat = input_matrix("target")

    if r != c:
        print("Inverse matrix only for square matrix")  # обрат матр сущ только для кв.
        return

    det = determinant_recursive(mat)
    if det == 0:
        print("Matrix has no inverse")  # матрица не обратима, если ее опр= 0
        return

    cofactors = []
    for i in range(r):
        cofactor_row = []
        for j in range(c):
            minor = [mat[x][:j] + mat[x][j + 1:] for x in range(r) if x != i]  # создаем минор
            cofactor_row.append(((-1) ** (i + j)) * determinant_recursive(minor))  # ыыч алг доп.
        cofactors.append(cofactor_row)

    adjugate = [[cofactors[j][i] for j in range(r)] for i in range(c)]  # транс матрицы дополнений
    inverse = [[adjugate[i][j] / det for j in range(c)] for i in range(r)]  # деление эл на определитель

    print("Inverse matrix:")
    for row in inverse:
        print(*map(lambda x: f"{x:.2f}", row))  # окр до 2з зн


def main():
    """
    Main menu matrix operations.
    """
    while True:
        print("\nMatrix Operations:")
        print("1. Add matrix")
        print("2. Multiply matrix and const")
        print("3. Multiply matrix")
        print("4. Transpose matrix")
        print("5. Calculate determinant")
        print("6. Inverse matrix")
        print("0. Exit")

        option = input("> ").strip()

        if option == "1":
            matrix_addition()
        elif option == "2":
            const_multiplication()
        elif option == "3":
            matrix_multiplication()
        elif option == "4":
            trans_matrix()
        elif option == "5":
            calc_determinant()
        elif option == "6":
            invert_matrix()
        elif option == "0":
            print("Exit!")
            break
        else:
            print("Invalid choice, try again")


if __name__ == "__main__":
    main()
