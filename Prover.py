from charm.toolbox.pairinggroup import ZR,G1,G2
from main import commit



def prove(T,gamma,t1,x,t2,y,paramsG,paramsH) :
    (m,n)=gamma.shape()
    if (m== len(t1) and n==len(t2)):
        resultG = commit(t1,x)
        resultH = commit(t2,y)
        alpha=group.random(ZR)
        beta= group.random(ZR)
        teta=group.random(ZR)
        delta=group.random(ZR)
        if (T=='PPE') :
            PivG= resultG["r"] * gamma * resultH["c"] + alpha * paramsH["v"] + beta * paramsH["w"]
            PivH= (resultG["c"] - paramasG["v"]*resultG["r"] - paramsG["w"]*resultG["s"]) * gamma * resultH["r"] - paramsG["v"]*alpha - paramasG["w"]*teta
            PiwG= resultG["s"]*gamma*resultH["c"]+ teta* paramsH["v"] + delta*paramsH["w"]
            PiwH= (resultG["c"]-paramsG[v]*resultG["r"]-paramsG["w"]*resultG["s"])*gamma*resultH["s"]-paramsG["v"]*beta-paramsG["w"]*delta
            proof= (PivG,PiwG,PivH,PiwH)
            return (proof)
        elif (T in {'PEncG','MEH'}) :
            PivG = resultG["r"] * gamma * resultH["c"] + alpha * paramsH["v"] + beta * paramsH["w"]
            PivH = (resultG["c"] - paramasG["v"] * resultG["r"] - paramsG["w"] * resultG["s"]) * gamma * resultH["r"] - paramsG["v"] * alpha
            PiwG = resultG["s"] * gamma * resultH["c"]
            PiwH = (resultG["c"] - paramsG[v] * resultG["r"] - paramsG["w"] * resultG["s"]) * gamma * resultH["s"] - paramsG["v"] * beta
            proof = (PivG, PiwG, PivH, PiwH)
            return (proof)
        elif (T in {'PEncH','MEG'}) :
            PivG = resultG["r"] * gamma * resultH["c"] + alpha * paramsH["v"]
            PivH = (resultG["c"] - paramasG["v"] * resultG["r"] - paramsG["w"] * resultG["s"]) * gamma * resultH["r"] - \
                   paramsG["v"] * alpha - paramasG["w"] * teta
            PiwG = resultG["s"] * gamma * resultH["c"] + teta * paramsH["v"]
            PiwH = (resultG["c"] - paramsG[v] * resultG["r"] - paramsG["w"] * resultG["s"]) * gamma * resultH["s"]
            proof = (PivG, PiwG, PivH, PiwH)
            return (proof)
        elif (T in {'MEncG', 'MEncH','QE'}):
            PivG = resultG["r"] * gamma * resultH["c"] + alpha * paramsH["v"]
            PivH = (resultG["c"] - paramasG["v"] * resultG["r"] - paramsG["w"] * resultG["s"]) * gamma * resultH["r"] - paramsG["v"] * alpha
            PiwG = resultG["s"] * gamma * resultH["c"]
            PiwH = (resultG["c"] - paramsG[v] * resultG["r"] - paramsG["w"] * resultG["s"]) * gamma * resultH["s"]
            proof = (PivG, PiwG, PivH, PiwH)
            return (proof)

