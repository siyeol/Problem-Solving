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

                for y in range(50):
                    for x in range(50):
                        if dup[r][c]!=0 and dup[y][x] == dup[r][c]:
                            board[y][x] = str(cmd_list[-1])

            elif len(cmd_list)==3:
                v1, v2 = str(cmd_list[1]), str(cmd_list[2])
                chng(v1, v2)

        elif cmd_list[0] == 'MERGE':
            r1, c1 = int(cmd_list[1])-1, int(cmd_list[2])-1
            r2, c2 = int(cmd_list[3])-1, int(cmd_list[4])-1
            
            if r1 == r2 and c1 == c2:
                continue

            color_list = list()
            if dup[r1][c1] == 0 and dup[r2][c2] == 0: #vanilla
                dup[r1][c1] = dupcnt
                dup[r2][c2] = dupcnt
                dupcnt+=1
                if board[r1][c1] != '' and board[r2][c2] != '':
                    board[r2][c2] = board[r1][c1]
                elif board[r1][c1] == '' and board[r2][c2] != '':
                    board[r1][c1] = board[r2][c2]
                elif board[r1][c1] != '' and board[r2][c2] == '':
                    board[r2][c2] = board[r1][c1]

            elif dup[r1][c1] != 0 and dup[r2][c2] == 0:
                # dup[r1][c]
                dup[r2][c2] = dup[r1][c1]
                board[r2][c2] = board[r1][c1]
            elif dup[r1][c1] == 0 and dup[r2][c2] != 0:
                #2 o
                if board[r1][c1] == '':
                    board[r1][c1] = board[r2][c2]
                    dup[r1][c1] = dup[r2][c2]
                else:
                    for y in range(50):
                        for x in range(50):
                            if dup[y][x] == dup[r2][c2]:
                                dup[y][x]=dup[r1][c1]
                                board[y][x] = board[r1][c1]                    
            else: #double join
                for y in range(50):
                    for x in range(50):
                        if dup[y][x] == dup[r2][c2]:
                            dup[y][x] = dup[r1][c1]
                            board[y][x] = board[r1][c1]

            # if board[r1][c1] != '' and board[r2][c2] != '':
            #     board[r2][c2] = board[r1][c1]
            # elif board[r1][c1] == '' and board[r2][c2] != '':
            #     board[r1][c1] = board[r2][c2]
            # elif board[r1][c1] != '' and board[r2][c2] == '':
            #     board[r2][c2] = board[r1][c1]
            # what if 둘다 null?

        elif cmd_list[0] == 'UNMERGE':
            r, c = int(cmd_list[1])-1, int(cmd_list[2])-1
            temp_store = ''
            if board[r][c] != '':
                temp_store=board[r][c]

            temp_dup = dup[r][c]
            for y in range(50):
                for x in range(50):
                    if temp_dup!=0 and dup[y][x] == temp_dup:
                        dup[y][x] = 0
                        board[y][x] = ''
            board[r][c] = temp_store

        elif cmd_list[0] == 'PRINT': #병합
            r, c = int(cmd_list[1])-1, int(cmd_list[2])-1
            if board[r][c]!='':
                answer.append(board[r][c])
            else:
                flag = False
                if dup[r][c] != 0:
                    for y in range(50):
                        for x in range(50):
                            if dup[r][c]!=0 and dup[y][x] == dup[r][c] and board[x][y]:
                                answer.append(board[y][c])
                                flag = True
                                break #UPGRADE
                        if flag:
                            break
                answer.append("EMPTY")
    return answer

input = ["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "PRINT 2 3", "PRINT 40 40"]
input = ["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]
input = ["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]
print(solution(input))

