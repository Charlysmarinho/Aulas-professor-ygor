class carro:
    def __init__(self,m4rca,m0delo,an0,c0r):
        self.m4rca = m4rca
        self.m0delo = m0delo
        self.an0 = an0
        self.c0r = c0r
    
        def s4ida_carro(self):
            print (f"\nmarca:{self.m4rca}\nmodelo:{self.m0delo}\nano:{self.an0}\ncor:{self.c0r}")

c4rro = carro (input("marca: "), input("modelo: "), input("ano: "), input("cor: "))   

c4rro.s4ida_carro
        