def solution(answers):
    answer = [0,0,0]
    a = []
    c1 = [1,2,3,4,5]
    c2 = [2,1,2,3,2,4,2,5]
    c3 = [3,3,1,1,2,2,4,4,5,5]
            
    for  i in range(len(answers)):
        if answers[i] == c1[i%5]:
            answer[0]+=1
        if answers[i] == c2[i%8]:
            answer[1]+=1
        if answers[i] == c3[i%10]:
            answer[2]+=1
    
    k = max(answer)
    
    for j in range(3):
        if answer[j] == k:
            a.append(j+1)
    
    return a