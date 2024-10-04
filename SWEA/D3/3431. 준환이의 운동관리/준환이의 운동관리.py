def cal_range(a,b,c):
    if c < a :
        return a-c
    elif b<c :
        return -1
    else:
        return 0

T = int(input())
for i in range(T):
    a,b,c = map(int, input().split())
    
    
    
    print(f'#{i+1} {cal_range(a,b,c)}')