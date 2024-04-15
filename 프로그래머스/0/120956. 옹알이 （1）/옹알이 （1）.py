def solution(babbling):
    answer = 0

    c = ["aya", "ye", "woo", "ma"]
    
    for i in babbling:
        a = i
        b = []
        for j in c:
            b.append(i.count(j))
            a= a.replace(j,'1')
            
        if max(b)<2 and a.isdigit():
            answer +=1
        
        
    
        
    return answer