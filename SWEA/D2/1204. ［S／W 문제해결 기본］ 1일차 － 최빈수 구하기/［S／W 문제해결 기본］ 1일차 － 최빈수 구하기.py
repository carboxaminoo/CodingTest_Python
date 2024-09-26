T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    tk = int(input())
    count = 0 
    n_list = list(map(int,input().split()))
    n_set = set(n_list)
    n_dict = {}
    
    for i in n_set:
        n_dict[i] = n_list.count(i)
        
        
    count = max(n_dict.values()) 
    key = [x for x, y in n_dict.items() if y == count]
    print(f"#{test_case} {max(key)}")
