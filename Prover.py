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
        p1 = np.dot(r_xi,gamma)
        prod1 = np.dot(p1,d_i)
        p2 = np.dot(s_xi, gamma)
        prod2 = np.dot(p2, d_i)
        p3 = c_i - np.dot(paramsG["v"],r_xi) - np.dot(paramsG["w"],s_xi)
        prod3 = np.dot(p3,gamma)
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

        PivH = prod1 + np.dot(alpha,paramsH["v"]) + np.dot(beta, paramsH["w"])
        PiwH = prod2 + np.dot(teta, paramsH["v"]) + np.dot(delta, paramsH["w"])
        PivG = np.dot(prod3,r_yi) -  np.dot(paramsG["v"], alpha) - np.dot(paramsG["w"],teta)
        PiwG = np.dot(prod3,s_yi) -  np.dot(paramsG["v"], beta) - np.dot(paramsG["w"],delta)
        proof = [PivH, PiwH, PivG, PiwG]
        return proof
