# Generator : http://www.landofcrispy.com/nonogrammer/nonogram.html?mode=build

#cols = [[3,2,3], [5,3,2], [3,2,1,1], [2,6,1], [1,3,2], [2,4,1], [4,1,1,1], [3,5], [1,2,5], [1,1,3,2], [1,3,1,1], [1,1,2,2]]
#rows = [[2,1,3,1], [11], [3,2,1], [2,2,2], [2,3,1,1], [1,4,1,2], [6,1,1], [1,1,3], [4,6], [1,2,2,1], [3,2,3], [1,1,5]]

#cols = [[1], [1], [3,4,1], [6,2,1], [1,2,1], [4,2], [7,2], [8,1], [7], [2]]
#rows = [[2], [2,1], [7], [6], [1,3], [1,2], [1,2], [1,3], [1,3], [1,2], [1,2], [1, 1], [3,2], [2,5]]

cols = [[2], [1,4], [3,6], [5,2,1], [6,2], [12], [3,8], [2,6], [1,6], [7,1], [8,1], [4,3], [3,3,2], [10], [9], [7,1], [6], [3], [3]]
rows = [[2], [2,3], [2,3], [4], [4, 5], [5,8], [2,13], [12,4,1], [11,7], [2,6,7], [6,6], [3,2,4], [3,4], [3,7]]

#cols = [[], [1,1], [1], [1], [1,1,1], [1]]
#rows = [[], [1,1], [], [1,1], [2], [2]]

numRows = len(rows)
numCols = len(cols)

grid = [[-1 for i in range(numCols)] for j in range(numRows)]

#┏━━━┳━━━┳━━━┓
#┃###┃   ┃   ┃
#┣━━━╋━━━╋━━━┫
#┃###┃###┃   ┃
#┣━━━╋━━━╋━━━┫
#┃###┃   ┃   ┃
#┗━━━┻━━━┻━━━┛

colsPoss = [[] for col in cols]
rowsPoss = [[] for row in rows]


def PrintRow(size, grid, yCoord, longestRow, top=1):
    res = "" # Input to print
    # On the left, we have the lines to print the inputs
    for i in range(longestRow):
        res += "━━━"
    
    # TOP
    if top == 0: # Top line of the grid
        res += "┏"
    elif top == 1: # Middle line
        res += "┣"
    else:
        res += "┗" # bottom of the grid
        
    for i in range(size):
        res += "━━━" # To print between each cells
        if i < size-1:
            if top == 0:
                res += "┳"
            elif top == 1:
                res += "╋"
            else:
                res += "┻"
    # To close each rows
    if top == 0:
        res += "┓"
    elif top == 1:
        res += "┫"
    else:
        res += "┛"
    print(res) # Print the row
    
    res = "" # Reset input to print (return to line)
    # We don't print this part for the liste line because this is where we print
    # the middle of each row (where we fill or not the cell)
    if top < 2:
        for i in range(longestRow):
            if i < len(rows[yCoord]):
                res += f"{str(rows[yCoord][i]): ^3}"
            else:
                res += "   "
        
        # Middle
        res += "┃"
        for i in range(size):
            if grid[yCoord][i] == 1:
                res += "###"
            elif grid[yCoord][i] == 0:
                res += " X "
            else:
                res += "   "
            if i < size-1:
                res += "┃"
        res += "┃"
        print(res)

def PrintColsNums(longestRow): # Do the same as the "PrintRow" methods with only this symbol ┃ and spaces
    longestCol = 0
    for col in cols:
        if len(col) > longestCol:
            longestCol = len(col)

    for j in range(longestCol):
        res = ""
        for i in range(longestRow):
            res += "   "
        res += "┃"
        for i in range(len(cols)):
            if j < len(cols[i]):
                res += f"{str(cols[i][j]): ^3}"
            else:
                res += "   "
            if i < len(cols)-1:
                res += "┃"
        res += "┃"
        print(res)

'''
    Main method to print the grid with a good looking display
'''
def PrintGrid():
    # Firstly, we get the number of max values in the rows as inputs to have all
    # row as the same size
    longestRow = 0
    for row in rows:
        if len(row) > longestRow:
            longestRow = len(row)
            
    '''
        Here's the differents lines :
            ┏━━━┳━━━┳━━━┓
            
            ┣━━━╋━━━╋━━━┫
            
            ┗━━━┻━━━┻━━━┛
        To close the cells, we use this symbol : ┃
    '''
            
    PrintColsNums(longestRow) # This is the method to print the columns on top
                              # of the grid as we do with rows
    
    PrintRow(numCols, grid, 0, longestRow, 0) # Then we print the first row
                                              # Because the top lines are not
                                              # the same everywhere
    for i in range(numRows-1):
        PrintRow(numCols, grid, i+1, longestRow, 1) # Print all middles rows
    PrintRow(numCols, grid, -1, longestRow, 2) # Same as the top's grid

def IsComplete(grid):
    for row in grid:
        for cell in row:
            if cell == -1:
                return False
    return True

def Solve():
    while (IsComplete(grid) == False):
        GetAllPosibilitiesRow(grid)
        PrintGrid()
        # Rows
        for i in range(len(rows)):
            if len(rowsPoss[i]) == 1:
                for j in range(len(cols)): 
                    if j < len(rowsPoss[i][0]):
                        grid[i][j] = rowsPoss[i][0][j]
            else:
                for j in range(len(cols)):
                    allSame = True
                    if len(rowsPoss[i]) > 0 and len(rowsPoss[i][0]) > 0 and j < len(rowsPoss[i][0]):
                        firstVal = rowsPoss[i][0][j]
                        for poss in rowsPoss[i]:
                            if poss[j] != firstVal:
                                allSame = False
                        if allSame:
                            grid[i][j] = rowsPoss[i][0][j]
        # Cols
        for i in range(len(cols)):
            if len(colsPoss[i]) == 1:
                for j in range(len(rows)):
                    if j < len(colsPoss[i][0]):
                        grid[j][i] = colsPoss[i][0][j]
            else:
                for j in range(len(rows)):
                    allSame = True
                    if len(colsPoss[i]) > 0 and len(colsPoss[i][0]) > 0 and j < len(colsPoss[i][0]):
                        firstVal = colsPoss[i][0][j]
                        for poss in colsPoss[i]:
                            if poss[j] != firstVal:
                                allSame = False
                        if allSame:
                            grid[j][i] = colsPoss[i][0][j]
        FillEmpty()
    PrintGrid() 


        
def SumArray(array):
    res = 0
    for val in array:
        res += val
    return res

# Rows
def CheckIndivPossRow(input_, row):
    res = []
    
    i = 0
    j = input_
    while j <= len(row):
        subRow = row[i:j]
        if not 0 in subRow:
            for k in range(len(subRow)):
                subRow[k] = 1
            row_ = []
            for k in range(len(row)):
                row_.append(row[k])
                if row_[k] == -1:
                    row_[k] = 0
            new_poss = row_[0:i] + subRow
            res.append(new_poss)
        i+=1
        j+=1
    return res
    

def testSorted(inputs, row):
    res = True
    
    i = 0
    for input_ in inputs:
        while i < len(row) and row[i] == 0:
            i += 1
        for j in range(input_):
            if i+j >= len(row) or row[i+j] == 0:
                return False
        i += j
        if i+1 < len(row) and row[i+1] != 0:
            return False
        i += 1
    
    while i < len(row):
        if row[i] == 1:
            return False
        i += 1
    return res


# Poss = possibilities
def CheckPossRow(inputs, row, allInputs, possList):
    if len(inputs) == 1:
        poss = CheckIndivPossRow(inputs[0], row)
        for poss_ in poss:
            row_ = []
            for i in range(len(poss_)):
                row_.append(poss_[i])
            for i in range(len(row)-len(poss_)):
                row_.append(row[len(poss_)+i])
            if len(poss_) < len(row_):
                row_[len(poss_)] = 0
            count = 0
            for i in range(len(row_)):
                if row_[i] == 1:
                    count += 1
                elif row_[i] == -1:
                    row_[i] = 0
                if row[i] != -1 and row_[i] != row[i]:
                    count = 0
            if count == SumArray(allInputs):
                if not row_ in possList and testSorted(allInputs, row_): # CHANGED
                    possList.append(row_)
    elif len(inputs) > 0:
        poss = CheckIndivPossRow(inputs[0], row[0:len(row)-SumArray(inputs[1:len(inputs)])-1])
        for poss_ in poss:
            row_ = []
            for i in range(len(poss_)):
                row_.append(poss_[i])
            for i in range(len(row)-len(poss_)):
                row_.append(row[len(poss_)+i])
            if len(poss_) < len(row_):
                row_[len(poss_)] = 0
            CheckPossRow(inputs[1:len(inputs)], row_, allInputs, possList)
    
    

def GetAllPosibilitiesRow(grid):
    for index in range(len(rows)):
        row = grid[index]
        #print(rows[index], row)
        poss = []
        CheckPossRow(rows[index], row, rows[index], poss)
        #print(poss)
        final_poss = []
        for poss_ in poss:
            add = True
            for i in range(len(poss_)):
                if row[i] != -1 and poss_[i] != row[i]:
                    add = False
                    break
            if add:
                final_poss.append(poss_)
        rowsPoss[index] = final_poss
    
    for index in range(len(cols)):
        row = ColToRow(grid, index)
        #print(cols[index], row)
        poss = []
        CheckPossRow(cols[index], row, cols[index], poss)
        #print(poss)
        final_poss = []
        for poss_ in poss:
            add = True
            for i in range(len(poss_)):
                if row[i] != -1 and poss_[i] != row[i]:
                    add = False
                    break
            if add:
                final_poss.append(poss_)
        colsPoss[index] = final_poss
                    
                    
def ColToRow(grid, index):
    res = []
    for i in range(len(rows)):
        res.append(grid[i][index])
    
    return res                    

def FillEmpty():
    for i in range(len(rows)):
        toCount = SumArray(rows[i])
        count = 0
        for j in range(len(cols)):
            if grid[i][j] == 1:
                count += 1
        if toCount == count:
            for j in range(len(cols)):
                if grid[i][j] == -1:
                    grid[i][j] = 0

    for i in range(len(cols)):
        toCount = SumArray(cols[i])
        count = 0
        for j in range(len(rows)):
            if grid[j][i] == 1:
                count += 1
        if toCount == count:
            for j in range(len(rows)):
                if grid[j][i] == -1:
                    grid[j][i] = 0
                    
Solve()