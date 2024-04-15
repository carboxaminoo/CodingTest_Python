def solution(progresses, speeds):
    answer = []
    count = day = 0
    for i, j in zip(progresses,speeds):
        rate = (100 - i)//j
        if (100-i) % j != 0:
            rate += 1
        if day == 0:
            day = rate
        if day < rate:
            answer.append(count)
            count = 0
            day = rate
        count +=1
    if count !=0:
        answer.append(count)
        
    return answer