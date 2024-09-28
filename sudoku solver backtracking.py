sudoku = [[0, 0, 7, 0, 0, 9, 0, 4, 5],
          [9, 3, 0, 7, 0, 8, 0, 6, 0],
          [6, 0, 0, 0, 5, 0, 0, 0, 7],
          [0, 0, 0, 0, 8, 0, 0, 7, 0],
          [0, 0, 0, 0, 0, 0, 0, 3, 0],
          [7, 2, 4, 0, 6, 3, 9, 1, 0],
          [0, 0, 0, 2, 0, 0, 0, 0, 6],
          [0, 6, 0, 9, 1, 0, 0, 0, 3],
          [1, 0, 3, 0, 0, 0, 0, 0, 0]]


def backtracking(sudoku):
    empty_field = next_empty_field(sudoku)
    
    if empty_field is None:
        # No empty fields left. The sudoku is solved.
        return True
    
    row, column = empty_field
    
    for number in range(1, 10): # Numbers from 1 to 9.
        if number_valid(sudoku, row, column, number):
            sudoku[row][column] = number
            
            solved = backtracking(sudoku)
            
            if solved:
                return True
            
            sudoku[row][column] = 0
    
    return False


def next_empty_field(sudoku):
    for row in range(9):
        for column in range(9):
            if sudoku[row][column] == 0:
                return (row, column)
    return None


def number_valid(sudoku, row, column, number):
    # Check row for duplicates
    for i in range(9):
        if sudoku[row][i] == number:
            return False
        
    # Check column for duplicates
    for i in range(9):
        if sudoku[i][column] == number:
            return False
        
    # Check box for duplicates
    box_start_row = (row // 3) * 3
    box_start_column = (column // 3) * 3
    for i in range(3):
        for j in range(3):
            if sudoku[box_start_row + i][box_start_column + j] == number:
                return False
    
    return True


def print_sudoku(sudoku):
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print("-" * 21)
            
        for column in range(9):
            if column % 3 == 0 and column != 0:
                print("|", end=" ")
                
            print(sudoku[row][column], end=" ")
            
        print()
        
    print()


backtracking(sudoku)
print_sudoku(sudoku)