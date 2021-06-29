def forward_dyn_prog(v_R,v_L,C_occ):
    #v_R: epipolar vector of the right image
    #v_L: epipolar vector of the left image
    #C_occ: occlusion cost
    m=len(v_R)
    d=np.zeros([m,m]) 
    # decision matrix (used in back-propagation, where it's encoded as 0,1 or 2 refereeing to match, right occlusion and left occlusion respectively.
    c=np.zeros([m,m]) 
    # cost matrix
    
    # Initializing matrices at (0,0)
    c_match= matching_cost(v_L[0],v_R[0])
    c_occ_r= C_occ
    c_occ_l= C_occ

    c_min = min(c_match,c_occ_r,c_occ_l)
    c[0,0] = c_min
    if c_min == c_match:
        d[0,0]= 0
    else:
        d[0,0]= 1 # (or 2 it doesn't matter)
         
    # Initializing first column
    for i in range(1,m):
        c_match= matching_cost(v_L[i],v_R[0])
        c_occ_r= C_occ + c[i-1,0]
        c_occ_l= C_occ 

        c_min = min(c_match,c_occ_r,c_occ_l)
        c[i,0] = c_min

        if c_min == c_match:
            d[i,0]= 0
        elif c_min == c_occ_r:
            d[i,0]= 1
        else:
            d[i,0]= 2
            
    # Initializing first row
    for i in range(1,m):
        c_match= matching_cost(v_L[0],v_R[i])
        c_occ_r=  C_occ  
        c_occ_l=  C_occ +c [0,i-1]

        c_min = min(c_match,c_occ_r,c_occ_l)
        #print(c_min,c_match,i,j)
        c[0,i]= c_min
        if c_min == c_match:
            d[0,i]= 0
        elif c_min == c_occ_r:
            d[0,i]= 1
        else:
            d[0,i]= 2
    # DP implementation for stereo matching        
    for i in range(1,m):
        for j in range(1,m):
            c_match= c[i-1,j-1] + 
                    matching_cost(v_L[i],v_R[j])
                    
            c_occ_r= c[i-1,j] + C_occ
            c_occ_l= c[i,j-1] + C_occ

            c_min = min(c_match,c_occ_r,c_occ_l)
            c[i,j] = c_min

            if c_min == c_match:
                d[i,j]= 0

            elif c_min == c_occ_r:
                d[i,j]= 1
            else:
                d[i,j]= 2
    return d