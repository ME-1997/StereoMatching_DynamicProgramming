def forward_dyn_prog_H_smooth(v_R,v_L,C_occ):
    m=len(v_R)
    D_d=np.zeros([m,m])
    D_v=np.zeros([m,m])
    D_h=np.zeros([m,m])
    c=np.zeros([m,m])
    
    
    c_match= matching_cost(v_L[0],v_R[0])
    c_occ_r= C_occ
    c_occ_l= C_occ
    
    c_min = min(c_match,c_occ_r,c_occ_l)
    c[0,0] = c_min



    if c_min == c_match:
        D_d[0,0]= 0
        D_v[0,0]=np.inf
        D_h[0,0]=np.inf
    else:
        D_d[0,0]=np.inf
        
    for i in range(1,m):
        c_match= matching_cost(v_L[i],v_R[0])
        c_occ_r= C_occ+ c[i-1,0]
        c_occ_l= C_occ 

        c_min = min(c_match,c_occ_r,c_occ_l)
        c[i,0] = c_min

        if c_min == c_match:
            D_d[i,0]= 0
        else:
            D_d[i,0]= np.inf
            
        if c_min == c_occ_r:
            D_h[i,0]= min(D_d[i-1,0]+1 ,
                                 D_h[i-1,0] ,
                                     D_v[i-1,0]+1)
        else:
            D_h[i,0]= np.inf
            
        if c_min == c_occ_l:
            D_v[i,0]= 0
        else:
            D_v[i,0]= np.inf
            
            
    for i in range(1,m):
        c_match= matching_cost(v_L[0],v_R[i])
        c_occ_r=  C_occ  
        c_occ_l=  C_occ + c[0,i-1]

        c_min = min(c_match,c_occ_r,c_occ_l)
        c[0,i]= c_min

        if c_min == c_match:
            D_d[0,i]= 0
        else:
            D_d[0,i]= np.inf
            
        if c_min == c_occ_r:
            D_h[0,i]= 0
        else:
            D_h[0,i]= np.inf
    
        if c_min == c_occ_l:
            D_v[0,i]= min(D_d[0,i-1]+1 ,
                                D_h[0,i-1]+1 ,
                                      D_v[0,i-1])
        else:
            D_v[0,i]= np.inf

    for i in range(1,m):
        for j in range(1,m):
            
            c_match=c[i-1,j-1] +
                     matching_cost(v_L[i],v_R[j])
                     
            c_occ_r= c[i-1,j]   + C_occ
            c_occ_l= c[i,j-1]   + C_occ

            c_min = min(c_match,c_occ_r,c_occ_l)
            c[i,j] = c_min

            if c_min == c_match:
                D_d[i,j]= min(D_d[i-1,j-1] ,
                               D_h[i-1,j-1]+1 ,
                                D_v[i-1,j-1]+1)
            else:
                D_d[i,j]= np.inf



            if c_min == c_occ_r:
                D_h[i,j]= min(D_d[i-1,j]+1 ,
                               D_h[i-1,j] ,
                                D_v[i-1,j]+1)
            else:
                D_h[i,j]= np.inf

            if c_min == c_occ_l:
                D_v[i,j]= min(D_d[i,j-1]+1 ,
                               D_h[i,j-1]+1 ,
                                D_v[i,j-1])
            else:
                D_v[i,j]= np.inf
            
    return D_d,D_h,D_v