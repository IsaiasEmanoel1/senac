import mysql.connector as mysql
from connector import conn
from Solicitacao import *
import os
from time import sleep
from aux_func import *

class Chaves():
    def __init__(self, num_chave, descri):
        self.num_chave = num_chave
        self.descri = descri

    def cadastro():
        try:
            mydb = conn()
            num_sala,descri = solicita_dados_chaves()
            sql = (f"INSERT INTO chaves(numero_sala, descricao, status) VALUES ('{num_sala}','{descri.lower()}', 1)")
            mycursor = mydb.cursor()
            mycursor.execute(sql)
            mydb.commit()
            print(GREEN +"Chave cadastrada!!!"+ RESET)
            mydb.close()
        except mysql.Error as error:
            if error.errno == 1062:
                print(RED +"Chave já cadastrado!!!" + RESET)

        finally: 
            mydb.close()

    def visualiza_chaves():
        os.system("cls")
        mydb = conn()
        mycursor = mydb.cursor()
        mycursor.execute(f"SELECT * FROM chaves where status = 1")
        myresult = mycursor.fetchall()
        print(BOLD + f"\tSala\tNome"+ RESET)
        for x in myresult:
            print("-"*50)
            print(f"\tNº {x[0]}\t{x[1]}")
        sleep(3)
        print("-"*50)
        mydb.close()

    def solicita_chaves():
        Solicitacao.regis_sol_chave()

    def atualiza_desc():
        prova = 0
        while prova == 0:
            Chaves.visualiza_chaves()
            pergunta = int(input(f"Informe o código da sala que deseja modificar \n ou digite 0 para sair: "))
            mydb = conn()
            mycursor = mydb.cursor()
            verificar = (f"SELECT COUNT(numero_sala) from chaves where numero_sala='{pergunta}' and status = 1 ")
            mycursor.execute(verificar)
            resultado = mycursor.fetchall()

            if pergunta == 0:
                prova = 1

            elif resultado[0][0] == 1:
                pergunta2 = input("Novo nome da chave: ")
                update = (f"UPDATE chaves SET descricao = '{pergunta2}' where numero_sala='{pergunta}'")
                mycursor.execute(update)
                mydb.commit()
                print(GREEN +"A chave foi atualizada!!!"+ RESET)
                mydb.close()
                prova = 1

            else:
                print(RED+"CODIGO INCORRETO"+RESET)
                sleep(1.5)
                os.system("cls")

    def atualiza_num():
        prova = 0
        while prova == 0:
            Chaves.visualiza_chaves()
            pergunta = input(f"Informe o nome da sala que deseja modificar \nou digite 0 para sair: ")
            mydb = conn()
            mycursor = mydb.cursor()
            verificar = (f"SELECT COUNT(descricao) from chaves where descricao='{pergunta}' and status = 1 ")
            mycursor.execute(verificar)
            resultado = mycursor.fetchall()

            if pergunta == '0':
                prova = 1

            if resultado[0][0] == 1:
                pergunta2 = int(input(f'informe o novo numero da sala {pergunta}: '))
                update = (f"UPDATE chaves SET numero_sala = '{pergunta2}' where descricao='{pergunta}'")
                mycursor.execute(update)
                mydb.commit()
                print(GREEN +"A chave foi atualizada!!!"+ RESET)
                mydb.close()
                prova = 1

            elif resultado[0][0] > 1:
                os.system("cls")
                mostra = (f"SELECT numero_sala, descricao from chaves where descricao='{pergunta}' and status = 1")
                mycursor.execute(mostra)
                resultado = mycursor.fetchall()
                print(BOLD + f"\tSala\tNome"+ RESET)
                for x in resultado:
                    print("-"*50)
                    print(f"\tNº {x[0]}\t{x[1]}")
                sleep(3)
                print("-"*50)
                pergunta = int(input('Informe o numero da sala que deseja atualizar: '))
                verificar = (f"SELECT COUNT(numero_sala) from chaves where numero_sala='{pergunta}' and status = 1 ")
                mycursor.execute(verificar)
                resultado = mycursor.fetchall()
                if resultado[0][0] == 1:
                    pergunta2 = int(input(f'informe o novo numero da sala {pergunta}: '))
                    update = (f"UPDATE chaves SET numero_sala = '{pergunta2}' where numero_sala='{pergunta}'")
                    mycursor.execute(update)
                    mydb.commit()
                    print(GREEN +"A chave foi atualizada!!!"+ RESET)
                    mydb.close()
                    prova = 1

                else:
                    print(RED+"CODIGO INCORRETO"+RESET)
                    sleep(1.5)
                    os.system("cls")

            else:
                print(RED+"CODIGO INCORRETO"+RESET)
                sleep(1.5)
                os.system("cls")

    def desativa():
        prova = 0
        while prova == 0:
            Chaves.visualiza_chaves()
            pergunta = int(input(f"Informe o código da chave que deseja modificar \n ou digite 0 para sair: "))
            mydb = conn()
            mycursor = mydb.cursor()
            verificar = (f"SELECT COUNT(numero_sala) from chaves where numero_sala='{pergunta}'")
            mycursor.execute(verificar)
            resultado = mycursor.fetchall()

            if pergunta == 0:
                prova = 1

            elif resultado[0][0] == 1:
                desativa = (f"UPDATE chaves SET status = 0 where numero_sala = '{pergunta}'")
                mycursor.execute(desativa)
                mydb.commit()
                print(GREEN +"A chave foi desativada!!!"+ RESET)
                mydb.close()
                prova = 1

            else:
                print('')
                print(RED+"CODIGO INCORRETO"+RESET)
                sleep(1.5)
                os.system("cls")