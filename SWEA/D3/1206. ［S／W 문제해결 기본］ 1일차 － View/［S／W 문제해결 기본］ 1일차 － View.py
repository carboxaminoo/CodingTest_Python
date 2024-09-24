test_case = 0 
while test_case <10 :
    b_num = int(input())
    b_list = [int(i) for i in input().split()]
    count = 0
    for i in range(2,b_num-2):
        b_max = max([b_list[j] for j in range(i-2, i+3)])
        if b_max == b_list[i]:
        	count += b_max - max(b_list[j] for j in [i-2, i-1, i+1, i+2])
            
    test_case += 1
    print(f"#{test_case} {count}")
	