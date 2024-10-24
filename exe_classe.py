class pessoa ():
    def __init__(self, n0me, s0brenome, id4de, c1dade):
        self.n0me = n0me
        self.s0brenome = s0brenome
        self.id4de = id4de
        self.c1dade = c1dade
n0me = pessoa(input("qual o seu nome? "))
s0brenome = pessoa(input("qual o seu sobrenome? "))
id4de = pessoa(int(input("qual sua idade? ")))
c1dade = pessoa(input("qual sua cidade? "))
print (f"\nnome:{pessoa.n0me},\nsobrenome:{pessoa.s0brenome}, \nidade:{pessoa.id4de}, cidade:{pessoa.c1dade} ")



    