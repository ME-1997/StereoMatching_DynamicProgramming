def pipe_line(img_R,img_L,C_occ):
#img_R: Right image
#img_L: Left image
#C_occ: Occlusion cost

    #number of rows
    m=img_R.shape[0]
    
    #disparity map of right image
    disp= np.zeros_like(img_R)

#for each row of both images
    for i in range(m):
        v_R=img_R[i,:]
        v_L=img_L[i,:]
        
        #obtain decision matrix
        d = forward_dyn_prog(v_R,v_L,C_occ)

        #obtain disparity of right image's row
        disp[i,:] = backward_dyn_prog(d)

    return disp