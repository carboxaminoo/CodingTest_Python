def solution(num):
    n = num
    for i in range(500):
        if n == 1:
            return i
        if n %2 == 0:
            n = n//2
        else:
            n = n*3 +1
    if n !=1 : 
        return -1
    else:return 500