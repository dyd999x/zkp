
from CheckFormat import checkFormat
import numpy as np

def verify(T, gamma, types1,c, types2,d, proof, paramsG, paramsH):
    (m, n) = gamma.shape
    C = np.array(c)
    D = np.array(d)
    D =  np.expand_dims(D,axis = 1)
    D = D.T
    (dim1_C, dim2_C) = C.shape
    (dim1_D, dim2_D) = D.shape

    p1 = np.array(proof[0])
    p2 = np.array(proof[1])
    p3 = np.array(proof[2])
    p4 = np.array(proof[3])

    (dim1_p1, dim2_p1) = p1.shape
    (dim1_p2, dim2_p2) = p2.shape
    (dim1_p3, dim2_p3) = p3.shape
    (dim1_p4, dim2_p4) = p4.shape

    vG = paramsG["v"]
    wG = paramsG["w"]
    vH = paramsH["v"]
    wH = paramsH["w"]



    if checkFormat(T, gamma, types1, types2):
        if (dim1_C == 2 and dim2_C == m) and (dim1_D == n and dim2_D == 2):
            if dim1_p1 ==2 and dim2_p1 == 1 and dim1_p2 == 2 and dim2_p2 == 1 and dim1_p3 == 1 and dim2_p3 == 2 and dim1_p4 == 1 and dim2_p4 == 2:
                C_gamma = np.dot(C,gamma)
                CgammaD = np.dot(C_gamma,D)
                aux = np.dot(vG,proof[1]) + np.dot(wG,proof[2]) + np.dot(proof[3],vH) + np.dot(proof[4], wH)
                if aux == CgammaD:
                    return 1
            else: print("wrong dimm for proof")
        else: print("wrong dimm for c or d")
    else: print("checkformat error")

    return 0









