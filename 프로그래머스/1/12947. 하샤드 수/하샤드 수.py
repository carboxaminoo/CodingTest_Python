def solution(x):
    adding = [int(x) for x in str(x)]
    if x%sum(adding): 
        return False
    else: 
        return True