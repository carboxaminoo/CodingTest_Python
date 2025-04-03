def solution(n):
    adding = n**(1/2)
    if adding%1==0:
        return (adding+1)**2
    else:
        return -1