'''
Pontifícia Universidade Católica do Paraná - PUCPR
Curso: Tecnologia em Análise e Desenvolvimento de Sistemas
Aluno: Rodrigo Hiroito Nishizawa Soares
'''

import random

print("""ZOMBIE DICE
Atividade somativa 1 - Protótipo inicial""")

num_jogadores = 0  # inicializa variável em 0 para condição do while ser True
while num_jogadores < 2:  # laço de repetição para receber o número de jogadores, sendo esse número maior ou igual a 2
    num_jogadores = int(input("Informe a quantidade de jogadores: "))
    if num_jogadores < 2:
        print("Você precisa de pelo menos 2 jogadores!")

lista_jogadores = []  # inicializa lista vazia para armazenar nomes dos jogadores

for i in range(num_jogadores):  # laço de repetição para receber o nome dos jogadores
    lista_jogadores.append(input(f"Informe o nome do jogador {i+1}: "))

# inicialização das variáveis referentes às cores dos dados
dado_verde = "CCCPPE"
dado_amarelo = "CCPPEE"
dado_vermelho = "CPPEEE"

# inicializa o tubo_dados como uma lista com 6 dados verdes, 4 amarelos e 3 vermelhos
tubo_dados = [
    dado_verde, dado_verde, dado_verde, dado_verde, dado_verde, dado_verde,
    dado_amarelo, dado_amarelo, dado_amarelo, dado_amarelo,
    dado_vermelho, dado_vermelho, dado_vermelho
]

print("INICIANDO O JOGO...")

jogador_atual = 0  # inicializa variável referente ao primeiro jogador
dados_sorteados = []  # inicializa lista vazia dos dados a serem retirados do tubo
# inicializa variáveis para contabilizar faces sorteadas dos dados
cerebros = 0
pegadas = 0
espingarda = 0

input("Vamos retirar dados do tubo. Pressione qualquer tecla para continuar.")

while (True):  # laço de repetição referente ao jogo completo
    print(f"Turno do jogador {lista_jogadores[jogador_atual]}")

    for i in range(3):  # laço de repetição que sorteia 3 dados entre os 13 existentes em tubo_dados
        # atribui à variável dado_sorteado um dado aleatório do tubo_dados
        dado_sorteado = tubo_dados[random.randint(0, 12)]
        if dado_sorteado == dado_verde:  # condicionais para atribuir à variável cor_dado a cor do dado sorteado
            cor_dado = "VERDE"
        elif dado_sorteado == dado_amarelo:
            cor_dado = "AMARELO"
        else:
            cor_dado = "VERMELHO"
        print(f"{i+1}.º dado sorteado: {cor_dado}")
        # adiciona o dado_sorteado à lista de dados_sorteados
        dados_sorteados.append(dado_sorteado)

    input("Agora vamos rolar os dados. Pressione qualquer tecla para continuar.")

    for dado in dados_sorteados:  # laço de repetição que sorteia a face dos 3 dados existentes em dados_sorteados
        # sorteia um caracter da string referente ao dado
        face = random.choice(dado)
        if face == "C":  # condicional para mostrar a face sorteada e incrementar a variável respectiva
            print("- CÉREBRO - Você devorou o cérebro de sua vítima!")
            cerebros += 1
        elif face == "E":
            print("- ESPINGARDA - Sua vítima revidou!")
            espingarda += 1
        else:
            print("- PEGADAS - Sua vítima escapou!")
            pegadas += 1

    print(f"PLACAR ATUAL\n"  # mostra placar acumulativo
          f"CÉREBROS: {cerebros}\n"
          f"ESPINGARDAS: {espingarda}")

    continuarTurno = input("Você deseja continuar rolando dados? (S/N):")

    if continuarTurno == "N":  # se jogador quiser encerrar o turno, passa para o próximo jogador e reinicializa as variáveis
        jogador_atual += 1
        dados_sorteados = []
        cerebros = 0
        pegadas = 0
        espingarda = 0
        # finaliza o protótipo se todos os jogadores já tiverem jogado seu turno
        if jogador_atual == len(lista_jogadores):
            print("Finalizando protótipo do jogo")
            break
    else:  # se jogador quiser continuar o turno, reinicializa a lista de dados_sorteados
        print(
            f"Continuando o turno do jogador {lista_jogadores[jogador_atual]}")
        dados_sorteados = []
