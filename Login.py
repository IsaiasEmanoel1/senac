from connector import conn
import os
from aux_func import *
from Solicitacao import Solicitacao
from Chaves import *
from Cargos import *
from Tele_Email_Endere import Tele_Email_Endere
from Funcionario import Funcionario

class Login():
    def __init__(self, cpf, senha):
        self.cpf = cpf
        self.senha = senha

    def menu_diretor():
        desenha_tela(tela='menu', altura= 2, largura= 20)
        print ("Escolha uma opcão: ","" , "1- Gerenciar cargo ", "2- Gerenciar funcionário", "3- Gerenciar chaves","4- Relatórios", "5- Sair", sep="\n")
        pergunta = int(input("Informe o codigo: "))
        os.system("cls")
        prova = 2

        if pergunta == 1:
            os.system("cls")
            while(prova==2):
                pergunta2 = pergunta_submenu(pergunta)
                if pergunta2 == 1:
                    os.system("cls")
                    Cargos.cadastro()
                    sleep(1.5)

                elif pergunta2 == 2:
                    os.system("cls")
                    Cargos.atualiza()
                    sleep(1.5)
                    os.system("cls")

                elif pergunta2 == 3:
                    os.system('cls')
                    Cargos.desativa()
                    sleep(1.5)
                    os.system("cls")

                elif pergunta2 == 4:
                    CONTROLE_MENU = True
                    while CONTROLE_MENU == True:
                        os.system("cls")
                        Solicitacao.solicita_dados_cargo()
                        sleep(1.5)
                        print("1- Voltar",  sep="\n")
                        pergunta2 = int(input("Escolha a opcao: "))
                        if pergunta2 == 1:
                            os.system("cls")
                            CONTROLE_MENU = False
                            
                        else:
                            print(RED +"Codigo incorreto!!"+ RESET)
                            sleep(1.5)
                            os.system("cls")
                            CONTROLE_MENU = True

                elif pergunta2 == 5:
                    os.system("cls")
                    Cargos.reativar()
                    sleep(1.5)
                    os.system("cls")

                elif pergunta2 == 6:
                    os.system("cls")
                    Login.menu_diretor()
                    prova = 0     

        elif pergunta == 2:
            os.system("cls")
            while(prova==2):
                pergunta2 = pergunta_submenu(pergunta)
                if pergunta2 == 1:
                    os.system("cls")
                    cpf, nome, cargo, senha = Solicitacao.solicita_dados_func()
                    sleep(0.5)
                    os.system("cls")
                    p_telefone, telefone, p_email, telefone2, email, email2 = Tele_Email_Endere.cadastro_tele_email()
                    sleep(0.5)
                    os.system("cls")
                    rua, numero, bairro, cidade, cep, complemento,pergunta_comp = Tele_Email_Endere.cadastra_endere()
                    if p_telefone == 2:
                        if p_email == 2:  
                            if pergunta_comp == 2:
                                func = Funcionario(cpf, nome, cargo, senha, telefone, email, rua, numero, bairro, cidade, cep)
                                func.cadastro_func()
                                del func
                                sleep(3)
                                os.system("cls")
                                Login.menu_diretor()
                            elif pergunta_comp == 1:
                                func = Funcionario(cpf, nome, cargo, senha, telefone, email, rua, numero, bairro, cidade, cep, complemento=complemento)
                                func.cadastro_func()
                                del func
                                sleep(3)
                                os.system("cls")
                                Login.menu_diretor()
                        elif p_email == 1:
                            if pergunta_comp == 2:
                                func = Funcionario(cpf, nome, cargo, senha, telefone, email, rua, numero, bairro, cidade, cep, email2 = email2)
                                func.cadastro_func()
                                del func
                                sleep(3)
                                os.system("cls")
                                Login.menu_diretor()
                            elif pergunta_comp == 1:
                                func = Funcionario(cpf, nome, cargo, senha, telefone, email, rua, numero, bairro, cidade, cep, email2 = email2, complemento=complemento)
                                func.cadastro_func()
                                del func
                                sleep(3)
                                os.system("cls")
                                Login.menu_diretor()

                    elif p_telefone == 1:
                        if p_email == 2:
                            if pergunta_comp == 2:
                                func = Funcionario(cpf, nome, cargo, senha, telefone,email, rua, numero, bairro, cidade, cep, telefone2 = telefone2 )
                                func.cadastro_func()
                                del func
                                sleep(3)
                                os.system("cls")
                                Login.menu_diretor()

                            elif pergunta_comp == 1:
                                func = Funcionario(cpf, nome, cargo, senha, telefone,email, rua, numero, bairro, cidade, cep, telefone2 = telefone2, complemento=complemento)
                                func.cadastro_func()
                                del func
                                sleep(3)
                                os.system("cls")
                                Login.menu_diretor()

                        elif p_email == 1:
                            if pergunta_comp == 2:
                                func = Funcionario(cpf, nome, cargo, senha, telefone, email, rua, numero, bairro, cidade, cep, telefone2 = telefone2, email2 = email2)
                                func.cadastro_func()
                                del func
                                sleep(3)
                                os.system("cls")
                                Login.menu_diretor()
                            
                            elif pergunta_comp == 1:
                                func = Funcionario(cpf, nome, cargo, senha, telefone, email, rua, numero, bairro, cidade, cep, telefone2 = telefone2, email2 = email2, complemento=complemento)
                                func.cadastro_func()
                                del func
                                sleep(3)
                                os.system("cls")
                                Login.menu_diretor()

                elif pergunta2 == 6:
                    os.system("cls")
                    prova = 0
                    Login.menu_diretor()
        
        elif pergunta == 3:
            os.system("cls")
            while(prova==2):
                pergunta2 = pergunta_submenu(pergunta)

                if pergunta2 == 1:
                    os.system("cls")
                    Chaves.cadastro()
                    sleep(1.5)
                    os.system("cls")
                
                elif pergunta2 == 2:
                    os.system("cls")
                    pergunta_at = int(input('Escolha uma opção: \n \n1- Atualizar numero da sala \n2- Atualizar nome da sala \n3- Voltar \nInforme o codigo: '))
                    if pergunta_at == 1:
                        os.system("cls")
                        Chaves.atualiza_num()
                        sleep(1.5)
                        os.system("cls")

                    elif pergunta_at == 2:               
                        os.system("cls")
                        Chaves.atualiza_desc()
                        sleep(1.5)
                        os.system("cls")

                    elif pergunta_at==3:
                        os.system("cls")

                elif pergunta2 == 3:
                    os.system("cls")
                    Chaves.desativa()
                    sleep(1.5)
                    os.system("cls")

                elif pergunta2 == 4:
                    os.system("cls")
                    CONTROLE_MENU = True
                    while CONTROLE_MENU == True:
                        os.system("cls")
                        Chaves.visualiza_chaves()
                        sleep(1.5)
                        print("1- Voltar ao Menu Principal", sep="\n")
                        pergunta2 = int(input("Escolha a opcao: "))

                        if pergunta2 == 1:
                            os.system("cls")
                            CONTROLE_MENU = False
                            Login.menu_diretor()

                        else:
                            print(RED +"Codigo incorreto!!"+ RESET)
                            sleep(1.5)
                            os.system("cls")
                            CONTROLE_MENU = True
    
                elif pergunta2 == 5:
                    os.system("cls")
                    prova = 0
                    Login.menu_diretor()

        elif pergunta == 4:
            pergunta2 = 2
            while (pergunta2 == 2):
                os.system("cls")
                Solicitacao.visua_relatorio()
                sleep(1.5)
                print("1- Voltar ao Menu Principal","2- Voltar ao Menu Anterior",  sep="\n")
                pergunta2 = int(input("Escolha a opcao: "))
                if pergunta2 == 1:
                    os.system("cls")
                    Login.menu_diretor()
            else:
                print(RED +"Codigo incorreto!!"+ RESET)
                sleep(1.5)
                os.system("cls")
                Login.menu_diretor()
            
        elif pergunta == 5:
            print("Saindo...")
            sleep(1.5)
            Login.login_inicial()

        else:
            print(RED +"Codigo incorreto!!"+ RESET)
            sleep(1.5)
            os.system("cls")
            Login.menu_diretor()

    def menu_seguranca():
        desenha_tela(tela='menu', altura= 2, largura= 20)
        print ("Escolha uma opcão: ", "1- Visualizar chaves","2- Entrega de chaves","3- Devolução","4- Visualizar relatório", "5- Sair", sep="\n")
        pergunta = int(input("Informe o codigo: "))
        os.system("cls")

        if pergunta == 1:
            CONTROLE_MENU = True       
            while CONTROLE_MENU == True:
                os.system("cls")
                Chaves.visualiza_chaves()
                sleep(2)
                print("1- Voltar ao Menu Principal",  sep="\n")
                pergunta2 = int(input("Escolha a opcao: "))
                if pergunta2 == 1:
                    os.system("cls")
                    CONTROLE_MENU = False
                    Login.menu_seguranca()
                else:
                    CONTROLE_MENU = True
                    print(RED +"Codigo incorreto!!"+ RESET)
                    

        elif pergunta == 2:
            pergunta2 = 2
            while (pergunta2 == 2):
                os.system("cls")
                Chaves.solicita_chaves()
                sleep(2)
                print("-"*50)
                print("1- Voltar ao Menu Principal","2- Voltar ao Menu Anterior",  sep="\n")
                pergunta2 = int(input("Escolha a opcao: "))
                if pergunta2 == 1:
                    os.system("cls")
                    Login.menu_seguranca()
                    
            else:
                print(RED +"Codigo incorreto!!"+ RESET)
                sleep(1.5)
                os.system("cls")
                Login.menu_seguranca()

        elif pergunta == 3:
            pergunta2 = 2
            while (pergunta2 == 2):
                os.system("cls")
                Solicitacao.verifica_devolucao()
                sleep(2)
                print("-"*50)
                print("1- Voltar ao Menu Principal","2- Voltar ao Menu Anterior",  sep="\n")
                pergunta2 = int(input("Escolha a opcao: "))
                if pergunta2 == 1:
                    os.system("cls")
                    Login.menu_seguranca()
            else:
                print(RED +"Codigo incorreto!!"+ RESET)
                sleep(1.5)
                os.system("cls")
                Login.menu_seguranca()      

        elif pergunta == 4:
            pergunta2 = 2
            while (pergunta2 == 2):
                os.system("cls")
                Solicitacao.visua_relatorio()
                sleep(2)
                print("1- Voltar ao Menu Principal","2- Voltar ao Menu Anterior",  sep="\n")
                pergunta2 = int(input("Escolha a opcao: "))
                if pergunta2 == 1:
                    os.system("cls")
                    Login.menu_seguranca()
            else:
                print(RED +"Codigo incorreto!!"+ RESET)
                sleep(1.5)
                os.system("cls")
                Login.menu_seguranca()

        elif pergunta == 5:
            print("Saindo...")
            sleep(1.5)
            Login.login_inicial()

        else:
            print(RED +"Codigo incorreto!!"+ RESET)
            sleep(1.5)
            os.system("cls")
            Login.menu_seguranca()

    def executa_login(self):
        mydb = conn()
        sql = (f"SELECT COUNT(nome), nome, cargo, cpf, senha FROM funcionario where cpf = '{self.cpf}' and senha = '{self.senha}'")
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        myresult = mycursor.fetchone()

        if myresult[0] == 1:
            if myresult[2] == 1:
                Login.menu_diretor()
                print(f"Olá {myresult[1]}")
            elif myresult[2] == 4:
                Login.menu_seguranca()
                print(GREEN +f"Olá {myresult[1]}"+ RESET)
            else:
                print(RED +"ACESSO NEGADO!!"+ RESET)
                sleep(2)
                Login.login_inicial()
        mydb.close()
        mydb = conn()
        sql_confirma = (f"SELECT COUNT(cpf), cpf, senha FROM funcionario where cpf = '{self.cpf}'")
        mycursor = mydb.cursor()
        mycursor.execute(sql_confirma)
        myresult = mycursor.fetchone()
        if myresult[1] == self.cpf and myresult[2] != self.senha:
            print(RED +f"Senha incorreto!!"+ RESET)
            sleep(2)
            Login.login_inicial()
        elif myresult[1] != self.cpf and myresult[2] != self.senha:
            print(RED +f"CPF e senha incorreto!!"+ RESET)
            sleep(2)
            Login.login_inicial()

    def login_inicial():
        desenha_tela(tela='Login', altura= 2, largura= 20)
        cpf, senha = solicita_login()
        login = Login(cpf, senha)
        login.executa_login()