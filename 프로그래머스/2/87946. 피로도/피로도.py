def solution(k, dungeons):
    global answer
    answer = 0
    
    l = [0]*len(dungeons)
    
    D(k,0,dungeons,l)
    return answer

def D(k,c,d,l):
    global answer 
    if c > answer:
        answer = max(answer,c)
    
    for i in range(len(d)):
        if l[i]==0 and d[i][0] <= k:
            l[i] = 1
            D(k-d[i][1],c+1,d,l)
            l[i] = 0