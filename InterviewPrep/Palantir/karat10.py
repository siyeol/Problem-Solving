matrix1 = [[1,1,1,1],
           [0,1,1,1],
           [0,1,0,0],
           [1,1,0,1],
           [0,0,1,1]]
rows1_1    =  [[], [1], [1,2], [1], [2]]
columns1_1 =  [[2,1], [1], [2], [1]]
# False
rows1_2 = [[],[],[1],[1],[1,1]]
columns1_2 = [[2],[1],[2],[1]]


matrix2 = [
    [1,1],
    [0,0],
    [0,0],
    [1,0]
]
# False
rows2_1 = [[],[2],[2],[1]]
columns2_1 = [[1,1],[3]]


def validate_nonogram(matrix, y_inst, x_inst):
    
    Y = len(matrix)#height
    X = len(matrix[0])#width
    
    #check valid
    def validate(single, valid):
        if len(valid) == 0:
            return True

        counter = valid.pop(0)
        for idx, elem in enumerate(single):
            if (counter == 0 and elem == 1):
                if len(valid) != 0:
                    counter = valid.pop(0)
                else:
                    return True
                
            if elem == 0:
                counter -= 1
            
        if len(valid) == 0 and counter == 0:
            return True
        else:
            return False
                
    #check row
    def check_row(matrix, y_inst):
        for mat, y in zip(matrix, y_inst):
            if validate(mat, y) is False:
                return False
        return True
                
    row_bool = check_row(matrix, y_inst)
    
    #check column
    def check_column(matrix, x_inst):
        for x, x_instruct in zip(range(X), x_inst):
            col = list()
            for y in range(Y):
                col.append(matrix[y][x])
            if (validate(col,x_instruct)) is False:
                return False
                
        return True
            
    col_bool = check_column(matrix, x_inst)
                    
    # bool && return
    if row_bool and col_bool:
        return True
    else:
        return False
        
    
print(validate_nonogram(matrix1, rows1_1, columns1_1))
print(validate_nonogram(matrix1, rows1_2, columns1_2))
print(validate_nonogram(matrix2, rows2_1, columns2_1))