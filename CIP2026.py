import random
import ctime
from graphics import Canvas

def main():
    pass
   
def create_empty_grid():
    return [[0] * 9 for i in range(9)]
    
def isValid(grid, row, col, num):
    #This will check if ever the number if alreday there in the row
    if num in grid[row]:
        return False
    #This will check if the number is already there in that column
    if num in grid[col]:
        return False
        
    #creating the box frame that will be use by the graphics method in creating the squre
    box_row = 3 * (row // 3)
    box_col = 3 * (col // 3)
    
    #now loop throw the rows and columns 
    for r in range(box_row, box_row + 3):
        for c in range(box_col, box_col + 3):
            if grid[r][c] == num:
                return False
    #Otherwise you are able to place the number there
    return True
 
def solve(grid, randomize=False):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                numbers = list(range(1, 10))
                if randomize:
                    random.shuffle(numbers)
                for num in numbers:
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve(grid, randomize):
                            return True
                        grid[row][col] = 0
                return False
    return True
    
#Create a full grid
def generate_FullGrid():
    grid = create_empty_grid()
    solve(grid, True)
    return grid
    
#Count how many solutions we have
def count_solutions(grid, limit = 2):
    count = [0]
    #solution(count, grid, limit)
    solution(count, grid, limit):
    return count[0]
        
    
def solution(count, grid, limit):
    if count[0] >= limit:
        return
    for row in range(9):
        for col in range (9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if isValid(grid, row col, num):
                        grid[row][col] = num
                        solution(count, grid, limit)
                        grid[row][col] = 0
                return
    count[0] += 1
    
def check_solution(puzzle, current):
    for row in range(9):
        for col in range(9):
            if current[row][col] == 0:
                return False, "Puzzle is not complete yet."
    for i in range(9):
        if sorted(current[i]) != list(range(1, 10)):
            return False, f"Row {i+1} is incorrect."
        if sorted([current[r][i] for r in range(9)]) != list(range(1, 10)):
            return False, f"Column {i+1} is incorrect."
    for br in range(3):
        for bc in range(3):
            box = [current[br*3+r][bc*3+c] for r in range(3) for c in range(3)]
            if sorted(box) != list(range(1, 10)):
                return False, f"Box ({br+1},{bc+1}) is incorrect."
    return True, "Congratulations! You solved it!"
    
    
if __name__ == "__main__":
    main()