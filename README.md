# Jogo_da_Velha_3D_Terminal
Projeto de Jogo da Velha tridimensional desenvolvido em Python, permitindo que o humano jogue contra o algoritmo.
O jogo em 3 dimensões difere do jogo da velha tradicional no fato de ser possível ganhar não apenas se houver uma sequência de 3 símbolos iguais na sequência de linhas, colunas ou diagonais de cada camada do jogo, mas também em diagonais, linhas e colunas entre as camadas (entre as dimensões).

Requisitos:
1. Cada jogador deverá (usuário/humano e computador), a cada rodada, visualizar a tabela do jogo atualizada no terminal;
2. O usuário (jogador 1) deve poder escolher entre jogar com X ou com O. Ao computador (jogador 2), será atribuído o outro símbolo;
3. O usuário entrará sua jogada com as coordenadas da casa desejada, sendo na ordem camada, linha e coluna. (Ex. “1,3,2”, o que equivale à casa da coluna 2, da linha 3 da primeira camada do tabuleiro 3D). Esta entrada pode ser flexível (Ex. “1, 2, 2” = “1,2,2” = “1, 2, 2), mas a sequência camada, linha e coluna deve ser respeitada;
4. Toda entrada deverá ser validada (Ex. O computador não deve receber uma jogada como “1,5,2”). Caso uma entrada do usuário seja inválida, o computador deverá solicitar uma nova jogada válida até que esta seja dada como entrada;
5. Após a jogada do usuário, o computador deverá fazer a sua jogada, usando a seguinte estratégia (nessa ordem):
  5.1. Caso haja uma sequência de dois símbolos do computador, em qualquer linha, coluna ou diagonal, seguida de uma casa vazia, o computador deverá jogar nessa casa,     para ganhar a rodada, fazendo a sequência de três símbolos;
  5.2. Caso não haja situação de vitória iminente do computador, caso haja uma sequência de dois símbolos do adversário, em qualquer linha, coluna ou diagonal, seguida     de uma casa vazia, o computador deverá jogar nessa casa, para evitar que o usuário ganhe o jogo;
  5.3. Caso não haja situação de vitória iminente do usuário, o computador deve jogar em uma casa tal que se forme uma sequência de dois símbolos do computador, seguidos   de uma casa vazia, considerando linha, coluna ou diagonal;
  5.4. Caso não haja situação descrita no item (5.3), o computador deve jogar em qualquer casa de qualquer linha, coluna ou diagonal onde não haja nenhuma outra casa       ocupada (seja por símbolo do usuário ou do computador);
  5.5. Caso nenhuma das hipóteses anteriores seja plausível, o computador deve jogar em qualquer casa livre.
6. Após a jogada do computador, o usuário deverá realizar a sua nova jogada, seguido pelo computador, até que algum dos jogadores ganhe o jogo, ou que haja empate;
7. O computador deverá, desde quando o programa for executado até o usuário escolher terminar o programa, guardar o placar entre usuário e computador, contabilizando também os empates. No final de cada rodada, o computador deverá exibir o placar e perguntar se o usuário deseja jogar novamente. Se sim, o jogo é recomeçado.


*Esse programa foi utilizado como avaliação na componente "Fundamentos de Programação", da turma de 2021.1, na Universidade Federal do Ceará.*
