def pw_cal(a,b):
    if b ==0:
        return 1
    else: 
        return a*pw_cal(a,b-1)
for i in range(10):
    T = int(input())
    a,b = map(int, input().split())
    print(f'#{T} {pw_cal(a,b)}')