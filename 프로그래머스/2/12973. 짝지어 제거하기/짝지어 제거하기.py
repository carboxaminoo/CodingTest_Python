def solution(s):
    if len(s)%2 ==1: return 0
    adding = []
    for i in s:
        adding.append(i)
        check = True
        while len(adding) > 1 and check: 
            if adding[-1] == adding[-2]:
                adding.pop()
                adding.pop()
            else: 
                check = False

            
    return 0 if adding else 1