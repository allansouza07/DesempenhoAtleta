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
    gols.append(int(input(f"quantos gols ele fez na {i}° partida")))

jogador["total"]= total = sum(gols)
jogador["g/p"]= gp = total / partidas
jogadores.append(jogador.copy())

#CONDIÇÃO (QUER CONTINUAR?)


print(jogador)
print(jogadores)