def loop(dump, b_list):
    for i in range(dump):
        n_min = min(b_list)
        n_max = max(b_list)
        
        count = n_max - n_min
        if count < 2: 
            return count
        else:
        	b_list[b_list.index(n_min)] = n_min +1
        	b_list[b_list.index(n_max)] = n_max -1
        
    return max(b_list)-min(b_list) 

for i in range(10):
    dump = int(input())
    b_list = list(map(int,input().split()))
    print(f"#{i+1} {loop(dump, b_list)}")
            
    
    
    