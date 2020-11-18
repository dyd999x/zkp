from charm.schemes.pkenc.pkenc_elgamal85 import ElGamal
import charm.toolbox.eccurve as ec
import charm.toolbox.ecgroup as eg
# import prime192v1
from charm.toolbox.ecgroup import ECGroup
import charm.toolbox.pairingcurves as pc
from charm.toolbox.pairinggroup import PairingGroup,ZR,G1,G2,GT,pair
from charm.core.math.pairing import pairing
import numpy as np


def gen_nonzero():
    cxi, phi = group.random(ZR,1), group.random(ZR,1)
    while int(cxi) == 0 | int(phi) ==0:
        cxi, phi = group.random(ZR,1), group.random(ZR,1)
    return cxi,phi

group = PairingGroup("MNT159")  # Way to limit order of this Group.

print(group.groupSetting().__str__())

ro, sigma = group.random(ZR,1), group.random(ZR,1)
cxi, phi = gen_nonzero()

g = group.random(G1)
h = group.random(G2)
z = group.random(GT)

e=(0,1)
v1= (cxi*g,g)
v1= np.array(v1).T

v2 = (phi*h,h)
v2 = np.array(v2).T

w1 = np.dot(ro,v1)
print(w1)

# print(h)
# print(z)
# print(v)






