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
com = CommAlgH(group)
x = group.random(G2)

c = com.pub(x)
print("pub " + str(c))
c = com.enc(x)
print("enc " + str(c))
c = com.com(x)
print("com " + str(c))
c = com.base()
print("base " + str(c))
c = com.sca(x)
print("sca " + str(c))
c = com.unit()
print("unit " + str(c))






