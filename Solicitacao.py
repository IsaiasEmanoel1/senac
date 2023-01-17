from connector import conn
from aux_func import *
from Tele_Email_Endere import Tele_Email_Endere
from time import sleep

def solicita_login():
    cpf = input("Informe seu CPF: ")
    senha = input("Informe sua senha: ")

    return cpf, senha

def solicita_dados_chaves():
    num_sala = int(input("Informe o numero da sala a ser cadastrada: "))
    descri = input("Informe uma descricao a chave: ")

    return num_sala,descri

def solicita_dados_cargo():
    nome_cargo = input("Informe o cargo a ser adicinado: ")

    return nome_cargo

class Solicitacao:
    def __init__(self):
        pass

    def verifica_func_sol():
            func = input("Funcionario: ")
            mydb = conn()
            mycursor = mydb.cursor()
            codigo = (f"SELECT cpf, nome FROM funcionario where nome LIKE '%{func.lower()}%'")
            mycursor.execute(codigo)
            myresult = mycursor.fetchall()
            print("-"*50)
            for x in myresult:
                print("CPF- ", x[0], "| Nome- ", x[1])
            return myresult
        
    def verifica_devolucao():
        sol = 0
        func = input("Funcionario: ")
        mydb = conn()
        mycursor = mydb.cursor()
        codigo = (f"SELECT s.cpf, f.nome,s.numero_sala FROM solicitacao as s INNER JOIN funcionario as f ON s.cpf = f.cpf AND f.nome LIKE '%{func.lower()}%' WHERE s.status = '0'")
        mycursor.execute(codigo)
        myresult = mycursor.fetchall()
        if len(myresult) != 0:
            for x in myresult:
                print("CPF- ", x[0], "| Nome- ", x[1],"| Sala- ", x[2])
            while sol == 0:
                pergunta_cpf = input("Informe o CPF: ")
                sol = Solicitacao.verifica_cpf_sol(pergunta_cpf)
                if sol == 1:
                    senha = input("Senha de segurança do funcionario: ")
                    resul = Solicitacao.verifica_senha(pergunta_cpf,senha)                 
                    if resul[0][0] == 1:
                        sql = (f"UPDATE solicitacao SET status ='1', data_devolucao = NOW() WHERE cpf = '{pergunta_cpf}'")
                        mycursor.execute(sql)
                        mydb.commit()
                        mydb.close()
                        print(GREEN +"Chave devolvida"+ RESET)
                    else:
                        print(RED+"Senha incorreta"+RESET)
                elif sol == 0:
                    print(RED+ "CPF não indetificado!!"+ RESET)
        else:
            print(RED +"Nenhum Funcionário encontrado!!"+ RESET)

    def visua_relatorio():
        desenha_tela(tela='Relatório', altura= 2, largura= 25)
        print("1- Mensal", "2- Diario", "3- Turno", sep="\n")
        mydb = conn()
        mycursor = mydb.cursor()
        pergunta = int(input("Escolha uma opcão: "))

        if pergunta == 1:
            mes = int(input("Informe o número correspondente ao mês: "))
            codigo = (f"SELECT f.nome, s.numero_sala, DATE_FORMAT(CAST(DATE(s.data_entrega) AS CHAR),'%d/%m/%Y'),CAST(TIME(s.data_entrega) AS CHAR), DATE_FORMAT(CAST(DATE(s.data_devolucao) AS CHAR),'%d/%m/%Y'),CAST(TIME(s.data_devolucao) AS CHAR) FROM solicitacao as s INNER JOIN funcionario as f on s.cpf = f.cpf WHERE MONTH(data_devolucao)={mes} AND YEAR(data_devolucao)=YEAR(CURRENT_DATE())")
            mycursor.execute(codigo)
            myresult = mycursor.fetchall()
            os.system("cls")
            print("-"*86)
            print(BOLD + f"Nome \tN da sala\tData entrega\tHora entrega\tData devolucao\tHora devolucao"+ RESET)
            print("-"*86)
            for x in myresult:
                if x[3] == x[5]:
                    print(f"{x[0]}\t{x[1]}\t\t{x[2]}\t{x[3]}\t{x[4]}"+ RED + f"\t{x[5]}"+ RESET)
                    print("-"*86)
                else:

                    print(f"{x[0]}\t{x[1]}\t\t{x[2]}\t{x[3]}\t{x[4]}"+ GREEN +f"\t{x[5]}"+ RESET)
                    print("-"*86)

        elif pergunta == 2:
            codigo = (f"SELECT f.nome, s.numero_sala, DATE_FORMAT(CAST(DATE(s.data_entrega) AS CHAR),'%d/%m/%Y'),\
            CAST(TIME(s.data_entrega) AS CHAR), DATE_FORMAT(CAST(DATE(s.data_devolucao) AS CHAR),'%d/%m/%Y'),\
            CAST(TIME(s.data_devolucao) AS CHAR) \
            FROM solicitacao AS s INNER JOIN funcionario AS f on s.cpf = f.cpf WHERE DAY(data_devolucao)=DAY(CURRENT_DATE()) AND YEAR(data_devolucao)=YEAR(CURRENT_DATE())")
            mycursor.execute(codigo)
            myresult = mycursor.fetchall()
            os.system("cls")
            print("-"*86)
            print(BOLD + f"Nome\tN da sala\tData entrega\tHora entrega\tData devolucao\tHora devolucao"+ RESET)
            print("-"*86)
            for x in myresult:
                if x[3] == x[5]:
                    print(f"{x[0]}\t{x[1]}\t\t{x[2]}\t{x[3]}\t{x[4]}"+ RED + f"\t{x[5]}"+ RESET)
                    print("-"*86)
                else:
                    print(f"{x[0]}\t{x[1]}\t\t{x[2]}\t{x[3]}\t{x[4]}"+ GREEN +f"\t{x[5]}"+ RESET)
                    print("-"*86)

        elif pergunta == 3:
            os.system("cls")
            print("1- Manha", "2- Tarde", "3- Noite", sep="\n")
            turno = int(input("Informe o numero do turno: "))
            os.system("cls")
            if turno == 1:
                codigo = (f"SELECT f.nome, s.numero_sala, DATE_FORMAT(CAST(DATE(s.data_entrega) AS CHAR),'%d/%m/%Y'),\
                            CAST(TIME(s.data_entrega) AS CHAR), DATE_FORMAT(CAST(DATE(s.data_devolucao) AS CHAR),'%d/%m/%Y'),\
                            CAST(TIME(s.data_devolucao) AS CHAR)\
                            FROM solicitacao AS s INNER JOIN funcionario AS f on s.cpf= f.cpf\
                            WHERE ((s.data_entrega BETWEEN cast(concat(date(now()), ' 07:00:00') as datetime)\
                            AND cast(concat(date(now()), ' 12:59:59') as datetime)\
                            AND s.data_entrega between cast(concat(date(now()), ' 07:00:00') as datetime) AND cast(concat(date(now()), ' 12:59:59')as datetime)))") 
                mycursor.execute(codigo)
                myresult = mycursor.fetchall()
                print("-"*86)
                print(BOLD + f"Nome \tN da sala\tData entrega\tHora entrega\tData devolucao\tHora devolucao"+ RESET)
                print("-"*86)
                for x in myresult:
                    if x[3] == x[5]:
                        print(f"{x[0]}\t{x[1]}\t\t{x[2]}\t{x[3]}\t{x[4]}"+ RED + f"\t{x[5]}"+ RESET)
                        print("-"*86)
                    else:
                        print(f"{x[0]}\t{x[1]}\t\t{x[2]}\t{x[3]}\t{x[4]}"+ GREEN +f"\t{x[5]}"+ RESET)
                        print("-"*86)

            elif turno == 2:
                codigo = (f"SELECT f.nome, s.numero_sala, DATE_FORMAT(CAST(DATE(s.data_entrega) AS CHAR),'%d/%m/%Y'),\
                            CAST(TIME(s.data_entrega) AS CHAR), DATE_FORMAT(CAST(DATE(s.data_devolucao) AS CHAR),'%d/%m/%Y'),\
                            CAST(TIME(s.data_devolucao) AS CHAR)\
                            FROM solicitacao AS s INNER JOIN funcionario AS f on s.cpf= f.cpf\
                            WHERE ((s.data_entrega BETWEEN cast(concat(date(now()), ' 13:00:00') as datetime) \
                            AND cast(concat(date(now()), ' 17:59:59') as datetime) \
                            AND s.data_entrega between cast(concat(date(now()), ' 13:00:00') as datetime) \
                            AND cast(concat(date(now()), ' 17:59:59')as datetime) ))")
                mycursor.execute(codigo)
                myresult = mycursor.fetchall()
                print("-"*86)
                print(BOLD + f"Nome \tN da sala\tData entrega\tHora entrega\tData devolucao\tHora devolucao"+ RESET)
                print("-"*86)
                for x in myresult:
                   if x[3] == x[5]:
                        print(f"{x[0]}\t{x[1]}\t\t{x[2]}\t{x[3]}\t{x[4]}"+ RED + f"\t{x[5]}"+ RESET)
                        print("-"*86)
                   else:
                        print(f"{x[0]}\t{x[1]}\t\t{x[2]}\t{x[3]}\t{x[4]}"+ GREEN +f"\t{x[5]}"+ RESET)
                        print("-"*86)

            elif turno == 3:
                codigo = (f"SELECT f.nome, s.numero_sala, DATE_FORMAT(CAST(DATE(s.data_entrega) AS CHAR),'%d/%m/%Y'),\
                            CAST(TIME(s.data_entrega) AS CHAR), DATE_FORMAT(CAST(DATE(s.data_devolucao) AS CHAR),'%d/%m/%Y'),\
                            CAST(TIME(s.data_devolucao) AS CHAR)\
                            FROM solicitacao AS s INNER JOIN funcionario AS f on s.cpf= f.cpf\
                            WHERE ((s.data_entrega BETWEEN cast(concat(date(now()), ' 18:00:00') as datetime) \
                            AND cast(concat(date(now()), ' 22:59:59') as datetime) \
                            AND s.data_entrega between cast(concat(date(now()), ' 18:00:00') as datetime) \
                            AND cast(concat(date(now()), ' 22:59:59')as datetime) ))")
                mycursor.execute(codigo)
                myresult = mycursor.fetchall()
                print("-"*86)
                print(BOLD + f"Nome\tN da sala\tData entrega\tHora entrega\tData devolucao\tHora devolucao"+ RESET)
                print("-"*86)
                for x in myresult:
                   if x[3] == x[5]:
                        print(f"{x[0]}\t{x[1]}\t\t{x[2]}\t{x[3]}\t{x[4]}"+ RED + f"\t{x[5]}"+ RESET)
                        print("-"*86)
                   else:
                        print(f"{x[0]}\t{x[1]}\t\t{x[2]}\t{x[3]}\t{x[4]}"+ GREEN +f"\t{x[5]}"+ RESET)
                        print("-"*86)
        else:
            os.system("cls")
            print(RED+"Código incorreto!!"+RESET)
            sleep(1.5)
            Solicitacao.visua_relatorio()
    
    def regis_sol_chave():
        sol = 0
        resultado_int = 0

        while (sol == 0 ):
            sleep(1)
            os.system("cls")
            lista = Solicitacao.verifica_sol_cpf()
            print("-"*50)
            cpf = input("CPF: ") 
            for x in lista:

                if cpf == x:                    
                    sol = Solicitacao.verifica_cpf(cpf)

                    if sol == 1:

                        while (resultado_int == 0):
                            sleep(1)
                            os.system("cls")
                            mydb = conn()
                            mycursor = mydb.cursor()
                            verifi_func_dis = (f"SELECT COUNT(s.status) as qtd, f.nome, s.numero_sala, s.status FROM solicitacao AS  s INNER JOIN funcionario as f on s.cpf = f.cpf WHERE s.cpf = '{cpf}' and s.status = '0' GROUP BY s.numero_sala")
                            mycursor.execute(verifi_func_dis)
                            myresult = mycursor.fetchall()
                            mydb.close()

                            if len(myresult) == 0 or myresult[0][0] == 0:
                                chave = int(input("Numero da sala: "))
                                mydb = conn()
                                mycursor = mydb.cursor()
                                num_chave = (f"SELECT COUNT(numero_sala) FROM chaves WHERE numero_sala = '{chave}'")
                                mycursor.execute(num_chave)
                                resultado = mycursor.fetchall()
                                resultado_int = int(resultado[0][0])

                                if resultado[0][0] == 1:
                                        verifi_chave_dis = (f"SELECT status FROM solicitacao WHERE numero_sala = '{chave}' ORDER BY status ASC LIMIT 1")
                                        mycursor.execute(verifi_chave_dis)
                                        myresult1 = mycursor.fetchall()

                                        if len(myresult1) == 0 or myresult1[0][0] == '1':
                                            senha = input("Senha de segurança do funcionario: ")
                                            resul = Solicitacao.verifica_senha(cpf,senha)  

                                            if resul[0][0] == 1:
                                                solicitacao = (f"INSERT INTO solicitacao(cpf, numero_sala, status, data_entrega, data_devolucao)\
                                                VALUES ('{cpf}', '{chave}', '0',NOW(), NOW() )")
                                                mycursor.execute(solicitacao)
                                                mydb.commit()
                                                mydb.close()
                                                print(GREEN +"Chave entregue!!"+ RESET)

                                            else:
                                                print(RED+"Senha incorreta"+RESET)

                                        elif myresult1[0][0] == '0':
                                            print(RED+"Chave indisponivel!!"+RESET)

                                        elif myresult[0][0] >= 1:
                                            print(RED +"Devolva a chave primeiro!!"+ RESET)
                                            print(f"Nome do funcionário- {myresult[0][1]} | Sala em uso- {myresult[0][2]}")

                                elif resultado[0][0] == 0:
                                    print(RED +"Chave nao cadastrada!!"+ RESET)

                            else:
                                print(RED+"O funcionario ja pegou uma chave!!"+RESET)
                                resultado_int = 1
                                sleep(1.5)
                                
                            
                    elif sol == 0:
                        print(RED +"CPF não existe!"+ RESET)

    def regis_receb_chave():
        cpf = input("CPF: ")
        mydb = conn()
        mycursor = mydb.cursor()
        solicitacao = (f"UPDATE solicitacao SET status=1, data_devolucao=SYSDATE() WHERE cpf='{cpf}'")
        mycursor.execute(solicitacao)
        mydb.commit()
        print(GREEN +"Chave devolvida com sucesso!!"+ RESET)
        mydb.close()
    
    def recebe_chaves():
        Solicitacao.verifica_devolucao()
        Solicitacao.regis_receb_chave()

    def solicita_dados_func():
        desenha_tela(tela="dados", altura= 2, largura= 20)
        nome = input("Informe o nome do funcionario: ")
        cpf = input("Informe o CPF do funcionario: ")        
        Solicitacao.solicita_dados_cargo()
        cargo = int(input("Informe o " + CYAN + "CÓDIGO" + RESET + " do cargo: "))
        senha = input("Informe uma senha: ")
        

        return cpf, nome, cargo, senha

    def solicita_dados_cargo():
        mydb = conn()
        mycursor = mydb.cursor()
        sql = "SELECT * FROM cargo where status = 1"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        print("-" *50)
        print(CYAN +"Códigos e Cargos cadastrados! :)"+ RESET)
        print("-" *50)
        for j in myresult:
            print(f"Código: {j[0]} | Cargo: {j[1]}")
        print("-" *50)
        mydb.close()

    def verifica_cpf(cpf):
        mydb = conn()
        mycursor = mydb.cursor()
        sql = (f"SELECT COUNT(cpf) FROM funcionario WHERE cpf = '{cpf}'")
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        mydb.close()
        
        return myresult[0][0]
    
    def verifica_sol_cpf():
        myresult1 = Solicitacao.verifica_func_sol()
        mydb = conn()
        mycursor = mydb.cursor()
        p = 0
        lista =[]
        for x in myresult1:
            mydb = conn()
            mycursor = mydb.cursor()
            sql = (f"SELECT cpf from funcionario where cpf = '{x[p]}'")
            mycursor.execute(sql)        
            p +=1
            lista.append(x[0])
            mydb.close()
        return lista
    
    def verifica_cpf_sol(cpf):
        mydb = conn()
        mycursor = mydb.cursor()
        sql = (f"SELECT COUNT(cpf) FROM solicitacao WHERE cpf = '{cpf}' AND status = '0'")
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        mydb.close()

        return myresult[0][0]
    def verifica_senha(cpf, senha):
        mydb = conn()
        mycursor = mydb.cursor()
        sql = (f"SELECT COUNT(senha) FROM funcionario WHERE cpf = '{cpf}' AND senha = '{senha}'")
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        mydb.close()

        return myresult
    
    def solicita_dados_cargo_inativo():
        mydb = conn()
        mycursor = mydb.cursor()
        sql = "SELECT * FROM cargo where status = 0"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        print("-" *50)
        print(CYAN +"Códigos e Cargos cadastrados! :)"+ RESET)
        print("-" *50)
        for j in myresult:
            print(f"Código: {j[0]} | Cargo: {j[1]}")
        print("-" *50)
        mydb.close()