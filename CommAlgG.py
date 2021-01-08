from charm.toolbox.pairinggroup import ZR,G1,G2
import numpy as np


class CommAlgG:
    def __init__(self, group):
        self.group = group

    def gen(self):
        zero_g = self.group.random(G1) ** 0
        v, w, u = self.group.random(G1), self.group.random(G1), self.group.random(G1)
        while v == zero_g or w == zero_g or u == zero_g:
            v, w, u = self.group.random(G1), self.group.random(G1), self.group.random(G1)

        params = {
            "v": v,
            "u": u,
            "w": w,
        }
        return params


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
        params = self.gen()
        v = params["v"]
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
        params = self.gen()
        e_x = (x ** 0, x)
        v = params["v"]
        w = params["w"]
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
        g = self.group.random(G1)
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
        params = self.gen()
        u = params["u"]
        v = params["v"]
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
        params = self.gen()
        r = 0
        s = 0
        c = params["u"]
        result = {
            "c": c,
            "r": r,
            "s": s,

        }
        return result