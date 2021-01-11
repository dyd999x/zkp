
from CheckFormat import checkFormat
import numpy as np

def verify(T, gamma, dict1, dict2, proof, paramsG, paramsH):
    (m, n) = gamma.shape
    t1 = list(dict1.keys())
    t2 = list(dict2.keys())
    C = np.array(list(dict1.values()))
    D = np.array(list(dict2.values()))
    D = D.T
    (dim1_C, dim2_C) = C.shape
    (dim1_D, dim2_D) = D.shape

    p1 = np.array(proof[1])
    p2 = np.array(proof[2])
    p3 = np.array(proof[3])
    p4 = np.array(proof[4])

    (dim1_p1, dim2_p1) = p1.shape
    (dim1_p2, dim2_p2) = p2.shape
    (dim1_p3, dim2_p3) = p3.shape
    (dim1_p4, dim2_p4) = p4.shape

    vG = paramsG["v"]
    wG = paramsG["w"]
    vH = paramsH["v"]
    wH = paramsH["w"]

    if checkFormat(T, gamma, t1, t2):
        if (dim1_C == 2 and dim2_C == m) and (dim1_D == n and dim2_D == 2):
            if dim1_p1 ==2 and dim2_p1 == 1 and dim1_p2 == 2 and dim2_p2 == 1 and dim1_p3 == 1 and dim2_p3 == 2 and dim1_p4 == 1 and dim2_p4 == 2:
                C_gamma = np.dot(C,gamma)
                CgammaD = np.dot(C_gamma,D)
                aux = np.dot(vG,proof[1]) + np.dot(wG,proof[2]) + np.dot(proof[3],vH) + np.dot(proof[4], wH)
                if aux == CgammaD:
                    return 1

    return 0









