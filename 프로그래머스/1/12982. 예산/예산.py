def solution(d, budget):
    m = budget
    answer = 0
    adding = sorted(d)

    for i in adding:
        m -= i
        answer += 1
        
        if m <0: 
            return answer -1 
    
    return answer