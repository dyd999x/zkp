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