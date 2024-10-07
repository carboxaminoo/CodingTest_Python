T = int(input())
for i in range(T):
    n = int(input())
    n_list = [int(x) for x in input().split()]
    n_list.sort()
    mid = sum(n_list)/n
    count = 0
    for j in n_list : 
        if j <= mid : 
            count +=1
        else:
            break
    print(f'#{i+1} {count}')
    