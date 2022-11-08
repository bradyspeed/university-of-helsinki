# Write your solution here
def count_matching_elements(my_matrix: list, element: int):
    count = 0
    for row in my_matrix:
        for item in row:
            if item == element:
                count += 1
    return count



if __name__ == "__main__":
    m = [[1, 2, 3], [2, 3, 1], [4, 5, 6]]
    print(count_matching_elements(m, 2))