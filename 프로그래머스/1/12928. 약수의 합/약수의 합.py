def solution(n):
    adding = 0
    if n == 0:
        return 0
    else:
        for i in range(1, n+1):
            if n % i ==0:
                adding+= i 
     
    return adding