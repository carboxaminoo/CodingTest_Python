def c_month(m):
    return True if 0 < m < 13 else False
def c_day(m,d):
    odd = [1,3,5,7,8,10,12]
    even = [4,6,9,11]
    
    if m in odd :
        return True if 0<d<32 else False
    elif m in even :
        return True if 0<d<31 else False
    else:
        return True if 0<d<29 else False

T = int(input())
for i in range(T):
    date = input()
    y = date[:4]
    m = int(date[4:6])
    d = int(date[6:])
    
    if c_month(m) and c_day(m,d) :
        str_date = f'{y}/{date[4:6]}/{date[6:]}'
        print(f'#{i+1} {str_date}')
    else:
        print(f'#{i+1} -1')