

def commit(t,x):

    gr = t[0]
    types = t[1]
    commitments = []
    for i in range(len(x)):
        if(gr == 1) :
            if(types[i]=='pub') :
               res = comG.pub(x[i])
               commitments += res
            elif (types[i]=='enc') :
                res =comG.enc(x[i])
                commitments += res
            elif(types[i]=='com') :
                res = comG.com(x[i])
                commitments += res
            elif(types[i]=='base') :
                 res =comG.base()
                 commitments += res
            elif(types[i]=='sca') :
                res =comG.sca(x[i])
                commitments += res
            elif(types[i]=='unit') :
                res =comG.unit()
                commitments += res
        elif(gr==2):
            if (types[i] == 'pub'):
                res =comH.pub(x[i])
                commitments += res
            elif (types[i] == 'enc'):
                res =comH.enc(x[i])
                commitments += res
            elif (types[i] == 'com'):
                res =comH.com(x[i])
                commitments += res
            elif (types[i] == 'base'):
                res =comH.base()
                commitments += res
            elif (types[i] == 'sca'):
                res =comH.sca(x[i])
                commitments += res
            elif (types[i] == 'unit'):
                res =comH.unit()
                commitments += res