from charm.toolbox.pairinggroup import ZR,G1,G2
import numpy as np


class CommAlgH:
    def __init__(self, group):
        self.group = group
        zero_h = self.group.random(G2) ** 0
        v, w, u = self.group.random(G2), self.group.random(G2), self.group.random(G2)
        while v == zero_h or w == zero_h or u == zero_h:
            v, w, u = self.group.random(G2), self.group.random(G2), self.group.random(G2)

        self.params = {
            "v": v,
            "w": w,
            "u": u,
        }



    def pub(self, x):
        c = (x**0, x)
        r = 0
        s = 0
        result = {
            "c": c,
            "r": r,
            "s": s,

        }
        return result

    def enc(self,x):
        r = self.group.random(ZR)
        s = 0
        e_x = (x ** 0, x)
        v = self.params["v"]
        v_r = v ** r
        c = np.dot(e_x,v_r)
        result = {
            "c": c,
            "r": r,
            "s": s,

        }
        return result


    def com(self,x):
            r = self.group.random(ZR)
            s = self.group.random(ZR)
            e_x = (x ** 0, x)
            v = self.params["v"]
            w = self.params["w"]
            v_r = v ** r
            w_s = w ** s
            c1 = np.dot(e_x,v_r)
            c = np.dot(c1, w_s)
            result = {
                "c": c,
                "r": r,
                "s": s,

            }
            return result

    def base(self):
        g = self.group.random(G2)
        r = 0
        s = 0
        c = (g ** 0, g)
        result = {
            "c": c,
            "r": r,
            "s": s,

        }
        return result

    def sca(self,x):
        r = self.group.random(ZR)
        s = 0
        u = self.params["u"]
        v = self.params["v"]
        x_u = np.dot(x, u)
        v_r = v ** r
        c = np.dot(x_u,v_r)
        result = {
            "c": c,
            "r": r,
            "s": s,

        }
        return result

    def unit(self):
        r = 0
        s = 0
        c = self.params["u"]
        result = {
            "c": c,
            "r": r,
            "s": s,

        }
        return result


    def getParams(self):
        return self.params


