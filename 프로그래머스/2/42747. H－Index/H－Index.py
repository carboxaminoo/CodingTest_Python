def solution(citations):
    if max(citations) >len(citations):
        n = len(citations)
    else:
        n = max(citations)
        
    
    
    for i in range(n,0,-1):
        up=0
        down=0
        for j in citations:
            if j < i:
                down +=1
            else:
                up+=1
            if down > i:
                break
        
        if up >=i and down<=i:
                return i
            
                
    return 0