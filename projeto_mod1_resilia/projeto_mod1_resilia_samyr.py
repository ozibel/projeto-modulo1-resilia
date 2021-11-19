def boas_vindas():
    print('= Bem Vindo ao Jogo RESGATE SILVESTRE ='.center(100, '|'))
def recomeço_boas_vindas():
    print('= Jogo RESGATE SILVESTRE ='.center(100, '|'))
    print(''' 
        Começo disse anteriormente, o jogo te leva em uma aventura pela Mata Atlântica para viver os desafios de
            proteger nossos animais em extinção e conhecer mais a biodiversidade do Brasil. 
        Todos os pontos do jogo serão revertidos para instituições que realizam trabalho de resgate, denúncia e 
            proteção animal.

        A sua missão é salvar  o Mico-Leão Dourado, a Onça-pintada, a Arara Azul e Preguiça de Coleira dos perigos
            dos caçadores, traficantes e comércio ilegal.
        Você pode escolher entre: Veterinário, Bióloga e Protetor das Florestas. As armas serão diferentes
         ''')
def decoraçao():
    print("= TENHA UM BOM JOGO! =".center(70, '-'))
def mostra_personagem_escolhido(personagem): # Como eu vou apenas mostrar ao usuário a escolha dele, não preciso retornar nada de fato.
    if personagem == 'v':
        print('\n Personagem Veterinário Rafael Caapora escolhido!')
    elif personagem == 'b':
        print('\n Personagem Bióloga Cauane Mangabeira escolhido!')
    else:
        print('\n Personagem Protetor Florestal Ozibel Ubiratan escolhido!')
def escolha_fim_de_jogo():
    letra_minuscula = input('O que você deseja fazer? [S] para finalizar e sair do jogo OU [R] para ' 
            'Recomeçar o jogo a partir das escolhas de personagem: ')            
    escolha_fim_de_jogo = letra_minuscula.upper()
    print(escolha_fim_de_jogo)
    return escolha_fim_de_jogo # Graças a aula 12 consegui o return (eu não estava recebendo a função em uma NOVA variável)
def qual_person(): # Input com opções de personagens + convertendo uma possível string maiuscula para minuscula
    escolha_de_personagem = input('\nEscolha UM dos 3 personagens, antes de começar o jogo. Para o personagem Veterinário'
        '\nRafael Caapora digite [V], a personagem Bióloga Cauane Mangabeira digite [B] ou'
        '\npersonagem Protetor Florestal Ozibel Ubiratan digite [P]: ')
    escolha_de_personagem = escolha_de_personagem.lower()
    return escolha_de_personagem
def escolha_opçao_da_fase(texto):
    opçoes_fase = input(texto)
    recebendo_opçao_fase = opçoes_fase.lower()
    return recebendo_opçao_fase
# Funções sendo chamada dentro da função loops_bloco3fases(). As Funções são chamadas de acordo com a opção de escolha do usuário
def caso_opçao_certa(msg_de_pontuaçao_obtida):  
    print(f'parabéns! Sua pontuação é {msg_de_pontuaçao_obtida} pontos.')
def caso_opçao_errada(msg_de_pontuaçao_):
    print(f'Infelizmente sua pontuação é {msg_de_pontuaçao_} pontos. Você voltou para a fase 1!')
    print('SUA VIDA SERÁ UM LOOP SE FICAR FAZENDO ESCOLHAS INADEQUADAS,\nSEMPRE DOIS PASSOS ATRÁS, NO CASO AQUI,'
          ' TRÊS FASES ATRÁS!')
# Esse WHILE vai acontecer as CONDICIONAIS/ESCOLHAS do usuário, determinando o destino dele até o fim do jogo
# IF/SE errar em qualquer uma das fases volta para o início da FASE1
def loops_bloco3fases(text1, text2, text3):

    pontos = 0                     # Contador das pontuações
    resultado = "bora"              # variável RESULTADO="bora" vai ser o indicador das fases se ele vai recomeçar do "zero" ou não
    while (resultado == "bora"):     # LOOP 1
        opçEscolhida1 = input(text1) # Usuário/personagem entra com sua ESCOLHA de caminho a seguir na fase 1
    
    # As 2 primeiras condicionais de cada fase da pra fazer uma DEF, será? 
        if opçEscolhida1 == 'a':
            pontos += 0
            caso_opçao_certa(pontos) # apresenta os PONTOS totais obtidos com as escolha dessa opção
            resultado = "fase2"
            opçoes_fase2 = escolha_opçao_da_fase(text2)
            
        elif opçEscolhida1 == 'b':
            pontos += 500
            caso_opçao_certa(pontos) # apresenta os PONTOS totais obtidos com a escolha dessa opção
            resultado = "fase2"
            opçoes_fase2 = escolha_opçao_da_fase(text2)
            
        elif opçEscolhida1 == 'c':
            pontos += 200
            caso_opçao_certa(pontos) # apresenta os PONTOS totais obtidos com a escolha dessa opção
            resultado = "fase2"
            opçoes_fase2 = escolha_opçao_da_fase(text2)
            
        elif opçEscolhida1 == 'd':
            pontos -= 300
            #pontos = int(pontos)
            print(f'Essa atitude não é legal! Você ganhou {pontos} pontos')
        
            resultado = "bora"
            
        else:
            print('opção inválida. escolha b, c ou d.')# Caso o usuário faça a GRACINHA de digitar qualquer outra coisa
    # FASE 2 -------------------------------------------------------------------------------------
        while (resultado == "fase2"):  # LOOP 2 > Só prosseguirá com base no resultado da fase 1
            if opçoes_fase2 == 'a':
                pontos -= 300
                print(f'Essa atitude não é legal! Você ganhou {pontos} pontos')
                resultado = "bora"
                
            elif opçoes_fase2 == 'b':
                pontos += 0
                print(f'Essa atitude não é legal! Você ganhou {pontos} pontos')
                resultado = "bora"
                
            elif opçoes_fase2 == 'c':
                pontos += 300
                caso_opçao_certa(pontos) # apresenta os PONTOS totais obtidos com as escolha dessa opção
                resultado = "fase3"
                opçoes_fase3 = escolha_opçao_da_fase(text3)
                
            elif opçoes_fase2 == 'd':
                pontos += 100
                print(f'Essa atitude não é legal! Você ganhou {pontos} pontos')
                resultado = "bora"
            
            else:
                print('opção inválida. escolha a, b, c ou d.')# Caso o usuário faça a GRACINHA de digitar qualquer outra coisa       
                resultado = "fase2"
                opçoes_fase2 = escolha_opçao_da_fase(text2)
                # opçoes_fase2 = input(text2) # Usuário/personagem entra com sua ESCOLHA de caminho a seguir na fase 2
                # opçoes_fase2 = opçoes_fase2.lower()
    # FASE 3 -------------------------------------------------------------------------------------
            while (resultado == "fase3"):   # LOOP 3 > Só prosseguirá com base no resultado da fase 2
                if opçoes_fase3 == 'a':
                    pontos -= 300
                    print(f'Essa atitude não é legal! Você ganhou {pontos} pontos')
                    resultado = "bora"
                    
                elif opçoes_fase3 == 'b':
                    pontos += 500
                    caso_opçao_certa(pontos) # apresenta os PONTOS totais obtidos com as escolha dessa opção
                    resultado = "fim"
                    
                elif opçoes_fase3 == 'c':
                    pontos += 200
                    caso_opçao_certa(pontos) # apresenta os PONTOS totais obtidos com as escolha dessa opção
                    resultado = "fim"
                    
                elif opçoes_fase3 == 'd':
                    pontos -= 100
                    print(f'Essa atitude não é legal! Você ganhou {pontos} pontos')
                
                    resultado = "bora"
                else:
                    print('opção inválida. escolha a, b ou c.')# Caso o usuário faça a GRACINHA de digitar qualquer outra coisa
                    resultado = "fase2"
                    opçoes_fase3 = escolha_opçao_da_fase(text3)
                    # opçoes_fase3 = input(text3) # Usuário/personagem entra com sua ESCOLHA de caminho a seguir na fase 2
                    # opçoes_fase3 = opçoes_fase3.lower()
# FIM da FUNÇÃO com as CONDICIONAIS das 3 fases---------------------------------------------------

boas_vindas()
print(''' 
    O jogo te leva em uma aventura pela Mata Atlântica para viver os desafios de proteger nossos
        animais em extinção e conhecer mais a biodiversidade do Brasil. 
    Todos os pontos do jogo serão revertidos para instituições que realizam trabalho de resgate,
        denúncia e proteção animal.

    A sua missão é salvar  o Mico-Leão Dourado, a Onça-pintada, a Arara Azul e Preguiça de Coleira
        dos perigos dos caçadores, traficantes e comércio ilegal.
    Você pode escolher entre: Veterinário, Biólogo e Protetor da Florestas. As armas são diferentes para cada personagem.
         ''')
# LOOP PRIMÁRIO: Contendo a chamada da Função de escolhas de personagem, a Função com as fases para cada personagem e as escolhas de fim de jogo.
escolha = 'R'           # [R] de RECOMEÇAR o jogo e [S] de SAIR
while escolha != 'S':  
    if escolha == 'R':
        
        escolha_personagem = qual_person() # Input com opções de personagens e convertendo uma possível string maiuscula para minuscula
        
        while escolha_personagem != 'v' and escolha_personagem != 'b' and escolha_personagem != 'p':
        
            escolha_personagem = qual_person() # Input com opções de personagens e convertendo uma possível string maiuscula para minuscula
        mostra_personagem_escolhido(escolha_personagem)      
        # print("Personagem " + escolha_personagem + " escolhido.")        
        tem_duvida = input("Tem certeza da sua escolha, se sim digite [0], se quer trocar de personagem digite [1] ou qualquer caracter: ")
        if tem_duvida == '0': #Resposta é não(0), então mostra a saudação, pula o LOOP de dúvidas e segue para começar o jogo.
            decoraçao() 
                        
        ''' Estrutura de repetição: Enquanto o usuário estiver em dúvida, a pergunta continuará se repetindo.. '''
        while tem_duvida != '0':
            
            if tem_duvida == '0': #Resposta é não(0), então mostra a saudação e sai do LOOP de dúvidas.
                decoraçao()             
            else :
                escolha_personagem = qual_person() # Input com opções de personagens e convertendo uma possível string maiuscula para minuscula
                
                if escolha_personagem == 'v' or escolha_personagem == 'b' or escolha_personagem == 'p':
                    mostra_personagem_escolhido(escolha_personagem)
                    # print("Personagem " + escolha_personagem + " escolhido.")
                    tem_duvida = input("Tem certeza da sua escolha, se sim digite [0], se quer trocar de personagem digite [1]: ")
                    if tem_duvida == '0':
                        decoraçao()
       
                else:
                    print('Escolha inválida, meu jovem!!!')
                    tem_duvida = '1'            
        # Glória, acabou a dúvida-----------------------------------------------------------------------------
        
        if escolha_personagem == 'v':
            print('\nPor ser um especialista em animais silvestres, explore as florestas para encontrar animais feridos e presos em armadilhas.'
                '\nA missão é proteger, resgatar e curar os animais. O seu maior vilão é o Caçador Corvo.')
            loops_bloco3fases(''' 
                Estamos no ambiente floresta e logo percebe-se que o caçador Corvo está indo em direção a preguiça de Coleira que
                está presa na árvore, o que parece bem comum, mas o que não é comum é ela está em volta de cordas presa na árvore, 
                já as duas Onças-pintadas se encontram em jaulas.
                Então, sabendo-se que o caçador está com um machado fortemente letal, o que você pretende fazer?
                
                [a] Salvar o Preguiça de Coleira apesar da proximidade do caçador.
                [b] Atacar o Corvo com uma pedra grande e tentar salvar todos os animais
                (pensou em Davi e Golias? Pois é apenas uma mera coincidência :D ).
                [c] Salvar as Onças-pintadas que estão nas jaulas e longe do caçador.
                [d] Fugir pois não se sente capacitado.
                
                >>> ''','Mesmo que ache que tenha sido pouco, a sua ajuda foi bem crucial lá atrás.'
                '\nEspera, isso não é nada bom...'
                '\nNão, não a sua atitude. O Mico-Leão Dourado está preso na árvore, certo, isso também parece comum, no entanto, ele'
                '\n está preso envolta de uma rede e parece que o Corvo não está presente. Faça uma escolha: '
                '\n\n[a] Fugir pois o caçador Corvo pode está à espreita.' # -300
                '\n[b] Esperar o caçador voltar para atacá-lo e libertar o Mico-Leão. ' #0
                '\n[c] Esperar o caçador voltar, esperar ele dormir e depois libertar o animal.' # +300
                '\n[d] Tentar libertar o Mico-Leão Dourado agindo rapidamente.' # +100
                '\n\n>>> ',
                '\nÉ isso aí! Vamos para o centro de reabilitação, o seu objetivo é levar o maior número de '
                'animais para o centro.\nMas cuidado! Pois os Caçadores podem tentar impedir o seu trabalho. Ao finalizar, os pontos'
                '\nacumulados serão doados para a causa animal. Você consegue!'
                '\n\nCerto, você recebeu uma comunicação do Protetor Florestal Ozibel Ubiratan dizendo que recebeu uma comunicação'
                '\ndo colega de um amigo que o caçador Corvo está a espreita próximo do centro de reabilitação. Tome uma atitude:'
                '\n\n[a] Não confia nessa história de “um amigo de um amigo” e segue em frente.' # GAME OVER -300
                '\n[b] Acredita na comunicação, mas logo lembra que tem em sua bolsa uma seringa sonífera e segue' #EVOLUI +500
                '\nem frente para tentar atacar e prender o caçador.'
                '\n[c] Acredita na comunicação  e dar a volta indo pelo caminho mais longo a esquerda.' # CONTINUA +200
                '\n[d] Acredita na comunicação e dar a volta indo pelo caminho mais longo a direita.' # GAME OVER -100
                '\n\n>>> ')
            
            escolha = escolha_fim_de_jogo()
            if escolha == 'R':
                recomeço_boas_vindas()
        elif escolha_personagem == 'b':
            
            print('\nComo bióloga perita em catalogação de espécies, educação e perícia ambiental, atue dentro e na borda'
                ' das florestas.\nA missão é proteger, resgatar e reintroduzir os animais, e o seu maior vilão são os compradores ilegais.')
            
            loops_bloco3fases('\nBem na borda da floresta há uma feira de vendas, logo percebe-se que tem animais enjaulados para a venda e são dois '
                '\nvendedores ilegais e alguns compradores. Sabendo-se que os compradores possam estar com armas'
                '\nnão letais (facões, armas de dardos...), qual destino seguirá:'
                '\n\n[b] Esperar que os dois vendedores estejam distraído e um pouco afastados para tentar'
                '\npegar e levar os animais para o centro de resgate.' # EVOLUI +500
                '\n[c] Esperar que um deles se afaste e o outro se distraia, tornando uma “luta” justa e tentar'
                '\nlevar os animais para o centro de resgate.' #(elu consegui mas não consegue todos os animais) CONTINUA +200
                '\n[d] Não se envolver, é claro, até porque são dois contra um ou até mais se estiverem escondidos! ' # GAME OVER -300
                
                '\n\n>>> ',
                '\nLegal, avançamos para dentro da floresta e mesmo que ache que tenha sido pouco,\na sua ajuda foi bem crucial na borda da floresta.'
                ' Espera, isso não é nada bom...\nNão, não a sua atitude (isso, talvez, possa parecer um Déjà vu, é normal!).'
                '\nA Arara Azul está presa na árvore envolta de uma rede, o Mico-Leão Dourado e a Preguiça de Coleira estão enjaulados,'
                '\nmas parece que o Corvo não está presente. Faça uma escolha:'
                '\n\n[a] Fugir pois os traficantes podem está à espreita!' # -300 GAME OVER
                '\n[b] Esperar os traficantes voltarem para atacá-los e libertar os animais. ' # 0 GAME OVER
                '\n[c] Esperar os traficantes voltarem, esperar eles dormirem e depois libertar os animais.'# +300  EVOLUI
                '\n[d] Tentar libertar os animais agindo rapidamente.' # +100 GAME OVER
                '\n\n>>> ',
                '\nÉ isso aí! Vamos reintroduzir o maior número de animais na floresta, mas cuidado,'
                '\npois os traficantes podem tentar impedir o seu trabalho. Ao finalizar, os pontos acumulados'
                '\nserão doados para a causa animal. Você consegue!\n'
                '\nCerto, você recebeu uma comunicação do Protetor Florestal Ozibel Ubiratan dizendo que recebeu uma comunicação'
                'do colega \nveterinário Caapora que um amigo de um amigo disse que o caçador Corvo está à espreita próximo dos'
                '\nlocais de reintrodução animal. Tome uma atitude:'
                '\n\n[a] Não confia nessa história de “um amigo de um amigo” e segue em frente para reintroduzir'
                '\ntodos os animais na savana.' # -300 GAME OVER
                '\n[b] Acredita na comunicação, mas logo lembra que tem em sua bolsa uma corda mágica,'
                '\ndecide seguir em frente e ficar preparado para tentar atacar e prender os traficantes.'
                '\nE mais a frente introduzir a Arara Azul e a Onça Pintada no pantanal, e os outros animais'
                '\n(Mico-Leão Dourado e Preguiça de Coleira) na floresta savana.' # EVOLUI +500
                '\n[c] Acredita na comunicação e espera dois dias para reintroduzir os animais na floresta savana' #CONTINUA +200
                '\n[d] Acredita na comunicação, mas logo lembra que tem em sua bolsa uma corda'
                '\nmágica, decide seguir em frente e ficar preparado para tentar atacar e prender os traficantes.'
                '\nE mais a frente introduzir a Onça Pintada no manguezal e os outros animais'
                '\n(Mico-Leão Dourado, Arara Azul e Preguiça de Coleira) na Savana' # GAME OVER -100
                '\n\n>>> ')
            escolha = escolha_fim_de_jogo()
            if escolha == 'R':
                recomeço_boas_vindas()
        elif escolha_personagem == 'p':
            print('\nEi! Por ser extremamente conectado com a floresta, proteja e resgate os animais dos caçadores e trafincantes!!'
                '\nO seu maior vilão é o Traficante El Diablo')
            loops_bloco3fases("texto FASE 1 + opções A, B, C: ","texto FASE 2 + opções A, B, C: ", "texto FASE 3 + opções A, B, C ou D: ")
            escolha = escolha_fim_de_jogo()
            if escolha == 'R':
                recomeço_boas_vindas()
    else:
        escolha = input(''' 
            Ei amigo, as escolhas são [S] OU [R], falou!? O que você deseja fazer? [S] para finalizar e sair do jogo OU 
            [R] para Recomeçar o jogo a partir da escolha de personagem: 
             ''')
        escolha = escolha.upper()
        if escolha == 'R':
            recomeço_boas_vindas()





# Dia 19