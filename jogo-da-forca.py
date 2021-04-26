import os, random, time
clear = lambda: os.system('cls')
Enforcou = False
Acertou = False
numero_tentativas = 0
Acertos = 0
l = 0 # Usado no 'for' na linha 163
cont = 0
c = [] # Contador de letras digitadas
quantidade = []
certo = []
dicas = [] # Se errar 3 vezes aparece uma dica
palavras = []
repetiu = 0
chuteS = 0 # Transforma o chute em string para obter apenas letras

################################### ABERTURA #######################################
nome=input('DIGITE SEU NOME:')

def mensagem_abertura():
	print(" ==================================================")
	print("|                  JOGO DA FORCA                   |")
	print(" ==================================================")
	print('|               BEM VINDO(A)',nome,'                   |')
	print(' ==================================================')


def placar(p1, p2):
	mensagem_abertura()
	if numero_tentativas == 0:
		print("              |----- ")
		print("              |    | ")
		print("              |     ")
		print("              |    ")
		print("              |     ")
		print("              |     ")
		print("              |")
	if numero_tentativas == 1:
		print("              |----- ")
		print("              |    | ")
		print("              |    O ")
		print("              |     ")
		print("              |     ")
		print("              |     ")
		print("              |")
	if numero_tentativas == 2:
		print("              |----- ")
		print("              |    | ")
		print("              |    O ")
		print("              |    | ")
		print("              |    | ")
		print("              |     ")
		print("              |")
	if numero_tentativas == 3:
		print("              |----- ")
		print("              |    | ")
		print("              |    O ")
		print("              |   /| ")
		print("              |    | ")
		print("              |     ")
		print("              |")
	if numero_tentativas == 4:
		print("              |----- ")
		print("              |    | ")
		print("              |    O ")
		print("              |   /|\\ ")
		print("              |    | ")
		print("              |     ")
		print("              |")
	if numero_tentativas == 5:
		print("              |----- ")
		print("              |    | ")
		print("              |    O ")
		print("              |   /|\\")
		print("              |    | ")
		print("              |   /  ")
		print("              |")
	if numero_tentativas == 6:
		print("              |----- ")
		print("              |    | ")
		print("              |    O ")
		print("              |   /|\\")
		print("              |    | ")
		print("              |   / \\ ")
		print("              |")

	LU = "".join(p1) #letras usadas
	LJ = "".join(p2) #letras juntas
	print("                           "+str(LJ)+"")
	print("\n  Letras Usadas: "+str(LU)+"                       ")
	print(" --------------------------------------------------")
##################################### DICAS #########################################
def dica():
	if numero_tentativas < 3:
		print("                   ASSUNTO: VARIADO                 ")
		print(" --------------------------------------------------")
	if numero_tentativas >= 3:
		ajuda = dica_secreta
		print("             DICA: ",ajuda)
		print(" --------------------------------------------------")

################################ PALAVRA SECRETA ##################################
def carrega_palavra_secreta():
	global palavra_secreta, dica_secreta
	dicas = []
	palavras = []
	arquivo = open("palavras_secretas.txt", "r")
	texto = arquivo.read()
	lista = texto.split('\n')
	LS = "".join(lista).upper() #lista string
	lista2 = LS.split(';')
	for i in range (len(lista2)):
		if i % 2 == 0:
			palavras.append(lista2[i])
		elif i % 2 == 1:
			dicas.append(lista2[i])
	maX = len(palavras) - 1
	numero_aleatorio = random.randint(0, maX)
	palavra_secreta = palavras[numero_aleatorio]
	dica_secreta = dicas[numero_aleatorio]
	arquivo.close()
################################# QUANTIDADE DE LETRAS ###############################
def inicializa_letras_acertadas():
	global letras
	letras = list(palavra_secreta)
	i = 0
	global quantidade
	while i < len(letras):
		quantidade.append('_')
		i = i + 1

####################################### PERGUNTA ######################################
def adivinhe_palavra():
	global chute, c, repetiu, chuteS
	chute = input("  Tente uma letra: ").upper()
	chuteS = chute.isalpha()
	if chuteS == True:
		if chute[0] in c:
			repetiu = 1
		else:
			c.append(chute[0])

###################################### SE ACERTAR #####################################
def chute_correto():
	global Acertos, certo
	certo[l] = chute[0]
	Acertos = Acertos + 1

####################################### JOGO ########################################
comeca = 'S'
mensagem_abertura()
time.sleep(4)
while comeca == 'S':
	carrega_palavra_secreta()
	inicializa_letras_acertadas()
	letras_acertadas = letras[:]
	certo = quantidade[:]

	while Enforcou == False and Acertou == False:
		cont = 0
		clear()
		placar(c, certo)
		dica()
		adivinhe_palavra()
		if chuteS == True:
			if repetiu == 0:
				for l in range(len(letras_acertadas)):
					if chute[0] == letras_acertadas[l]:
						chute_correto()
						cont = cont + 1
				if cont == 0:
					numero_tentativas = numero_tentativas + 1
					print("  Errou :(")
					time.sleep(1)
				else:
					print("  Acertou :D")
					time.sleep(1)
			else:
				print("  Letra repetida, tente outra!")
				repetiu = 0
				time.sleep(1)
		else:
			print("  Digite apenas letras!")
			time.sleep(1)
		clear()
		placar(c, certo)
		dica()
		if Acertos == len(certo):
			time.sleep(1)
			Acertou = True
		if numero_tentativas == 6:
			time.sleep(1)
			Enforcou = True

	if Acertou == True:
		print("  GANHOU!!!!!!")
	if Enforcou == True:
		p = "".join(palavra_secreta)
		print("  PERDEU :(\n  A PALAVRA ERA ",p)
	pergunta = input('\n  DESEJA JOGAR NOVAMENTE? (S/N): ').upper()
	if pergunta[0] == 'S':
		clear()
		Enforcou = False
		Acertou = False
		numero_tentativas = 0
		Acertos = 0
		l = 0
		cont = 0
		repetiu = 0
		del quantidade[:]
		del certo[:]
		del c[:]
		del dicas[:]
		del palavras[:]
		continue
	else:
		clear()
		mensagem_abertura()
		break

partidas_ganhou=int(Acertou)
partidas_perdeu=int(Enforcou)
print('Jogos ganhos:',partidas_ganhou)
print('Jogos perdidos:',partidas_perdeu)
partidas_disputadas=partidas_perdeu+partidas_ganhou
print('Você jogou: ',partidas_disputadas,'vezes!')

input("\n\t\tOBRIGADO POR JOGAR :D...")
