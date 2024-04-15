def solution(A, B, C, D):
    numer = A*D+ C*B
    denom = B*D
    
    answer =[]
    AAA = 0
    for i in range(2, min(numer,denom)+1):
        if numer %i ==0 and denom%i ==0:
            AAA = i
            
    if AAA ==0:
        answer.append(numer)
        answer.append(denom)
    else:
        answer.append(numer//AAA)
        answer.append(denom//AAA)
    
    return answer