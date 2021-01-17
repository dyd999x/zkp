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
from CheckFormat import checkFormat



def commit(t,x):
    gr = t[0]
    types = t[1]
    commitments = []
    for i in range(len(types)):
        if(gr == 1) :
            if(types[i]=='pub') :
               res = comG.pub(x[i])
               commitments.append(res)
            elif (types[i]=='enc') :
                res =comG.enc(x[i])
                commitments.append(res)
            elif(types[i]=='com') :
                res = comG.com(x[i])
                commitments.append(res)
            elif(types[i]=='base') :
                 res =comG.base()
                 commitments.append(res)
            elif(types[i]=='sca') :
                res =comG.sca(x[i])
                commitments.append(res)
            elif(types[i]=='unit') :
                res =comG.unit()
                commitments.append(res)
        elif(gr==2):
            if (types[i] == 'pub'):
                res =comH.pub(x[i])
                commitments.append(res)
            elif (types[i] == 'enc'):
                res =comH.enc(x[i])
                commitments.append(res)
            elif (types[i] == 'com'):
                res =comH.com(x[i])
                commitments.append(res)
            elif (types[i] == 'base'):
                res =comH.base()
                commitments.append(res)
            elif (types[i] == 'sca'):
                res =comH.sca(x[i])
                commitments.append(res)
            elif (types[i] == 'unit'):
                res =comH.unit()
                commitments.append(res)
    return commitments


group = PairingGroup("MNT159")
comH = CommAlgH(group)
comG= CommAlgG(group)

g = group.random(G1)
s = group.random(ZR)
x = g ** s
T = 'MEG'
types1 = ['pub','com']
types2=['unit']
t1=[1]
t2=[2]
t1.append(types1)
t2.append(types2)
elemG = [x,s]

print(t1[1])
gamma= np.array([[1, -1]]).T

resultG = commit(t1,elemG)
resultH = commit(t2,[])
print(resultH)
print(resultG)

print(checkFormat(T,gamma,types1,types2))
print(x)
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





