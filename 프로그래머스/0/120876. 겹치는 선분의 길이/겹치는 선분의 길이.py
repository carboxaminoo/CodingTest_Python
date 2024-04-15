def make(a,b):
    c = sorted(a+b)
    if a[0]<=b[0]<=a[1] or a[0]<=b[1]<=a[1]:
        return c[1:3],c[2]-c[1]
    else: 
        if a[0]>=b[0] and a[1]<=b[1]:
            return c[1:3],c[2]-c[1]
        return [0,0],0

def adding(a,b):
    c = sorted(a+b)
    if a[0]<=b[0]<=a[1] or a[0]<=b[1]<=a[1]:
        return [c[0],c[3]],c[3]-c[0]
    else: 
        if a[0]>=b[0] and a[1]<=b[1]:
            return [c[0],c[3]],c[3]-c[0]
            
    return [0,0],0

def solution(lines):
    A,a = make(lines[0],lines[1])
    B,b = make(lines[0],lines[2])
    C,c = make(lines[1],lines[2])
    D,d = adding(A,B)
    E,e = adding(A,C)
    F,f = adding(B,C)
    
    if d+e+f ==0:return a+b+c
    elif d*e*f != 0:return max(d,e,f)
    else: 
        g = d+e+f
        if d !=0:
            g+=c
        elif e != 0:
            g+=b
        else:
            g+=a
            
            
        return g

    
    