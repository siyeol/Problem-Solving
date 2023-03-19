def solution(commands):
    board = [['']*50 for _ in range(50)]
    dup = [[0]*50 for _ in range(50)]
    answer = []

    def chng(val1, val2): #beware of dup
        for y in range(50):
            for x in range(50):
                if board[y][x]==val1:
                    board[y][x] = val2

    dupcnt = 1

    for command in commands:
        cmd_list = command.split()
        
        if cmd_list[0] == 'UPDATE': #병합!
            if len(cmd_list) == 4:
                r, c = int(cmd_list[1])-1, int(cmd_list[2])-1
                board[r][c] = str(cmd_list[-1])

                if dup[r][c]!=0 :
                    temp_rc = dup[r][c]
                    for y in range(50):
                        for x in range(50):
                            if dup[y][x] == temp_rc:
                                board[y][x] = str(cmd_list[-1])

            elif len(cmd_list)==3:
                v1, v2 = str(cmd_list[1]), str(cmd_list[2])
                chng(v1, v2)

        elif cmd_list[0] == 'MERGE':
            r1, c1 = int(cmd_list[1])-1, int(cmd_list[2])-1
            r2, c2 = int(cmd_list[3])-1, int(cmd_list[4])-1
            
            if r1==r2 and c1==c2:
                continue
                
            if board[r1][c1] != '' and board[r2][c2] != '':
                temp_1, temp_2 = board[r1][c1], board[r2][c2]
                board[r2][c2] = board[r1][c1]
                dupcnt+=1
                for y in range(50):
                    for x in range(50):
                        if board[y][x] == temp_1 or board[y][x] == temp_2:
                            board[y][x] = temp_1
                            dup[y][x] = dupcnt
                            
            elif board[r1][c1] != '' and board[r2][c2] == '':
                temp_rc1, temp_rc2 = dup[r1][c1], dup[r2][c2]
                for y in range(50):
                    for x in range(50):
                        if dup[y][x]==temp_rc2:
                            board[r2][c2] = board[r1][c1]
                            dup[y][x] = temp_rc1
                    
            elif board[r1][c1] == '' and board[r2][c2] != '':
                temp_rc1, temp_rc2 = dup[r1][c1], dup[r2][c2]
                for y in range(50):
                    for x in range(50):
                        if dup[y][x]==temp_rc1:
                            board[r1][c1] = board[r2][c2]
                            dup[y][x] = temp_rc2
                    
            else:
                temp_1, temp_2 = dup[r1][c1], dup[r2][c2]
                dupcnt+=1
                for y in range(50):
                    for x in range(50):
                        if dup[y][x] == temp_1 or dup[y][x] == temp_2:
                            dup[y][x] = dupcnt
                    
            
        elif cmd_list[0] == 'UNMERGE':
            r, c = int(cmd_list[1])-1, int(cmd_list[2])-1
            
            temp_rc = dup[r][c]
            temp_val = board[r][c]
            
            print(temp_val)
            if temp_rc != 0:
                for y in range(50):
                    for x in range(50):
                        if dup[y][x] == temp_rc:
                            dup[y][x] = 0
                            board[y][x] = ''

            if temp_val != '':
                board[r][c] = temp_val
            
        elif cmd_list[0] == 'PRINT': #병합
            r, c = int(cmd_list[1])-1, int(cmd_list[2])-1
            if board[r][c]!='':
                answer.append(board[r][c])
            else:
                answer.append("EMPTY")
    return answer