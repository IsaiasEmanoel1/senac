from time import sleep
from aux_func import *

class Tele_Email_Endere:
    def __init__(self,telefone,email,rua,numero,bairro,cidade,cep):
        self.telefone = telefone
        self.email = email
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.cep = cep

    def cadastro_tele_email():
        desenha_tela(tela="telefone e email", altura= 2, largura= 36)
        telefone2 = "NULL"
        email2 = "NULL"
        telefone = input("Telefone do funcionario: ")
        print("O funcionario tem outro numero? ", "1- Sim", "2- Não", sep="\n")
        p_telefone = int(input("Digite o codigo: "))
        if p_telefone == 1:
           telefone2 =  input("Telefone do funcionario: ")
           email = input("Email do Funcionario: ")
           print("O funcionario tem outro email? ", "1- Sim", "2- Não", sep="\n")
           p_email = int(input("Digite o codigo: "))
           if p_email == 1:
            email2 =  input("Email do funcionario: ")
           elif p_email == 2:
            pass
        
        elif p_telefone == 2:
            email = input("Email do Funcionario: ")
            print("O funcionario tem outro email? ", "1- Sim", "2- Não", sep="\n")
            p_email = int(input("Digite o codigo: "))
            if p_email == 1:
                email2 =  input("Email do funcionario: ")
            elif p_email == 2:
                pass
        else:
            print("Algo de errado!!", "Tente novamente.", sep="\n")
            sleep(2)
            Tele_Email_Endere.cadastro_tele_email()
        return p_telefone, telefone, p_email, telefone2, email, email2

    def cadastra_endere():
        complemento = "NULL"
        desenha_tela(tela="endereço", altura= 2, largura= 24)
        rua = input("Rua: ")
        numero = input("Numero: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        cep = input("CEP: ")
        print(f"Quer adicionar complemento?","1- Sim","2- Não", sep="\n")
        pergunta_comp = int(input("Digite o codigo: "))
        if pergunta_comp == 1:
            complemento = input("Complemento: ")

        elif pergunta_comp == 2:
            pass

        return rua,numero,bairro,cidade,cep,complemento,pergunta_comp
