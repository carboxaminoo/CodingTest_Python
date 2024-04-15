def solution(s):
    answer =0
    s1 = s + s[:len(s)-1]
    b_s = c_s = []
    d = True
    
    for i in range(len(s)):
        
        b_s = s1[i:i+len(s)]
        while True:
            c_s = len(b_s)
            b_s = b_s.replace('()','')
            b_s = b_s.replace('{}','')
            b_s = b_s.replace('[]','')
            if len(b_s) == 0:
                answer+=1
                break
                
            elif len(b_s)== c_s:
                break
                
                
            
    return answer