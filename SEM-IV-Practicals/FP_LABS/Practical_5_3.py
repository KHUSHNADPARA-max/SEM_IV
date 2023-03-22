def is_binary_matrix(matrix, rows, columns):
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] not in [0, 1]:
                return "NO", None
    return "YES", "Binary"

def is_identity_matrix(matrix, rows, columns):
    for i in range(rows):
        for j in range(columns):
            if i == j:
                if matrix[i][j] != 1:
                    return "NO", None
            else:
                if matrix[i][j] != 0:
                    return "NO", None
    return "YES", "Identity"

def main():
    dimensions = input("Enter the number of rows and columns of the matrix, separated by a space: ").split()
    if len(dimensions) != 2:
        print("Invalid input, please provide two integers separated by a space.")
        return
    try:
        n, m = int(dimensions[0]), int(dimensions[1])
    except ValueError:
        print("Invalid input, please provide two integers separated by a space.")
        return

    matrix = []
    for i in range(n):
        row = list(map(int, input("Enter the values for row {}: ".format(i+1)).split()))
        if len(row) != m:
            print("Invalid input, please provide a matrix with {} columns.".format(m))
            return
        matrix.append(row)

    binary_result, binary_type = is_binary_matrix(matrix, n, m)
    if binary_result == "NO":
        print("Matrix is not binary.")
        return

    identity_result, identity_type = is_identity_matrix(matrix, n, m)
    if identity_result == "NO":
        print("Matrix is binary but not identity.")
    else:
        print("Matrix is both binary and {}.".format(identity_type))

if __name__ == "__main__":
    main()
