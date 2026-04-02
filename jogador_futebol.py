#CADASTRAR O 1° JOGADOR
print("Bem-vindo ao sistema de cadastro de jogadores!")
time= str(input("defina o nome do seu time: \n"))
print(f"{time} foi selecionado! Agora vamos cadastrar os jogadores e suas estaísticas: \n")
jogadores= []
nome = 0
gols=[]
i = 0
total = sum(gols)
gp = 0
#COLETA DE DADOS
jogador = {"nome do atleta": nome, "gols": gols, "total": total,"g/p":gp}

jogador["nome do atleta"]= str(input("qual o nome do jogador? "))
partidas = int(input(f"quantos jogos o {jogador['nome do atleta']} fez? "))
while i < partidas :
    i += 1
    gols.append(int(input(f"quantos gols ele fez na {i}° partida: ")))

jogador["total"]= total = sum(gols)
jogador["g/p"]= gp = total / partidas
jogadores.append(jogador.copy())

#DADOS DO JOGADOR
print()
print(f"Confira os dados do {jogador['nome do atleta']}:")
for c,k in jogador.items():
    if c == "nome do atleta" :
        print(f"Nome: {k}")
    if c == "gols":
        print(f"Partidas: {partidas}")
        print(f"Gols: {total}")
    if c == "g/p":
        print(f"G/P: {k:.2f} gols a cada partida")
print()

#CONDIÇÃO (QUER CONTINUAR?)
i = 0
a = 0
while True:
    i += 1
    escolha = str (input("quer continuar? "))
    if escolha in " n N NAO nao ":
        break
    elif escolha in " s S SIM sim ":
        a = 0
        total = sum(gols)
        gols = []
        gp = 0
        jogador["nome do atleta"] = str(input(f"qual o nome do {i + 1}° atleta: "))
        partidas = int (input(f"quantas partidas o {jogador['nome do atleta']} jogou? "))
        while a < partidas:
            a+= 1
            gols.append(int(input(f"quantos gols ele fez na {a} partida? ")))
    else :
        print("erro, tente novamente!")

    jogador["total"]= sum(gols)
    jogador["g/p"] = gp = total / partidas
    jogadores.append(jogador.copy())
    


        


print(jogador)
print(jogadores)