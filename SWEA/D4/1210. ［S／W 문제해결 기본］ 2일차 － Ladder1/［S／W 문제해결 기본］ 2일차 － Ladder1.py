for _ in range(10):
    T = int(input())
    n_list = []
    for j in range(100):
        n_list. append([0]+list(map(int,input().split()))+[0])
    
    head = 0 # 방향[-1,0,1]
    idx_1 = 99 # 1차 (상하)
    idx_2 = n_list[idx_1].index(2)# 2차 (좌우)
    
    while idx_1 != 0:
        if head == 0:
            if n_list[idx_1][idx_2-1] ==1:
                idx_2 -= 1
                head = -1
            elif n_list[idx_1][idx_2+1] == 1:
                idx_2 +=1
                head = 1
            else:
                idx_1 -=1
        else : 
            if n_list[idx_1][idx_2+head] == 1:
                idx_2 += head
            else:
                idx_1 -= 1
                head =0
    
    
    
    print(f'#{T} {idx_2-1}')