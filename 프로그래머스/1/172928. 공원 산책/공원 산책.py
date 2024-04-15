def solution(park, routes):
    answer = []
    count = 0
    h= w = 0 
    H = len(park)
    W = len(park[0])
    
    # S 위치 찾기 
    for i in park:
        if "S" in i:
            w = i.index("S")
            h = park.index(i)
            break
            
    for j in routes:
        d,n = j.split()
        n = int(n)
        
            

        if d == "N":
            answer = park[h-n:h]
            count = 0
            if 0 <= h-n < H :
                for j in park[h-n:h]:
                    if j[w] != "X" : count+=1
                    
                if count == len(answer):
                    h -= n
            
            
        elif d == "S":
            answer = park[h:h+n+1]
            count = 0
            if 0 <= h+n < H :
                for j in park[h:h+n+1]:
                    if j[w] != "X" : count+=1
            
                if count == len(answer):
                    h += n
            
            
        elif d == "W":
            if 0 <= w-n < W and "X" not in park[h][w-n:w]: w -= n 
            
        else:
            if 0 <= w+n < W and "X" not in park[h][w:w+n+1]: w += n
            
            

        
    
    return h,w