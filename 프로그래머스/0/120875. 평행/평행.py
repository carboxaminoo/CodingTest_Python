def cal(a,b):
    return (a[1]-b[1])/(a[0]-b[0])
    
def solution(dots):
    if cal(dots[0],dots[1])==cal(dots[2],dots[3]):
        return 1
    elif cal(dots[0],dots[2])==cal(dots[1],dots[3]):
        return 1
    elif cal(dots[0],dots[3])==cal(dots[1],dots[2]):
        return 1
    else:
        return 0
