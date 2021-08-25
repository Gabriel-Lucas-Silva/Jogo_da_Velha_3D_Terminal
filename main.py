
import random
import time
import os


#Função que criará as 3 matrizes que servirão de base para as 3 camadas
def criarMat(linhas, colunas, valorI):
  m = [[valorI]*colunas for _ in range (linhas)]
  return m
  

#Função resposável por mostrar as camadas do jogo
def mostrarCam(c1,c2,c3):
  print("   Camada 1         Camada 2         Camada 3")
  print("  1   2   3        1   2   3        1   2   3")

  for i in range(3):
    print(i+1,end="")
    for g in range(2):
      print(c1[i][g],end="|")
    print(c1[i][2],end="")
    print(i+1,"   ",end="")
    print(i+1,end="")
    for g in range(2):
      print(c2[i][g],end="|")
    print(c2[i][2],end="")
    print(i+1,"   ",end="")
    print(i+1,end="")
    for g in range(2):
      print(c3[i][g],end="|")
    print(c3[i][2],end="")
    print(i+1,"   ",end="")
      
    print()

    if i<2:
      print(" ---+---+---      ---+---+---      ---+---+---")


#Função responsável por fazer as marcações nas camadas
def marcarCam(simbolo,ca,li,co,c1,c2,c3):
  #Recebe o símbolo a ser marcado
  #Recebe as coordenadas escolhidas (ca,li,co)
  #Recebe as camadas (matrizes c1,c2,c3)

  #ca = camada
  #li = linha
  #co = coluna

  c1j = c1[li-1][co-1]
  c2j = c2[li-1][co-1]
  c3j = c3[li-1][co-1]

  if ((ca==1) and (c1j == "   ")):
    #Encontra a camada escolhida e verifica se a coordenada passada está disponível para, em seguida, realizar a marcação
    c1[li-1][co-1] = " "+simbolo+" "
    return False

  elif ((ca==2) and (c2j == "   ")):
    c2[li-1][co-1] = " "+simbolo+" "
    return False

  elif ((ca==3) and (c3j == "   ")):
    c3[li-1][co-1] = " "+simbolo+" "
    return False

  else:
    return True


#Função para solicitar e validar a jogada da pessoa(humano)
def jogaPes(simpes,c1,c2,c3):
  #Função que verifica se as coordenadas passadas são válidas
  def validacoord(c):
    i = 0
    g = 0
    while (i < (len(c)-g)):
      numero = int(c[i])
      #Verificando se os dígitos entre as vírgulas são válidos e excluindo os inválidos
      if ((numero!=1) and (numero!=2) and (numero!=3)):
        del(c[i])
        g += 1
      i += 1

    return c

  jogar = True
  while  jogar:
    c = input("Escolha uma coordenada e digite no seguinte\nformato (Camada,Linha,Coluna): ").split(",")
    print()

    c = validacoord(c)

    #Verifica se a quantidade de dígitos que restaram após a limpeza é válida
    if (len(c) != 3):
      print("\033[1m"+"\033[31m"+"              Coordenada inválida\n\n"+"\033[0;0m")

    else:
      #Atribui as coordenadas armazenadas na lista às variáveis de localização (ca,li,co)
      ca=int(c[0])
      li=int(c[1])
      co=int(c[2])

      #Solicita a marcação passando as coordenadas e recebe a confirmação se o ato está consumado ou não
      if (ca==1):
        jogar = marcarCam(simpes,ca,li,co,c1,c2,c3)

      elif (ca==2):
        jogar = marcarCam(simpes,ca,li,co,c1,c2,c3)

      elif (ca==3):
        jogar = marcarCam(simpes,ca,li,co,c1,c2,c3)

      #Se não estiver, a coordenada não está disponível
      else:
        print("\033[1m"+"\033[31m"+"              Coordenada inválida\n\n"+"\033[0;0m")

    
#Função para realizar a jogada do computador seguindo a estratégia determinada
def jogacomp(simcomp,simpes,rodadas,c1,c2,c3):
  jogar = True
  #'For' responsável por fazer o computador realizar as verificações buscando por uma situação de vitória iminente do próprio e, em seguida, realizar as mesmas verificações buscando por uma situação de vitória iminente do adversário
  for comp_pessoa in range (2):
    if comp_pessoa == 0:
      marcacao= (" "+simcomp+" ")
    else:
      marcacao= (" "+simpes+" ")

    for i in range (3):
      seguinte = i+1
      posSeguinte = i+2
      if seguinte==3:
        seguinte = 0
      if posSeguinte>=3:
        posSeguinte = posSeguinte-3

      for g in range (3):
        segc = g+1
        if segc==3:
          segc = 0
        #Início da codificação da estratégia do computador
        if ((c1[i][g] == marcacao) and (jogar)):
            ca = 1
            co = g+1
            if ((c1[i][g] == c1[seguinte][g]== marcacao) and (jogar)):
              li = seguinte+2
              if li>=4:
                li -= 3
              jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
            if ((c1[i][g] == c1[posSeguinte][g]== marcacao) and (jogar)):
              li = seguinte+1
              if li>=4:
                li -= 3
              jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
            if ((c1[i][segc] == c1[i][g]== marcacao) and (jogar)):
              li = i+1
              co = segc+2
              if co==4:
                co = 1
              jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
            if ((c1[i][g] == c2[i][g]== marcacao) and (jogar)):
              ca = 3
              li = i+1
              co = g+1
              jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
            if ((c1[i][g] == c3[i][g]== marcacao) and (jogar)):
              ca = 2
              li = i+1
              co = g+1
              jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
            if ((i<=1) and (c1[i][i] == c1[i+1][i+1] == marcacao) and (jogar)):
              ca = 1
              li = i+3
              co = i+3
              if co==4:
                li = 1
                co = 1
              jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
            if ((c1[0][0] == c1[2][2]== marcacao) and (jogar)):
              ca = 1
              li = 2
              co = 2
              jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
            if ((i==g==1) and (jogar)):
              ca = 1
              if ((c1[0][2]==c1[1][1]== marcacao) and (jogar)):
                li = 3
                co = 1
                jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
              if ((c1[2][0]==c1[1][1]== marcacao) and (jogar)):
                li = 1
                co = 3
                jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
              if ((c1[2][0]==c1[0][2]== marcacao) and (jogar)):
                ca = 1
                li = 2
                co = 2
                jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)


        if ((c2[i][g] == marcacao) and (jogar)):
            ca = 2
            co = g+1
            if ((c2[i][g] == c2[seguinte][g]== marcacao) and (jogar)):
              li = seguinte+2
              if li>=4:
                li -= 3
              jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
            if ((c2[i][g] == c2[posSeguinte][g]== marcacao) and (jogar)):
              li = seguinte+1
              if li>=4:
                li -= 3
              jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
            if ((c2[i][segc] == c2[i][g]== marcacao) and (jogar)):
              li = i+1
              co = segc+2
              if co==4:
                co = 1
              jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
            if ((c3[i][g] == c2[i][g]== marcacao) and (jogar)):
              ca = 1
              li = i+1
              co = g+1
              jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
            if ((i<=1) and (c2[i][i] == c2[i+1][i+1] == marcacao) and (jogar)):
              ca = 2
              li = i+3
              co = i+3
              if co==4:
                li = 1
                co = 1
              jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
            if ((c2[0][0] == c2[2][2]== marcacao) and (jogar)):
              ca = 2
              li = 2
              co = 2
              jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
            if ((c2[2][0]==c2[0][2]== marcacao) and (jogar)):
                ca = 2
                li = 2
                co = 2
                jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)


            if ((c2[1][1] == marcacao) and (jogar)):
              for t in range (3):
                meio = c2[1][1]
                if ((c2[0][2] == marcacao) and (jogar)):
                  ca = 2
                  li = 3
                  co = 1
                  jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
                if ((c2[2][0] == marcacao) and (jogar)):
                  ca = 2
                  li = 1
                  co = 3
                  jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
                if ((c1[t][1]==meio) and (jogar)):
                  ca = 3
                  co = 2
                  if t==0:
                    li = 3
                    jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
                  elif t==2:
                    li = 1
                    jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
                if ((c3[t][1]==meio) and (jogar)):
                  ca = 1
                  co = 2
                  if t==0:
                    li = 3
                    jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
                  elif t==2:
                    li = 1
                    jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)   
                if ((c1[0][t]==meio) and (jogar)):
                  ca = 3
                  li = 3
                  if t==0:
                    co = 3
                    jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
                  elif t==2:
                    co = 1
                    jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3) 
                if ((c1[2][t]==meio) and (jogar)):
                  ca = 3
                  li = 1
                  if t==0:
                    co = 3
                    jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
                  elif t==2:
                    co = 1
                    jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
                if ((c3[0][t]==meio) and (jogar)):
                  ca = 1
                  li = 3
                  if t==0:
                    co = 3
                    jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
                  elif t==2:
                    co = 1
                    jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
                if ((c3[2][t]==meio) and (jogar)):
                  ca = 1
                  li = 1
                  if t==0:
                    co = 3
                    jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
                  elif t==2:
                    co = 1
                    jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)

             
        if ((c2[i][1] == marcacao) and (jogar)):
          meio = c2[i][1]
          if ((c1[i][g]==meio) and (jogar)):
            ca = 3
            li = i+1
            if g==0:
              co = 3
              jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
            elif g==2:
              co = 1
              jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
              
            if ((c3[i][g]==meio) and (jogar)):
              ca = 1
              li = i+1
              if g==0:
                co = 3
                jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
              elif g==2:
                co = 1
                jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)

        if ((c2[1][g] == marcacao) and (jogar)):
          meio = c2[1][g]
          if ((c1[i][g]==meio) and (jogar)):
            ca = 3
            co = g+1
            if i==0:
              li = 3
              jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
            elif i==2:
              li = 1
              jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
            
          if ((c3[i][g]==meio) and (jogar)):
            ca = 1
            co = g+1
            if i==0:
              li = 3
              jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
            elif i==2:
              li = 1
              jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)   

        if ((c3[i][g] == marcacao) and (jogar)):
          ca = 3
          co = g+1
          if ((c3[i][g] == c3[seguinte][g]== marcacao) and (jogar)):
            li = seguinte+2
            if li>=4:
              li -= 3
            jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
          if ((c3[i][g] == c3[posSeguinte][g]== marcacao) and (jogar)):
            li = seguinte+1
            if li>=4:
              li -= 3
            jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
          if ((c3[i][segc] == marcacao) and (jogar)):
            ca = 3
            li = i+1
            co = segc+2
            if co==4:
              co = 1
            jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
          if ((i<=1) and (c3[i][i] == c3[i+1][i+1] == marcacao) and (jogar)):
            ca = 3
            li = i+3
            co = i+3
            if co==4:
              li = 1
              co = 1
            jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
          if ((c3[0][0] == c3[2][2] == marcacao) and (jogar)):
            ca = 3
            li = 2
            co = 2
            jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
          if ((i==g==1) and (jogar)):
            ca = 3
            if ((c3[0][2]==c3[1][1]== marcacao) and (jogar)):
              li = 3
              co = 1
              jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
            if ((c3[2][0]==c3[1][1]== marcacao) and (jogar)):
              li = 1
              co = 3
              jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
          if ((c3[2][0]==c3[0][2]== marcacao) and (jogar)):
            ca = 3
            li = 2
            co = 2
            jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)

          
    if ((c1[0][0]== marcacao) and (jogar)):
      ca = 2
      if ((c3[0][2]== marcacao) and (jogar)):
        li = 1
        co = 2
        jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
      if ((c3[2][0]== marcacao) and (jogar)):
        li = 2
        co = 1
        jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)

    if ((c1[0][2]== marcacao) and (jogar)):
      ca = 2
      if ((c3[0][0]== marcacao) and (jogar)):
        li = 1
        co = 2
        jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
      if ((c3[2][2]== marcacao) and (jogar)):
        li = 2
        co = 3
        jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)

    if ((c1[2][0]== marcacao) and (jogar)):
      ca = 2
      if ((c3[2][2]== marcacao) and (jogar)):
        li = 3
        co = 2
        jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
      if ((c3[0][0]== marcacao) and (jogar)):
        li = 2
        co = 1
        jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)

    if ((c1[2][2]== marcacao) and (jogar)):
      ca = 2
      if ((c3[0][2]== marcacao) and (jogar)):
        li = 2
        co = 3
        jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
      if ((c3[2][0]== marcacao) and (jogar)):
        li = 3
        co = 2
        jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)


  #Caso não aja situação de vitória iminente em ambas as partes, o computador seguirá na estratégia com o próximo trecho 
  marcacao = " "+simcomp+" "
  for i in range (3):      
    for g in range (3):
      if ((c1[i][g]== marcacao) and (jogar)):
        ca = random.randrange(1,2)
        li = i+1
        co = g+1
        if ca==1:
          ca=3
        jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
       
      if ((c2[i][g]== marcacao) and (jogar)):
        ca = random.randrange(1,2)
        li = i+1
        co = g+1
        if ca==2:
          ca=3
        jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)

      if ((c3[i][g]== marcacao) and (jogar)):
        ca = random.randrange(1,2)
        li = i+1
        co = g+1
        jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)

      if ((c1[i][g]== marcacao) and (jogar)):
        ca = 1
        li = i+2
        co = g+1
        if li == 4:
          li = 1
        jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
        if jogar:
          ca = 1
          li = i+1
          co = g+2
          if co == 4:
            co = 1
          jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)

      if ((c2[i][g]== marcacao) and (jogar)):
        ca = 2
        li = i+2
        co = g+1
        if li == 4:
          li = 1
        jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
        if jogar:
          li = i+1
          co = g+2
          if co == 4:
            co = 1
          jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)

      if ((c3[i][g]== marcacao) and (jogar)):
        ca = 3
        li = i+2
        co = g+1
        if li == 4:
          li = 1
        jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
        if jogar:
          li = i+1
          co = g+2
          if co == 4:
            co = 1
          jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)

  #Se o computador for realizar sua primeira jogada, dará preferência à localização central do jogo, o meio da camada 2, pois é um lugar estratégicamente interessante
  if rodadas == 1:
    if c2[1][1] == "   ":
      ca = 2
      li = 2
      co = 2
      jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)


  #Se na primeira jogada do computador o lugar supracitado estiver ocupado ou nenhuma das jogadas anteriores puderem ser realizadas, ele se encarregará de fazer uma jogada no modo aleatório
  if jogar:
    while jogar:
      ca = random.randrange(1,4)
      li = random.randrange(1,4)
      co = random.randrange(1,4)

      c1j = c1[li-1][co-1]
      c2j = c2[li-1][co-1]
      c3j = c3[li-1][co-1]

      if ((ca==1) and (c1j == "   ")):
        jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
          
      elif ((ca==2) and (c2j == "   ")):
        jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)
    
      elif ((ca==3) and (c3j == "   ")):
        jogar = marcarCam(simcomp,ca,li,co,c1,c2,c3)


#Função que realiza a verificação do término da partida por vitória ou por empate
def verificaFim(c1,c2,c3,simpes,simcomp,jogadas):
  #Recebe as camadas
  #Recebe o símbolo da pessoa e do computador
  #Recebe o número de jogadas realizadas

  #Função que verifica qual foi o vencedor (se houver)
  def quemvenceu(ca,li,co,ganhou):
    #Recebe as coordenadas para verificar
    pessoa = (" "+simpes+" ")
    computador = (" "+simcomp+" ")
    if ca==1:
      if c1[li][co] == pessoa:
        c1[li][co] = ("\033[33m"+c1[li][co]+"\033[0;0m")
        mostrarCam(c1,c2,c3)
        ganhou = 1
        exibirmsg(ganhou)
      elif c1[li][co] == computador:
        c1[li][co] = ("\033[33m"+c1[li][co]+"\033[0;0m")
        mostrarCam(c1,c2,c3)
        ganhou = 2
        exibirmsg(ganhou)

    elif ca==2:
      if c2[li][co] == pessoa:
        c2[li][co] = ("\033[33m"+c2[li][co]+"\033[0;0m")
        mostrarCam(c1,c2,c3)
        ganhou = 1
        exibirmsg(ganhou)
      elif c2[li][co] == computador:
        c2[li][co] = ("\033[33m"+c2[li][co]+"\033[0;0m")
        mostrarCam(c1,c2,c3)
        ganhou = 2
        exibirmsg(ganhou)

    elif ca==3:
      if c3[li][co] == pessoa:
        c3[li][co] = ("\033[33m"+c3[li][co]+"\033[0;0m")
        mostrarCam(c1,c2,c3)
        ganhou = 1
      elif c3[li][co] == computador:
        c3[li][co] = ("\033[33m"+c3[li][co]+"\033[0;0m")
        mostrarCam(c1,c2,c3)
        ganhou = 2

    return ganhou

  #Função que exibe a mensagem de vitória, derrota ou empate
  def exibirmsg(n):
    tempoatraso = 0.5
    if n == 1:
      time.sleep(tempoatraso)
      print("\n\n-----------------------------------------------")
      print("\033[32m"+"----------------- Você ganhou! ----------------"+"\033[0;0m")
      print("-----------------------------------------------\n")
    elif n == 2:
      time.sleep(tempoatraso)
      print("\n\n-----------------------------------------------")
      print("\033[31m"+"----------------- Você perdeu! ----------------"+"\033[0;0m")
      print("-----------------------------------------------\n")
    elif n == 3:
      time.sleep(tempoatraso)
      print("\n\n-----------------------------------------------")
      print("\033[34m"+"------------------ Empatou! ------------------"+"\033[0;0m")
      print("-----------------------------------------------\n")

  ganhou = 0
  #Verificação da ocorrência de empate
  if jogadas == 27:
    ganhou = 3
    exibirmsg(ganhou)

  #Caso não haja empate, verificação de vitória ou derrota
  else:
    i=0
    while ((i<=2) and (ganhou == 0)):
      g=0
      while ((g<=2) and (ganhou == 0)):
        if (c1[i][g] == c2[i][g] == c3[i][g]):
          ca = 1
          li = i
          co = g
          ganhou = quemvenceu(ca,li,co,ganhou)
        g+=1
          
      if (c1[i][0] == c1[i][1] == c1[i][2]):
        ca = 1
        li = i
        co = 0
        ganhou = quemvenceu(ca,li,co,ganhou)
        
      if (c1[0][i] == c1[1][i] == c1[2][i]):
        ca = 1
        li = 0
        co = i
        ganhou = quemvenceu(ca,li,co,ganhou)
          
      if (c2[i][0] == c2[i][1] == c2[i][2]):
        ca = 2
        li = i
        co = 0
        ganhou = quemvenceu(ca,li,co,ganhou)
          
      if (c2[0][i] == c2[1][i] == c2[2][i]):
        ca = 2
        li = 0
        co = i
        ganhou = quemvenceu(ca,li,co,ganhou)
          
      if (c3[i][0] == c3[i][1] == c3[i][2]):
        ca = 3
        li = i
        co = 0
        ganhou = quemvenceu(ca,li,co,ganhou)
          
      if (c3[0][i] == c3[1][i] == c3[2][i]):
        ca = 3
        li = 0
        co = i
        ganhou = quemvenceu(ca,li,co,ganhou)


      if (c1[1][1] == c1[0][0] == c1[2][2]):
        ca = 1
        li = 1
        co = 1
        ganhou = quemvenceu(ca,li,co,ganhou)

      if (c1[1][1] == c1[0][2] == c1[2][0]):
        ca = 1
        li = 1
        co = 1
        ganhou = quemvenceu(ca,li,co,ganhou)

      if (c2[1][1] == c2[0][0]==c2[2][2]):
        ca = 2
        li = 1
        co = 1
        ganhou = quemvenceu(ca,li,co,ganhou)

      if (c2[1][1] == c2[0][2]==c2[2][0]):
        ca = 2
        li = 1
        co = 1
        ganhou = quemvenceu(ca,li,co,ganhou)

      if (c2[1][1] == c1[0][0]==c3[2][2]):
        ca = 2
        li = 1
        co = 1
        ganhou = quemvenceu(ca,li,co,ganhou)

      if (c2[1][1] == c1[0][2]==c3[2][0]):
        ca = 2
        li = 1
        co = 1
        ganhou = quemvenceu(ca,li,co,ganhou)

      if (c2[1][1] == c1[2][0]==c3[0][2]):
        ca = 2
        li = 1
        co = 1
        ganhou = quemvenceu(ca,li,co,ganhou)

      if (c2[1][1] == c1[2][2]==c3[0][0]):
        ca = 2
        li = 1
        co = 1
        ganhou = quemvenceu(ca,li,co,ganhou)

      if (c3[1][1] == c3[0][0]==c3[2][2]):
        ca = 3
        li = 1
        co = 1
        ganhou = quemvenceu(ca,li,co,ganhou)

      if (c3[1][1] == c3[0][2]==c3[2][0]):
        ca = 3
        li = 1
        co = 1
        ganhou = quemvenceu(ca,li,co,ganhou)

      if (c2[i][1] == c1[i][0]==c3[i][2]):
        ca = 2
        li = i
        co = 1
        ganhou = quemvenceu(ca,li,co,ganhou)

      if (c2[i][1] == c1[i][2]==c3[i][0]):
        ca = 2
        li = i
        co = 1
        ganhou = quemvenceu(ca,li,co,ganhou)

      if (c2[1][i] == c1[0][i]==c3[2][i]):
        ca = 2
        li = 1
        co = i
        ganhou = quemvenceu(ca,li,co,ganhou)

      if (c2[1][i] == c1[2][i]==c3[0][i]):
        ca = 2
        li = 1
        co = i
        ganhou = quemvenceu(ca,li,co,ganhou)
      
      i+=1

  return ganhou


#Função que mostra o placar e dá as opções de fim de partida
def fimPartida(placarpes,placarcomp):
  print("                     Placar                    ")
  print("-----------------------------------------------")
  print(" Você                Computador    | Empates")
  print("  ",placarpes,"         X         ",placarcomp,"        |   ",placaremp)
  print("-----------------------------------------------\n")

  escolher = True
  #Escolha da opção de fim da partida
  while escolher:
    final = int(input("Escolha uma opção:\n (1) Continuar Jogo\n (2) Reiniciar Jogo\n (3) Finalizar Jogo\nEu escolho a opção: "))
    if ((final==1) or (final==2) or (final==3)):
      escolher = False
    else: 
      print("\033[1m"+"\033[31m"+"\n                 Opção inválida\n"+"\033[0;0m")
    print()

  return final


#-------------------------------------------------------------


print("\033[34m"+"\n                Jogo da Velha 3D \n\n"+"\033[0;0m")
time.sleep(0.5)

placarpes = 0
placarcomp = 0
placaremp = 0
continuarjogo = True

while continuarjogo:
  resultado = 0
  jogadas = 0
  #Chamada da função de criar matrizes por cada camada
  c1 = criarMat(3,3,"   ")
  c2 = criarMat(3,3,"   ")
  c3 = criarMat(3,3,"   ") 

  escolherSimbolo = True
  while escolherSimbolo:
    simpes = int(input("Escolha uma opção de símbolo:\n (1) X\n (2) O\nEu escolho a opção: "))

    if (simpes==1):
      escolherSimbolo = False
      simpes="X"
      simcomp="O"
      print("Você escolheu o símbolo X",end="\n\n")

    elif (simpes==2):
      escolherSimbolo = False
      simpes="O"
      simcomp="X"
      print("Você escolheu o símbolo O",end="\n\n")

    else:
      print("\033[1m"+"\033[31m"+"\n                 Opção inválida\n\n"+"\033[0;0m")

  #Resultado == 0 significa que não houve vitória, derrota ou empate
  while resultado == 0:
    #Chamada da função de mostrar as camadas
    mostrarCam(c1,c2,c3)
    print("\n------------------- Sua Vez -------------------\n")
    #Chamada da função para solicitar a jogada por parte da pessoa
    jogaPes(simpes,c1,c2,c3)
    jogadas +=1

    #Se o número de jogadas for maior que 4, inicia-se a verificação de vitória, derrota ou empate 
    if jogadas > 4:
      resultado = verificaFim(c1,c2,c3,simpes,simcomp,jogadas)
    
    #Se ainda não houver vencedor, segue a partida
    if resultado == 0:
      #Chamada da função de mostrar as camadas
      mostrarCam(c1,c2,c3)
      print("\n-------------- Vez do Computador --------------\n")
      time.sleep(1)
      #Chamada da função para o computador realizar a jogada
      jogacomp(simcomp,simpes,jogadas,c1,c2,c3)
      jogadas +=1

      if jogadas > 4:
        resultado = verificaFim(c1,c2,c3,simpes,simcomp,jogadas)
    
    #Se o resultado for diferente de 0, significa que a partida chegou ao fim, seja por vitória ou empate
    if resultado != 0:

      #Se o resultado for 1, a pessoa ganhou, é somado o ponto ao seu placar
      if resultado == 1:
        placarpes +=1

      #Se o resultado for 2, o computador ganhou, é somado o ponto ao seu placar
      elif resultado == 2:
        placarcomp +=1

      #Se o resultado for 3, houve empate, é somado o ponto ao seu placar
      elif resultado == 3:
        placaremp +=1

      #Chamada da função de fim de partida
      finalizar = fimPartida(placarpes,placarcomp)

      #Se a opção escolhida pela pessoa for a 2ª (Reiniciar Jogo), os placares são zerados e é realizada a limpeza do console
      if finalizar == 2:
        placarpes = 0
        placarcomp = 0
        placaremp = 0
        try:
          os.system('clear')
        except:
          os.system('cls')

      #Se a opção escolhida pela pessoa for a 3ª (Finalizar Jogo), o programa agradece e se encerra  
      elif finalizar == 3:
        print("\033[34m"+"\n                     Até logo!\n"+"\033[0;0m")
        continuarjogo = False
