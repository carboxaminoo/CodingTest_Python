def solution(s):
    
    count_zero = s.count('0')
    s = s.count('1')
    if s ==1 and count_zero == 0:
        return [0,0]
    
    count_time = 1
    while s != 1:
        count_one = 0
        count_time = count_time + 1
        copy_s = s
        while copy_s > 0:
            if copy_s %2: 
                count_one = count_one + 1 
            else: 
                count_zero = count_zero + 1
            copy_s = copy_s //2
        s = count_one
    return [count_time, count_zero]