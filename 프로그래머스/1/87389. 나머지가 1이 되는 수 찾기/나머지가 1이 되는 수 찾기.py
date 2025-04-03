def solution(n):
    answer = 2
    for i in range(2,n//2):
        if (n-1)% i == 0:
            return i 
    return n-1