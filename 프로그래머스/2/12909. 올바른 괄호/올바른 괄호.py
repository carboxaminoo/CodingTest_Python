def solution(s):
    answer = True
    a = ['[','{','(',']','}',')']
    count = [0,0,0]
    
    if s[0] not in a[:3]:
        return False
    elif s[-1] not in a[3:]:
        return False
    
    for i in s :
        idx = a.index(i)
        if idx <3 :
            count[idx%3] = count[idx%3]+1
        else:
            count[idx%3] = count[idx%3]-1
            if min(count) < 0:
                return False
    
    if min(count) == 0 and max(count)==0:
        return True
    else:
        return False