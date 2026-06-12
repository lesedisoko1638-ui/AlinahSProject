import random
import ctime

def main():
    pass
    
def isValid(grid, row, col, num):
    #This will check if ever the number if alreday there in the row
    if num in grid[row]:
        return False
    #This will check if the number is already there in that column
    if num in grid[col]:
        return False
    #Otherwise you are able to place the number there
    return True
    
    
if __name__ == "__main__":
    main()