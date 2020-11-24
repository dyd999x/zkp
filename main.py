from charm.schemes.pkenc.pkenc_elgamal85 import ElGamal
import charm.toolbox.eccurve as ec
import charm.toolbox.ecgroup as eg
# import prime192v1
from charm.toolbox.ecgroup import ECGroup
import charm.toolbox.pairingcurves as pc
from charm.toolbox.pairinggroup import PairingGroup,ZR,G1,G2,GT,pair
from charm.core.math.pairing import pairing
import numpy as np

def ext_gen(gr):
    g = gr.random(G1)
    h= gr.random(G2)
    zero_g = g ** 0
    zero_h = h ** 0
    ro, cxi = gr.random(G1), gr.random(G1)
    sigma, phi = gr.random(G2), gr.random(G2)
    while cxi == zero_g or phi == zero_h:
        cxi, phi = gr.random(G1), gr.random(G2)
    v1 = (g*cxi, g)
    v1 = np.array(v1).T
    w1 = np.dot(ro,v1)
    v2 = (h*phi,h)
    w2 = np.dot(sigma,v2)
    aux1 = (zero_g, g)
    u1 = w1 * np.array(aux1).T
    aux2 = (zero_h,h)
    u2 = w2 * np.array(aux2).T
    return v1,w1,u1,v2,w2,u2


group = PairingGroup("MNT159")  # Way to limit order of this Group.

v1,w1,u1,v2,w2,u2 = ext_gen(group)
print(v1)
print(w1)
print(u1)
print(v2)
print(w2)
print(u2)

# g = group.random(G1)
# h = group.random(G2)
# z = group.random(GT)
# print(group.groupSetting())
# print(GT)
#
# e=(0,1)
# v1= (cxi*g,g)
# v1= np.array(v1).T
# w1 = np.dot(ro,v1)
#
# zero = g**0
# print(type(zero))
# aux = (zero,g)
# u1 = w1 * np.array(aux).T
# print(u1)
#
# v2 = (phi*h,h)
# v2 = np.array(v2).T
# w2 = np.dot(sigma, v2)


# print(h)
# print(z)
# print(v)






