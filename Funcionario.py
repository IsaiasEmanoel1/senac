from Solicitacao import *
import mysql.connector as mysql
from connector import *
from aux_func import *
from Tele_Email_Endere import Tele_Email_Endere
from time import sleep

class Funcionario(Tele_Email_Endere):
    def __init__(self,cpf,nome, cargo,senha, telefone, email, rua, numero, bairro, cidade, cep, **kwargs):
        super().__init__(telefone, email, rua, numero, bairro, cidade, cep)
        self.cpf = cpf
        self.nome = nome
        self.senha = senha
        self.cargo = cargo
        self.telefone = telefone
        self.email = email
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.cep = cep
        self.email2 = kwargs.get('email2', None)
        self.telefone2 = kwargs.get('telefone2', None)
        self.complemento = kwargs.get('complemento', None)

    def cadastro_func(self):
        try:
            mydb = conn()
            sql = (f"INSERT INTO funcionario(cpf, nome, cargo, senha, status) values ('{self.cpf}','{self.nome.lower()}',{self.cargo},'{self.senha}', 1)")
            mycursor = mydb.cursor()
            mycursor.execute(sql)
            mydb.commit()
            sql_tele = (f"INSERT INTO telefone_email(cpf,telefone,email) values ('{self.cpf}','{self.telefone}', '{self.email}')")
            mycursor.execute(sql_tele)
            mydb.commit()
            if self.telefone2 != None:
                if self.email2 != None:
                    sql_tele = (f"INSERT INTO telefone_email(cpf,telefone,email) values ('{self.cpf}','{self.telefone2}', '{self.email2}')")
                    mycursor = mydb.cursor()
                    mycursor.execute(sql_tele)
                    mydb.commit()
                else:
                    sql_tele = (f"INSERT INTO telefone_email(cpf,telefone) values ('{self.cpf}','{self.telefone2}')")
                    mycursor = mydb.cursor()
                    mycursor.execute(sql_tele)
                    mydb.commit()
            elif self.email2 != None:
                    sql_tele = (f"INSERT INTO telefone_email(cpf,email) values ('{self.cpf}', '{self.email2}')")
                    mycursor = mydb.cursor()
                    mycursor.execute(sql_tele)
                    mydb.commit()
            if self.complemento == "NULL":
                sql_endere = (f"INSERT INTO endereco(cpf,rua,numero,bairro,cidade,complemento,cep) values ('{self.cpf}','{self.rua}','{self.numero}','{self.bairro}','{self.cidade}','','{self.cep}')")
                mycursor.execute(sql_endere)
                mydb.commit()
            elif self.complemento != "NULL":
                sql_endere = (f"INSERT INTO endereco(cpf,rua,numero, bairro, cidade, complemento, cep) values ('{self.cpf}','{self.rua}','{self.numero}','{self.bairro}','{self.cidade}','{self.complemento}','{self.cep}')")
                mycursor.execute(sql_endere)
                mydb.commit()
            print (GREEN + f"Cadastro do funcionário {self.nome} feito com sucesso!!" + RESET)

        except mysql.Error as error:
            print(RED +"Algo de errado!!!" + RESET)
            if error.errno == 1062:
                print(RED +"CPF já cadastrado!!!" + RESET)
            
        finally: 
            mydb.close()
