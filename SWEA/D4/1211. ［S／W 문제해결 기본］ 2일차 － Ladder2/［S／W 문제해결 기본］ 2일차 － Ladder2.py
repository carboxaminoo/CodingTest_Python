## Ladder1 코드 재사용 

for _ in range(10):
    T = int(input())
    n_list = []
    for j in range(100):
        n_list. append([0]+list(map(int,input().split()))+[0])
        
    start = [ x for x in range(100) if n_list[99][x] ==1]
    min_count = 10000   # 200으로 애매하게 잡아서 Error
    min_start = 1
    for i in start :
        head = 0 # 방향[-1,0,1]
        idx_1 = 99 # 1차 (상하)
        idx_2 = i 
        count = 0
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
            count += 1
            
        if min_count > count:
            min_count = count 
            min_start = idx_2
        elif min_count == count and min_start < idx_2:
            min_start = idx_2
    
    print(f'#{T} {min_start-1}')