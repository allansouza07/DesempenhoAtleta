#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.


#dicionario do jogador
import sleep

jogador = {"nome do jogador": 'nome', "partidas jogadas": 'partidas' ,"gols": 'gols', "total": 'total'} 
nome= str(input("qual o nome do jogador? \n"))
jogador["nome do jogador"] = nome
partidas = int(input("quantas partidas ele jogou? \n"))
jogador["partidas jogadas"] = partidas
gols = []
i = 0
total = 0
while i < partidas:
    i += 1
    jogo = int(input(f"quantos gols ele marcou na {i} partida?\n"))
    gols.append(jogo)
    total += jogo
print(">-" * 40)
jogador["gols"] = gols
jogador["total"] = total
for k,v in jogador.items() :
    print(f'o campo {k} tem como resultado: {v}')

escolha = (input(f"voce que ver o histórico de gols de {jogador["nome do jogador"]}? ")) 
if escolha in " sim SIM s S " :

    print()
    print(f"historico de partidas de {jogador['nome do jogador']}")
    for k, v in enumerate(gols) :
        print(f'na {k+1}° partida, {jogador["nome do jogador"]} fez um total de {v} gols')
        time.sleep(1)
    print(f'totalizando, assim, {total} gols')
else:
    print("ok, valeu")