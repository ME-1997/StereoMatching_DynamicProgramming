def backward_dyn_prog_H_V(D_d,D_h,D_v):
    
    i=D_d.shape[0]-1
    j=D_d.shape[1]-1
    
    match=np.zeros(i+1)
    state=np.zeros(i+1)

    
    idx=np.argmin([D_d[i,j],D_h[i,j],D_v[i,j]])
    
    if idx==0:
        p=1
        q=1
        match[i]=np.absolute(i-j)
        state[i]=1
        d1=0
        d2=1
        d3=1
        
        
        
        
    if idx==1:
        
        state[i]=2

        p=1
        q=0
        
        d1=1
        d2=0
        d3=1
        
        
    
    if idx==2:
        state[i]=3

        p=0
        q=1
        
        d1=1
        d2=1
        d3=0
        
    
    
    while(i != 0 and j != 0):
        
        idx=np.argmin([ D_d[i-p,j-q]+d1 ,D_h[i-p,j-q]+d2,D_v[i-p,j-q]+d3])
    
        if idx==0:
            state[i]=1

            match[i]=np.absolute(i-j)
            
            i=i-p
            j=j-q
            
            p=1
            q=1
            
            d1=0
            d2=1
            d3=1
            continue



        if idx==1:
            state[i]=2
            i=i-p
            j=j-q
            
            p=1
            q=0
            
            d1=1
            d2=0
            d3=1
            continue



        if idx==2:
            state[i]=3
            i=i-p
            j=j-q
            
            p=0
            q=1
            
            d1=1
            d2=1
            d3=0
            continue
            
            
    return match , state