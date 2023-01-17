import os
#criar uma funcao
RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

def desenha_tela(tela,altura, largura, simbolo = '-', preenchimento = ' '):
    os.system("cls")
    print(simbolo * largura)
    print(GREEN+f"\t{tela.upper()}"+RESET)
    for _ in range(altura-2):
        print('{}{}{}'.format(simbolo, preenchimento * (largura - 2), simbolo))
    print(simbolo * largura)

def pergunta_submenu(val):
    if val == 1:
        desenha_tela(tela='menu cargo', altura= 2, largura= 26)
        print("Escolha uma opção:", "", "1- Cadastrar", "2- Atualizar dados", "3- Desativar", "4- Visualizar", "5- Reativar","6- Voltar", sep="\n")
        pergunta2 = int(input("Informe o código: "))

    elif val == 2:
        desenha_tela(tela='menu funcionário', altura= 2, largura= 32)
        print("Escolha uma opção:", "", "1- Cadastrar", "2- Atualizar dados", "3- Desativar", "4- Visualizar", "5- Reativar","6- Voltar", sep="\n")
        pergunta2 = int(input("Informe o código: "))

    elif val == 3:
        desenha_tela(tela='menu chaves', altura= 2, largura= 26)
        print("Escolha uma opção:", "", "1- Cadastrar", "2- Atualizar dados", "3- Desativar", "4- Visualizar", "5- Voltar", sep="\n")
        pergunta2 = int(input("Informe o código: "))

    return pergunta2