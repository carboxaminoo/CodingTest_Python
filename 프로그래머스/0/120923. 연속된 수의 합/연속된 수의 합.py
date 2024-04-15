def solution(num, total):
    answer = []
    a = total/num
    for i in range(1,num//2+1):
        answer.append(int(a)+i)
        if num%2 ==1:
            answer.append(int(a)-i)
        else: 
            answer.append(int(a)-i+1)
    if int(a) not in answer:
        answer.append(int(a))
    return sorted(answer)