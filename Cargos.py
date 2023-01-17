from aux_func import *
from Solicitacao import Solicitacao
from connector import conn
from time import sleep
import os

class Cargos():
    def __init__(self, nome_cargo):
        self.nome_cargo = nome_cargo

    def cadastro():
        prova = 0
        while prova == 0:
            mydb = conn()
            Solicitacao.solicita_dados_cargo()
            nome_cargo = input(f"Digite o nome do cargo que deseja cadastrar \nou digite 0 para sair: ")
            mycursor = mydb.cursor()
            verificar = (f"SELECT COUNT(cargo) FROM cargo where cargo = '{nome_cargo.lower()}'")
            mycursor.execute(verificar)
            resultado = mycursor.fetchall()

            if nome_cargo == '0':
                prova = 1

            elif resultado[0][0] == 0:
                sql = (f"INSERT INTO cargo(cargo, status) VALUES ('{nome_cargo.lower()}', 1)")
                mycursor = mydb.cursor()
                mycursor.execute(sql)
                mydb.commit()
                print(GREEN +"O cargo foi adicionado!!!"+ RESET)
                mydb.close()
                prova = 1

            else:
                print(RED+"CARGO EXISTENTE"+RESET)
                sleep(1.5)
                os.system("cls")

    def atualiza():
        prova = 0
        while prova == 0:
            Solicitacao.solicita_dados_cargo()
            pergunta = int(input(f"Informe o código do cargo que deseja modificar \n ou digite 0 para sair: "))
            mydb = conn()
            mycursor = mydb.cursor()
            verificar = (f"SELECT COUNT(cargo) from cargo where codigo='{pergunta}'")
            mycursor.execute(verificar)
            resultado = mycursor.fetchall()

            if pergunta == 0:
                prova = 1

            elif resultado[0][0] == 1:
                pergunta2 = input("Novo nome do cargo: ")
                update = (f"UPDATE cargo SET cargo = '{pergunta2}' where codigo='{pergunta}'")
                mycursor.execute(update)
                mydb.commit()
                print(GREEN +"O cargo foi atualizado!!!"+ RESET)
                mydb.close()
                prova = 1

            else:
                print(RED+"CODIGO INCORRETO"+RESET)
                sleep(1.5)
                os.system("cls")

    def desativa():
        prova = 0
        while prova == 0:
            Solicitacao.solicita_dados_cargo()
            pergunta = int(input(f"Informe o código do cargo que deseja modificar \n ou digite 0 para sair: "))
            mydb = conn()
            mycursor = mydb.cursor()
            verificar = (f"SELECT COUNT(cargo) from cargo where codigo='{pergunta}'")
            mycursor.execute(verificar)
            resultado = mycursor.fetchall()

            if pergunta == 0:
                prova = 1

            elif resultado[0][0] == 1:
                desativa = (f"UPDATE cargo SET status = 0 where codigo = '{pergunta}'")
                mycursor.execute(desativa)
                mydb.commit()
                print(GREEN +"O cargo foi desativado!!!"+ RESET)
                mydb.close()
                prova = 1

            else:
                print('')
                print(RED+"CODIGO INCORRETO"+RESET)
                sleep(1.5)
                os.system("cls")

    def reativar():
        prova = 0
        while(prova == 0):
            Solicitacao.solicita_dados_cargo_inativo()
            pergunta = int(input("Informe o código do cargo que deseja modificar \n ou digite 0 para sair: "))
            mydb = conn()
            mycursor = mydb.cursor()
            verificar = (f"SELECT COUNT(cargo) from cargo where codigo='{pergunta}'")
            mycursor.execute(verificar)
            resultado = mycursor.fetchall()

            if pergunta == 0:
                prova = 1

            elif resultado[0][0] == 1:
                ativa = (f"UPDATE cargo SET status = 1 where codigo = '{pergunta}'")
                mycursor.execute(ativa)
                mydb.commit()
                print(GREEN +"O cargo foi ativado novamente!!!"+ RESET)
                mydb.close()
                prova = 1

            else:
                print(RED+"CODIGO INCORRETO"+RESET)
                sleep(1.5)
                os.system("cls")
