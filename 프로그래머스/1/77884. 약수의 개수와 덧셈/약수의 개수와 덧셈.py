def solution(left, right):
    answer =0
    for i in range(left, right+1):
        add = i**(1/2)
        if int(add)== add:
            answer -= i
        else: 
            answer += i            
    return answer