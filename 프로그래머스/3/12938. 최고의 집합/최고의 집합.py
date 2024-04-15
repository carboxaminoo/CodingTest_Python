def solution(n, s):
    answer = []
    power = 0
    if s - n <0:
        return [-1]
    
    for i in range(n):
        answer.append(s//n)
        
    if s%n != 0:
        for j in range(s%n):
            answer[j]+=1
        
    return sorted(answer)