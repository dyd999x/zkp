import sys

from charm.schemes.pkenc.pkenc_elgamal85 import ElGamal
import charm.toolbox.eccurve as ec
import charm.toolbox.ecgroup as eg
# import prime192v1
from charm.toolbox.ecgroup import ECGroup
import charm.toolbox.pairingcurves as pc
from charm.toolbox.pairinggroup import ZR,G1,G2,PairingGroup
import numpy as np
from CommAlgG import CommAlgG
from CommAlgH import CommAlgH


group = PairingGroup("MNT159")
comH = CommAlgH(group)
comG= CommAlgG(group)
p = comG.getParams()
print(p)
# y = group.random(G2)
# x= group.random(G1)
# gamma = np.arange(12).reshape(2, 6)








# y1= commit((1,'com'),x)
# y2= checkFormat((1,'enc'),x,(2,'base'),y)
# print(str(y1))
# print(str(y2))
#
# v_1 = group.random(G1)
# v_2 = group.random(G1)
# v = np.array((v_1, v_2)).T
# r =group.random(ZR)
# e_x = (x ** 0, x)
# res = v ** r
# c = np.dot(e_x,res)

#print(c)





