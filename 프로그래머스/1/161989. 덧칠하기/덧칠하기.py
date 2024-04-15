def solution(n, m, section):
    answer = 0
    a = 0
    
    for i in range(len(section)):
        if a < section[i]:
            a = section[i]+m-1
            answer += 1

        
        
    return answer