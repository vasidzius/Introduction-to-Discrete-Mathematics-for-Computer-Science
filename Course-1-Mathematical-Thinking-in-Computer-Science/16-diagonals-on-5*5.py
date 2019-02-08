'''

draw N diagonals in m*m squares that do not touch each other.
Resolve it for case N = 16 and m = 5
something like:

/////
    
/////

\\\\\ 

but here only 15 so it is incorrect

'''

def printMatrix(matrix):
    for row in matrix:
        for val in row:
            print(val, end=" "),
        print()
    print()
        
def countDiagonals(matrix):
    result = 0;
    for row in matrix:
        for val in row:
            if(val == '/' or val == '\\'):
                result += 1;
    return result;

def calculateNewIndex(curRow, curCol, nCols):
    if(curCol < nCols - 1):
        curCol += 1
    else:
        curRow += 1
        curCol = 0
    return curRow, curCol

def is_allowed(matrix, curRow, curCol):
    cur = matrix[curRow][curCol]
    if cur == 'x':
        return True

    #left top corner
    if curRow == 0 and curCol == 0:
        return True
        
    #top border
    if curRow == 0 and curCol > 0:
        if cur == '/' and (matrix[curRow][curCol-1] == '/' or matrix[curRow][curCol-1] == 'x'):
            return True
        elif cur == '\\' and (matrix[curRow][curCol-1] == '\\' or matrix[curRow][curCol-1] == 'x'):
            return True
        else: 
            return False
    
    #left border
    if curRow > 0 and curCol == 0:
        if cur == '/' and (
            (matrix[curRow-1][curCol] == '/' or matrix[curRow-1][curCol] == 'x')
            and (matrix[curRow-1][curCol+1] == '\\' or matrix[curRow-1][curCol+1] == 'x')
            ):
            return True
        elif cur == '\\' and (
            matrix[curRow-1][curCol] == '\\' or matrix[curRow-1][curCol] == 'x'
            ):
            return True
        else: 
            return False 
    
    #middle cell
    if curRow > 0 and curCol > 0 and curCol < len(matrix[0])-1:
        if cur == '/' and (
            (matrix[curRow][curCol-1] == '/' or matrix[curRow][curCol-1] == 'x')
            and (matrix[curRow-1][curCol] == '/' or matrix[curRow-1][curCol] == 'x')
            and (matrix[curRow-1][curCol+1] == '\\' or matrix[curRow-1][curCol+1] == 'x')
            ):
            return True
        elif cur == '\\' and (
            (matrix[curRow][curCol-1] == '\\' or matrix[curRow][curCol-1] == 'x')
            and (matrix[curRow-1][curCol-1] == '/' or matrix[curRow-1][curCol-1] == 'x')
            and (matrix[curRow-1][curCol] == '\\' or matrix[curRow-1][curCol] == 'x')
            ):
            return True
        else: 
            return False 
        
    #right border
    if curCol == len(matrix[0])-1:
        if cur == '/' and (
            (matrix[curRow][curCol-1] == '/' or matrix[curRow][curCol-1] == 'x')
            and (matrix[curRow-1][curCol] == '/' or matrix[curRow-1][curCol] == 'x')
            ):
            return True
        elif cur == '\\' and (
            (matrix[curRow][curCol-1] == '\\' or matrix[curRow][curCol-1] == 'x')
            and (matrix[curRow-1][curCol-1] == '/' or matrix[curRow-1][curCol-1] == 'x')
            and (matrix[curRow-1][curCol] == '\\' or matrix[curRow-1][curCol] == 'x')
            ):
            return True
        else: 
            return False 

def add_new_symb(matrix, nRows, nCols, n, curRow, curCol):
    
    for cur in ['/', '\\', 'x']:
        matrix[curRow][curCol] = cur
        
        if is_allowed(matrix, curRow, curCol):
            if(countDiagonals(matrix) == n):
                printMatrix(matrix)
                exit()
            newCurRow, newCurCol = calculateNewIndex(curRow, curCol, nCols)
            if(newCurCol < nCols and newCurRow < nRows):
                add_new_symb(matrix, nRows, nCols, n, newCurRow, newCurCol)
        
nRows = 5
nCols = 5
nDiagonals = 16
matrix = [['x' for x in range(nCols)] for y in range(nRows)] 
    
print('Start')
add_new_symb(matrix, nRows, nCols, nDiagonals, 0, 0)
