def solution(brown, yellow):
    a = (brown-4)//2
    for i in range(1,a+1):
        if i*(a-i) == yellow: 
            return [a-i+2,i+2]
