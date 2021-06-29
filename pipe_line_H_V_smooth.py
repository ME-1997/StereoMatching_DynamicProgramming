
    def pipe_line(img_R,img_L,C_occ):
#img_R: Right image
#img_L: Left image
#C_occ: Occlusion cost

    #number of rows
    m=img_R.shape[0]
    #disparity map of right image
    disp= np.zeros_like(img_R)

    #temporary variable contains the solution of the previous scan-line
    temp=np.zeros(img_R.shape[1])
    
    #variable to indicate the first scan-line
    init=0
#for each row of both images
    for i in range(m):
        v_R=img_R[i,:]
        v_L=img_L[i,:]
        
        #obtain decision matrices
        D_d,D_h,D_v = 
          forward_dyn_prog_H_V(v_R,v_L,C_occ,temp,init)

        #obtain disparity of right image's row
        disp[i,:] =
          backward_dyn_prog_H_V(D_d,D_h,D_v)

    return disp
