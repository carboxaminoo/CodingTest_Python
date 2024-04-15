
    
def solution(board):
    answer = 0
    aaa = [-1,0,1]
    n = len(board)
    for i in range(n):
        board[i].append(0)
        board[i].insert(0,0)
    
    n += 2
    board.append([0 for x in range(n)])
    board.insert(0,[0 for x in range(n)])
    
    for l in range(n):
        for m in range(n):
            if board[l][m]==1: 
                for aa in aaa:
                    for bb in aaa:
                        if board[l+aa][m+bb]==0:
                            board[l+aa][m++bb]=2
                

    for j in range(1,n-1):
        answer += board[j][1:-1].count(0)
    return answer