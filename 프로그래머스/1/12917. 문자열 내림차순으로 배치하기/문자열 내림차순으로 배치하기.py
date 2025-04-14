def solution(s):
    answer = [i for i in s]
    answer.sort(reverse=1)
    return "".join(answer)