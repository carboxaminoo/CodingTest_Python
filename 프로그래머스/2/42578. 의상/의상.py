
def solution(clothes):
    answer = 1
    cat = {}
    cat1 = set()
    for cloth in clothes: 
        if cloth[1] in cat1:
            cat[cloth[1]] +=1
        else:
            cat1.add(cloth[1])
            cat[cloth[1]] = 1

    for i in cat.values():
        answer *= (i+1)
        
    return answer-1