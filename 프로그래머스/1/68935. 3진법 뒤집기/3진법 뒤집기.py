def solution(n):
    answer = 0
    adding = []
    while n !=0 :
        adding.append(str(n % 3))
        n = n//3
    
    base_3 = int("".join(adding))
    str_base_3 = str(base_3)
    print(base_3)
    for i in range(0, len(str_base_3)):
        answer += int(str_base_3[-i-1]) * (3**i)
        print(answer)
        
    
    return answer