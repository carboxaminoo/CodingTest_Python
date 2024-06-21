def solution(s):
    A = s.split(" ")
    B = ""
    for i in range(len(A)):
        # upper, lower 로 나눠서 쓰면 RunTime Error 발생
        st = A[i].capitalize()
        B = B + st
        if i !=len(A)-1:
            B = B +" "
        else: 
            return B
                