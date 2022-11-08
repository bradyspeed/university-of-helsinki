# Write your solution here
def row_correct(sudoku: list):
    row_no = 0
    numbers = []
    while row_no < 9:
        for number in sudoku[row_no]:
            if number > 0 and number in numbers:
                #print(numbers)
                return False
            numbers.append(number)
        #print(numbers)
        numbers.clear()
        row_no += 1
    return True



def column_correct(sudoku: list):
    col_no = 0
    numbers = []
    while col_no < 9:
        for row in sudoku:
            number = row[col_no]
            if number > 0 and number in numbers:
                #print(numbers)
                return False
            numbers.append(number)
        #print(numbers)
        numbers.clear()
        col_no += 1
    return True



def block_correct(sudoku: list):
    block_matrix = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]
    numbers = []
    index = 0
    #row = block_matrix[index]
    while index < 9:
        row = block_matrix[index]
        row_no = row[0]
        column_no = row[1]
        for r in range(row_no, row_no+3):
            for s in range(column_no, column_no+3):
                number = sudoku[r][s]
                if number > 0 and number in numbers:
                    return False
                numbers.append(number)
        #print(numbers)
        numbers.clear()
        index += 1
    return True




def sudoku_grid_correct(sudoku: list):
    block_result = block_correct(sudoku)
    column_result = column_correct(sudoku)
    row_result = row_correct(sudoku)
    if block_result == True:
        if column_result == True:
            if row_result == True:
                return True
    return False

if __name__ == "__main__":
    sudoku = [
    [ 2, 6, 7, 8, 3, 9, 5, 0, 4 ],
    [ 9, 0, 3, 5, 1, 0, 6, 0, 0 ],
    [ 0, 5, 1, 6, 0, 0, 8, 3, 9 ],
    [ 5, 1, 9, 0, 4, 6, 3, 2, 8 ],
    [ 8, 0, 2, 1, 0, 5, 7, 0, 6 ],
    [ 6, 7, 4, 3, 2, 0, 0, 0, 5 ],
    [ 0, 0, 0, 4, 5, 7, 2, 6, 3 ],
    [ 3, 2, 0, 0, 8, 0, 0, 5, 7 ],
    [ 7, 4, 5, 0, 0, 3, 9, 0, 1 ],
    ]

    print(sudoku_grid_correct(sudoku))