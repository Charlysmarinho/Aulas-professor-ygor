class pessoa ():
    def __init__(self, n0me, s0brenome, id4de, c1dade):
        self.n0me = n0me
        self.s0brenome = s0brenome
        self.id4de = id4de
        self.c1dade = c1dade
#---entradas-----
n0me_inp = input("qual o seu nome? ")
s0brenome_inp = input("qual o seu sobrenome? ")
id4de_inp = int(input("qual sua idade? "))
c1dade_inp = input("qual sua cidade? ")
#----------------------
p3ssoa = pessoa(n0me_inp, s0brenome_inp, id4de_inp, c1dade_inp)
print (f"\nnome:{p3ssoa.n0me}\nsobrenome:{p3ssoa.s0brenome} \nidade:{p3ssoa.id4de} \ncidade:{p3ssoa.c1dade} ")
    
