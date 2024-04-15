def solution(t, p):
    answer = 0
    p_n = len(str(p))
    t_n = len(str(t))
    p_s = str(p)
    t_s = str(t)
    
    for i in range(t_n-p_n+1):
        if t_s[i:i+p_n]<= p_s:
            answer+=1
        

    return answer