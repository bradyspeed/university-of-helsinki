# Write your solution here
def transpose(matrix: list):
    transpose = [[matrix[i][j]
    for i in range(len(matrix))]
        for j in range(len(matrix[0]))]
    print(transpose)
    matrix = transpose[:]


if __name__ == "__main__":
    m = [[1, 2], [1, 2]]
    print(transpose(m))