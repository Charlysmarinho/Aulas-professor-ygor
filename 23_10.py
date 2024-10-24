print ("--------MENU----------")
s3lec_menu = int(input("qual exercício deseja executar?"))

if s3lec_menu == 1:
    #dados_basicos_do usuario
    n0me = input("qual o seu nome? ")
    s0brenome = input("qual o seu sobrenome? ")
    id4de = int(input("qual a sua idade? "))
    c1dade = input("qual sua cidade? ")

    li5ta_dados = [n0me, s0brenome, id4de, c1dade]
    #menu02_lista_meses
    print(li5ta_dados)
elif s3lec_menu == 2:
    l1sta_mes = ['janeiro', 'fevereiro' , 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    num3ro= int(input("digite um numero de 1 a 12: "))
    print(f"o mês correspondente ao número {num3ro} é:", l1sta_mes[int(num3ro)-1])

else:
    print ("'pane no sistema alguem me desconfigurou'")

