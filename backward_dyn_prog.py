def backward_dyn_prog(d):
#d: decision map
    i=d.shape[0]-1
    j=i
    #disparity map of the right image
    match=np.zeros(i+1)
    while(i != 0 and j != 0):
        idx=d[i,j]
        #if decision at (i,j) is diagonal path
        if idx==0:
            match[i]=np.absolute(i-j)
            i=i-1
            j=j-1
            continue
        #if decision at (i,j) is horizontal path
        if idx==1:
            i=i-1
            continue
        #if decision at (i,j) is vertical path    
        if idx==2:
            j=j-1
            continue
    return match
\end{lstlisting}

    \begin{lstlisting}[language=Python, caption=Python implementation stereo-matching using dynamic programming]
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