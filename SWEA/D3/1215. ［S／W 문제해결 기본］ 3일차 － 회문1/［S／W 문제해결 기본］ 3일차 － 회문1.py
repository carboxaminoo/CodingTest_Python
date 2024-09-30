for i in range(10):
    T = int(input())
    s_list = []
    count = 0
    for j in range(8):
        s_sts = [x for x in input()]
        s_list.append(s_sts)
        for k in range(9-T):
            a = s_sts[k:k+T]
            check = True
            for l in range(T//2) :
                if a[l] != a[-(l+1)]:
                    check = False
                    break            
            if check :
                count +=1
    for m in range(8):
        s_sts = [s_list[k][m] for k in range(8)]
        for k in range(9-T):
            a = s_sts[k:k+T]
            check = True
            for l in range(T//2):
                if a[l] != a[-(l+1)]:
                    check = False
                    break
            if check:
                count +=1

    print(f'#{i+1} {count}')
                    
        