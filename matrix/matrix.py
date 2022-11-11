# write your solution here
def matrix_sum():
    total = 0
    with open("matrix.txt") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(",")
            for i in parts:
                temp_num = int(i)
                total += temp_num
        return total

def matrix_max():
    largest = 0
    with open("matrix.txt") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(",")
            for i in parts:
                temp_num = int(i)
                if temp_num > largest:
                    largest = temp_num
        return largest

def row_sums():
    new_list = []
    with open("matrix.txt") as new_file:
        for line in new_file:
            row_total = 0
            line = line.replace("\n", "")
            parts = line.split(",")
            for i in parts:
                temp_num = int(i)
                row_total += temp_num
            new_list.append(row_total)
    return new_list



if __name__ == "__main__":
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())