def solution(n):
    answer = sorted([x for x in str(n)])
    answer.reverse()
    answer = ''.join(answer)
    
    
    return int(answer)