
from CheckFormat import checkFormat
import numpy as np
from charm.toolbox.pairinggroup import ZR,G1,G2,GT,PairingGroup, pair


def verify(T, gamma, types1,c, types2,d, proof, paramsG, paramsH,gr):
    C = c
    D = d


    p1 = proof[0]
    p2 = proof[1]
    p3 = proof[2]
    p4 = proof[3]

    vG = paramsG["v"]
    wG = paramsG["w"]
    vH = paramsH["v"]
    wH = paramsH["w"]


    vGp1 = gr.pair_prod(vG,p1[0])
    wGp2 = gr.pair_prod(wG,p2[0])
    p3vH = gr.pair_prod(p3[0][0],vH)
    p4wH = gr.pair_prod(p4[0][0],wH)
    # print(vGp1)
    # print(wGp2)
    # print(p3vH)
    # print(p4wH)
    sum2 = vGp1 * wGp2 * p3vH * p4wH
    print(sum2)

    Cgamma = C ** gamma
    pairings = []
    sum1 = 1
    for i in Cgamma:
        for j in list(range(2)):
            p = gr.pair_prod(i[j],D[0])
            pairings.append(p)
            sum1 = sum1 * p
    print(sum1)

    if checkFormat(T, gamma, types1, types2):
        if sum1 == sum2:
            return 1
    return 0









