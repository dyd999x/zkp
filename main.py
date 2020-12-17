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
# print("pub " + str(c))
# c = com.enc(x)
# print("enc " + str(c))
# c = com.com(x)
# print("com " + str(c))
# c = com.base()
# print("base " + str(c))
# c = com.sca(x)
# print("sca " + str(c))
# c = com.unit()
# print("unit " + str(c))

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
def checkFormat (t1,x,t2,y) :
    if(t1[0]==1) and (t2[0]==2) :
        if (t1[1] in ['base','pub','enc','com'] and t2[1] in ['base','pub','enc','com'] ) :
            return ('PPE')
        elif (t1[1] in ['base','pub','enc'] and t2[1] in ['base','com'] ) :
            return ('PEncG')
        elif (t1[1] in ['base','pub'] and t2[1] in ['base','com'] ) :
            return ('PConstG')
        elif (t1[1] in ['base','com'] and t2[1] in ['base','pub','enc'] ) :
            return ('PEncH')
        elif (t1[1] in ['base','com'] and t2[1] in ['base','pub'] ) :
            return ('PConstH')
        elif (t1[1] in ['base','pub','enc','com'] and t2[1] in ['unit','sca'] ) :
            return ('MEG')
        elif (t1[1] in ['base','pub','enc'] and t2[1] in ['unit','sca'] ) :
            return ('MEncG')
        elif (t1[1] in ['base','pub'] and t2[1] in ['unit','sca'] ) :
            return ('MConstG')
        elif (t1[1] in ['base','com'] and t2[1] in ['unit'] ) :
            return ('MLinG')
        elif (t1[1] in ['unit','sca'] and t2[1] in ['base','pub','enc','com'] ) :
            return ('MEH')
        elif (t1[1] in ['unit','sca'] and t2[1] in ['base','pub','enc'] ) :
            return ('MEncH')
        elif (t1[1] in ['unit','sca'] and t2[1] in ['base','pub'] ) :
            return ('MConstH')
        elif (t1[1] in ['unit'] and t2[1] in ['base','com'] ) :
            return ('MLinH')
        elif (t1[1] in ['unit','sca'] and t2[1] in ['unit','sca'] ) :
            return ('QE')
        elif (t1[1] in ['unit'] and t2[1] in ['unit','sca'] ) :
            return ('QConstG')
        elif (t1[1] in ['unit','sca'] and t2[1] in ['unit'] ) :
            return ('QConstH')




y1= commit((1,'com'),x)
y2= checkFormat((1,'enc'),x,(2,'base'),y)
print(str(y1))
print(str(y2))






