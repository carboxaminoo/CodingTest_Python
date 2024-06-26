# 처음에 재귀로 풀었더니 런타임 에러 발생
def F(n):
    if n in [0,1]:
        return n
    else:
        return F(n-1)+F(n-2)
    
    
def solution(n):

    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    
    return b %1234567