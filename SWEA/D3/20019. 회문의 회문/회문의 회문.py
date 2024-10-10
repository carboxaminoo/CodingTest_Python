def recursive(sts):
    for i in range(len(sts)//2):
        if sts[i] != sts[-(i+1)]:
            return False 
    return True

T = int(input())

for i in range(T):
    sts = [x for x in input()]
    if recursive(sts):
        if recursive(sts[:len(sts)//2]):
            print(f"#{i+1} YES")
        else: 
            print(f"#{i+1} NO")
    else:
        print(f"#{i+1} NO")
        
        
    
    
    