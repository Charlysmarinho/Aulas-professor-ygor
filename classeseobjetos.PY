##--ESCOLA_DO_FUTURO----------|
#--PROGRAMAÇÃO_ORIE_OBJETOS---|
#-CHARLYS_HENRIQUE_TURMA:_N1__|
#-------25_10_24--------------|

class pessoinha:
    def __init__(self,n4me,n4me2,id4de,c1dade):
        self.n4me = n4me
        self.n4me2 = n4me2
        self.id4de = id4de
        self.c1dade = c1dade
    def inf0rmacao_saida(self):
        print (f"ola meu nome é {self.n4me},meu sobrenome é {self.n4me2} , e eu tenho {self.id4de}, sou de {self.c1dade} ")
pessoinha1 = pessoinha(input('\nqual seu nome?'), input("\nqual seu sobrenome? "), input("\nqual sua idade? "), input("\nqual sua cidade? ") )

pessoinha1.inf0rmacao_saida() 

