for i in range(10) :
    T = int(input())
    n_list = []
    n_max = 0
    for j in range(100):
        m_list = list(map(int, input().split()))
        m_max = sum(m_list)
        if n_max < m_max: 
            n_max = m_max
            
        n_list.append(m_list)
        
    for j in range(100): 
        m_max = sum(list(x[j] for x in n_list))
        if n_max < m_max: 
            n_max = m_max
    m_max = sum(list(n_list[j][j] for j in range(100)))
    if n_max < m_max :
    	n_max = m_max
    m_max = sum(list(n_list[j][99-j] for j in range(100)))
    if n_max < m_max :
    	n_max = m_max
        

    
    print(f'#{i+1} {n_max}') 