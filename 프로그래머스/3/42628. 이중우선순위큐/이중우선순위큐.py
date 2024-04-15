def solution(operations):
    answer = []
    for i in operations:
        j,k = i.split()
        k = int(k)
        if j == "I":
            answer.append(k)
        else:
            if answer:
                if k >0:
                    del answer[answer.index(max(answer))]
                else:
                    del answer[answer.index(min(answer))]
        
    
    if not answer: 
        return [0,0]
    else: 
        return [max(answer),min(answer)]