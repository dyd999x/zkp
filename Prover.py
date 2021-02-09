from charm.toolbox.pairinggroup import ZR,G1,G2,PairingGroup
from commit import commit
import numpy as np


def prove(T,gamma,types1,c_i,r_xi,s_xi,types2,d_i,r_yi,s_yi,paramsG,paramsH) :
    (m,n)=gamma.shape
    # C = np.array(c_i)
    # D = np.array(d_i)
    group = PairingGroup("MNT159")
    if (m== len(types1) and n==len(types2)):

        alpha = 0
        beta= 0
        teta= 0
        delta= 0
        p1 = np.dot(r_xi,gamma) #r is from ZR
        prod1 = d_i ** p1
        p2 = np.dot(s_xi, gamma)
        prod2 = d_i ** p2
        v_r =(paramsG["v"]** (-r_xi[0])) *(paramsG["v"] ** (-r_xi[1]))
        w_s = (paramsG["w"]** (-s_xi[0])) *(paramsG["w"] ** (-s_xi[1]))
        c_vr =[]
        p3 = []
        for ci in c_i:
            c_vr.append(ci[0] * v_r + ci[1]*v_r)
        for ci in c_vr:
            p3.append(ci*w_s)
        prod3 = p3 ** gamma

        if (T=='PPE') :
            alpha = group.random(ZR)
            beta = group.random(ZR)
            teta = group.random(ZR)
            delta = group.random(ZR)

        elif (T in {'PEncG','MEH'}) :
            alpha = group.random(ZR)
            beta = group.random(ZR)

        elif (T in {'PEncH','MEG'}) :
            alpha = group.random(ZR)
            teta = group.random(ZR)

        elif (T in {'MEncG', 'MEncH','QE'}):
            alpha = group.random(ZR)

        PivH = prod1 * (paramsH["v"]**alpha) * (paramsH["w"]**beta)
        PiwH = prod2 * (paramsH["v"]**teta) * (paramsH["w"]**delta)
        PivG =(prod3 ** r_yi) / (paramsG["v"] ** alpha) / (paramsG["w"] ** teta)
        PiwG = (prod3 ** s_yi) /  (paramsG["v"] **beta) / (paramsG["w"] **delta)
        proof = [PivH, PiwH, PivG, PiwG]
        return proof

