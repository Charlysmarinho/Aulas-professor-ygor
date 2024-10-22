##1.numero_positivo_negativo##
#num3ro_user = float(input("escolha um número: "))
#if num3ro_user >0:
#    print (f'o numero {num3ro_user} é positivo.')
#elif num3ro_user <0:
#    print (f'o número { num3ro_user} é negativo. ')
#else:
#    print ("o número é zero")
#--------------------------------------------------
##2.MAIORIDADE######################
#id4de = int(input("insira sua idade:"))
#if id4de >=18:
#    print (f'idade: {id4de} se lascou, vai preso!')
#else:
#    print (f"idade: {id4de} você é menor de idade, vai so apanhar mesmo.")
#---------------------------------------------------
##3.PAR_OU_IMPAR#### 
#num3ro = int(input("digite um número: "))
#if num3ro%2 == 0:
#    print (f"{num3ro} é par")
#else:
#    print (f"{num3ro}é impar: ")
##--------------------------------------------------
##4.NUMERO_MAIOR################################
#num3_1 = float(input(" digite um número: "))
#num3_2 = float(input(" digite outro número:"))
#if num3_1 > num3_2:
#    print (f"{num3_1} é maior que {num3_2: .2f}.")
#else:
#    print (f"{num3_2}é maior que {num3_1: .2f}.")
##--------------------------------------------
#5.DESCONTO_NA_COMPRA##########################
#v4lor_total = float(input("qual o valor total da sua compra?"))
#d3sconto = v4lor_total*10/100
#if v4lor_total > 100:
#    print (f'você recebeu um desconto de 10% em sua compra, seu novo total é de R$:{v4lor_total-d3sconto: .2f}')
#else: 
#    print (f'Total da sua compra é de R$:{v4lor_total}')
##----------------------------------------------
##6.VERIFICAR_MULTIPLO#################
#numer0 = float(input("digite um número:"))
#if numer0 %5 == 0:
#    print (f'{numer0: .2f} é multiplo de 5.')
#else:
#    print(f'{numer0: .2f} não é multiplo de 5.')
##-----------------------------------------------
##7.CALCULAR_MÉDIA##################
#num3r01 = float(input("insira uma nota: "))
#num3r02 = float(input("insira uma nota: "))
#num3r03 = float(input("insira uma nota: "))
#m3dia = (num3r01 + num3r02 + num3r03)/3
#print (f'a média das sua notas são: {m3dia: .2f}')
##----------------------------------------------------
###8.SENHA_CORRETA####################
#senh4 = input("insira sua senha: ")

#passworld = ("python123_EFG")
#if senh4 == passworld:
#    print ("acesso liberado meu jovem.")
#else:
#    print ("acesso negado meu parceiro.")
##------------------------------------------
##9.ENTRADA_GRATUITA###############
#idad3 = int(input("qual a idade?"))
#if idad3<6 or idad3>60:
#    print (f'parabens você recebeu o nosso passe gratuito ao parque.')
#else:
#    print ("você paga o valor integral do ingresso.")
##----------------------------------------------
##10.VERIFICAR_NOTA    
#n0ta = int(input("atribua uma nota ao nosso servico: "))
#if n0ta >= 0 and n0ta <= 10:
#    print (f"você atribuiu nota: {n0ta}")
#else:
#    print ("erro, atribua uma nota de 0 a 10.")  
##-------------------------------------------------
##11.CATEGORIA_DE_IDADE#################
#id4d3 = int(input('insira sua idade: ')) 

#if id4d3 >= 18:
#    print (f"você é adulto, sua idade é: {id4d3}.")
#elif id4d3 <=12:
#    print (f'você é criança, sua idade é: {id4d3}.')
#elif id4d3 >=13 and id4d3 <=17:
#    print (f'você é um chato geracao z, sua idade é: {id4d3}')
##---------------------------------------------------
##12.MAIOR_NUMERO####
#num3r01 = float(input("digite um número: "))
#num3r02 = float(input("digite um número: "))
#num3r03 = float(input("digite um número: "))

#m4ior = num3r01
#if num3r02 > m4ior:
#    m4ior = num3r02
#if num3r03 > m4ior:
#    m4ior = num3r03

#m3nor = num3r01
#if num3r02<m3nor:
#    m3nor = num3r02
#if num3r03 < m3nor:
#    m3nor = num3r03
#print (f'o maior número é {m4ior}')
#print (f'o menor número é {m3nor}')    
##-------------------------------------------------
##13.DIVISAO_SEGURA###############
#num3r01 = float(input("digite um número: "))
#num3r02 = float(input("digite um número:"))
#if num3r02 == 0:
#    print ('não é possivel dividir por 0(zero), por favor digite um número válido.')   
#div1sao = num3r01/num3r02
#print (f"o resultado da divisão: {num3r01: .2f}/{num3r02: .2f} = {div1sao: .2f}")
##---------------------------------------------------
##14.NUMERO_ENTRE_0_E_50##########
#num3r0 = int(input("digite um número: "))
#if num3r0>= 0 and num3r0 < 50:
#    print (f"o número {num3r0} esta entre 0 e 50.")
#else:
#    print (f"o número {num3r0} não esta entre 0 e 50.")
##-----------------------------------------------------
##15.APROVADO_REPROVADO_RECUPERACAO--------
#n0me = input("insira o nome do aluno: ")
#n0ta1 = float(input("digite a primeira nota: "))
#n0ta2 = float(input("digite a segunda nota: "))
#n0ta3 = float(input("digite a terceira nota: "))
#n0ta4 = float(input("digite a quarta nota: "))

#m3dia = (n0ta1 + n0ta2 + n0ta3 + n0ta4)/4
#n0ta_total = n0ta1 + n0ta2 + n0ta3 + n0ta4

#if m3dia <=50:
#    print (f"olá {n0me}, sua nota total é {n0ta_total: .2f}, sua média é {m3dia: .2f} , você esta reprovado.")
#elif m3dia >=70:
#   print (f"olá {n0me}, sua nota total é {n0ta_total: .2f}, sua média é {m3dia: .2f}, você esta aprovado.")
#elif m3dia > 51 and m3dia< 60:
#    print (f" olá {n0me}, sua nota total é {n0ta_total: .2f}, sua média é {m3dia: .2f}, você esta de recuperação.")
#-----------------------------------------------------------
##16.CALCULAR_IMC-------------------------------------
#p3so = float(input("qual o seu peso? "))
#altur4 = float(input("qual a sua altura?"))
#imc = p3so/(altur4**2)
#print (f"seu imc é: {imc:.2f}" )
#
#if imc<18.5:
#    print ("você esta magro demais!vai treinar seu frango!!")
#elif 18.5<= imc <= 24.9:
#    print ("seu peso esta normal!")
#elif 25<= imc <= 29.9:
#    print (" voce esta com sobrepeso hein!")
#elif 30<= imc <=39.9:
#    print ("voce esta com obesidade tipo 1")
#elif 40<= imc <=100:
#    print ("voce esta gigaenorme meu chapa")
#------------------------------------------------------
##18.LOGIN_E_SENHA
#l0gin = input("USUARIO:")
#s3nha = input("SENHA:")

#senh4 = ("123")
#us3r = ("admin")

#if l0gin == us3r and s3nha == senh4:
#    print ("acesso liberdo, bem vindo")
#else:
#        print ("usuario nao tem permissao de administrador.")
#-----------------------------------------------------------
##19.IDADE_PARA_DIRIGIR:
#id4de = int(input("qual sua idade: "))
#c4lc = 18 - id4de

#if id4de >= 18:
#    print ("você pode dirigir, desde que habilitado.")
#else:
#    print ("você não pode dirigir ainda faltam mais ou menos:", c4lc ,"anos.")
   