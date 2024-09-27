def finding(w,s):
    count = s.find(w)
    if count != -1:
        return 1 + finding(w,s[count + len(w):])
    else :
        return 0

for _ in range(10):
    T = int(input()) 
    f_w = input()
    f_s = input()
    
    print(f'#{T} {finding(f_w,f_s)}')