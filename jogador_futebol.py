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
jogador["partidas"]=partidas
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
        print()
        jogador["total"]= total = sum(gols)
        jogador["g/p"] = gp = total / partidas
        jogador["partidas"]=partidas
        jogadores.append(jogador.copy())
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
        
    else :
        print("erro, tente novamente!")

#MOSTRAR TODOS OS DADOS 
print(f"ESCOLHA A ESTATÍSTICA\n 1 - Jogadores com mais partidas \n 2 - Maiores Artilheiros: \n 3 - Maiores médias de gols por partida: \n 4 - Todas as informações\n 5 - Sair \n")


#JOGADORES COM MAIS PARTIDAS
while True:
    print()
    escolha = int(input("escolha: "))
    print()
    if escolha == 1:
        print('Você selecionou: "Jogadores com mais partidas"')
        print()
        mais_partidas = sorted(jogadores, key= lambda x:x["partidas"], reverse=True)
        for c, k in enumerate (mais_partidas):
            print(f"{k["nome do atleta"]}: {k["partidas"]} partidas jogadas") 
    #JOGADORES ARTILHEIROS
    if escolha == 2:
        print('Você selecionou: "Maiores artilheiros"')
        mais_gols = sorted(jogadores, key = lambda x:x["total"], reverse=True) 
        for c, k in enumerate(mais_gols):
            print(f'{k["nome do atleta"]}: {k["total"]} gols ')
    if escolha == 5:
        break
    
    


        


print(jogador)
print(jogadores)