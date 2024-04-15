def solution(name, yearning, photo):
    answer = []
    for i in range(len(photo)):
        adding = 0
        for j in photo[i]:
            if j in name :
                adding += yearning[name.index(j)]
            
        answer.append(adding)
        
    return answer