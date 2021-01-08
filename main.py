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
y = group.random(G2)
x= group.random(G1)
gamma = np.arange(12).reshape(2, 6)

def commit(t,m):
    if(t[0]==1) :
        if(t[1]=='pub') :
            return comG.pub(m)
        elif (t[1]=='enc') :
            return comG.enc(m)
        elif(t[1]=='com') :
                return comG.com(m)
        elif(t[1]=='base') :
                return comG.base()
        elif(t[1]=='sca') :
            return comG.sca(m)
        elif(t[1]=='unit') :
            return comG.unit()
    elif(t[0]==2) :
        if (t[1] == 'pub'):
            return comH.pub(m)
        elif (t[1] == 'enc'):
            return comH.enc(m)
        elif (t[1] == 'com'):
            return comH.com(m)
        elif (t[1] == 'base'):
            return comH.base()
        elif (t[1] == 'sca'):
            return comH.sca(m)
        elif (t[1] == 'unit'):
            return comH.unit()





# y1= commit((1,'com'),x)
# y2= checkFormat((1,'enc'),x,(2,'base'),y)
# print(str(y1))
# print(str(y2))

v_1 = group.random(G1)
v_2 = group.random(G1)
v = np.array((v_1, v_2)).T
r =group.random(ZR)
e_x = (x ** 0, x)
res = v ** r
c = np.dot(e_x,res)

#print(c)

res = comG.enc(x)
print(res["s"])

print("***************************************")







