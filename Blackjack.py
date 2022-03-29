from random import randrange
import os

cartes = [
'1-C','2-C','3-C','4-C','5-C','6-C','7-C','8-C','9-C','10-C','R-C','D-C','V-C',
'1-L','2-L','3-L','4-L','5-L','6-L','7-L','8-L','9-L','10-L','R-L','D-L','V-L',
'1-T','2-T','3-T','4-T','5-T','6-T','7-T','8-T','9-T','10-T','R-T','D-T','V-T',
'1-P','2-P','3-P','4-P','5-P','6-P','7-P','8-P','9-P','10-P','R-P','D-P','V-P'
]

cartesJoueur = []
cartesCasino = []
cagnotteJeux = [2000,2000]
misesJeux = [0,0]
scoresTab = [0,0]
Tour = 1

def genererCarte():
    carte = (cartes[randrange(len(cartes))])
    cartes.remove(carte)
    return carte

def recupererLesMises():
    global misesJeux
    global cagnotteJeux
    os.system('clear')
    print('██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗░░░░░██╗░█████╗░░█████╗░██╗░░██╗')
    print('██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝░░░░░██║██╔══██╗██╔══██╗██║░██╔╝')
    print('██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░░░░░░██║███████║██║░░╚═╝█████═╝░')
    print('██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░██╗░░██║██╔══██║██║░░██╗██╔═██╗░')
    print('██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗╚█████╔╝██║░░██║╚█████╔╝██║░╚██╗')
    print('╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝')
    miseJoueur = int(input('╰──> Vous Avez : ' + str(cagnotteJeux[1]) + ' Jetons / ───>  Votre Mise : '))
    while(miseJoueur>cagnotteJeux[1]):
        miseJoueur = int(input('( ! ) Vous Avez : ' + str(cagnotteJeux[1]) + ' Jetons / ───>  Votre Mise : '))
    cagnotteJeux[1] = cagnotteJeux[1] - miseJoueur
    misesJeux[1] = miseJoueur
    print("\n \n \n C'est Parti ! \n \n \n")

def demarrer():
    recupererLesMises()
    for i in range(2):
        cartesJoueur.append(genererCarte())
        cartesCasino.append(genererCarte())
    printLiveResultats()


def calculLiveValues():
    joueursTab = ['Joueur','Casino']
    for personne in joueursTab:
        monScore = 0
        mesCartes = eval('cartes'+personne)
        for i in range(len(mesCartes)):
            if(mesCartes[i].split('-')[0] in ['R','D','V'] ):
                monScore += 10
            else:
                monScore += int(mesCartes[i].split('-')[0])
        
        if personne == 'Casino' : scoresTab[0]=monScore
        else: scoresTab[1] = monScore


def uiCartes(personne):
    symTab = ['♥','♦','♣','♠']
    symTabNom = ['C','L','T','P']

    calculLiveValues()


    # Calc Casino Print Score
    casinoLastCardValue = cartesCasino[len(cartesCasino)-1].split('-')[0]
    if(casinoLastCardValue in ['R','D','V'] ):
        casinoLastCardValue = 10

    if(personne == 'Casino'):
            print('\n\n                 ╭── Casino Cartes & SCORE = ' + str(scoresTab[0] - int(casinoLastCardValue)) + ' ──╮ \n\n')

    for i in range(len(eval('cartes'+personne))):
        carte = eval('cartes'+personne)[i]
        carteNum = carte.split('-')[0] 
        carteSym = symTab[symTabNom.index(carte.split('-')[1])]
        if(carteNum != '10'):
            carteNum+=' '
        if((personne == 'Casino') & (i > 0)):
            carteNum = '# '
        print(
        '                           ╭───────╮ \n'
        +'                           │ '+carteSym+'     │ \n'
        +'                           │       │ \n'
        +'                           │   '+carteNum+'  │ \n'
        +'                           │       │ \n'
        +'                           │     '+carteSym+' │ \n'
        '                           ╰───────╯ \n'
        )
        
    if(personne == 'Joueur'):
            print('\n\n                 ╰── Vos Cartes & SCORE = ' + str(scoresTab[1]) + ' ──╯ \n\n')


def rejouer():
    global cartes
    global cartesJoueur
    global cartesCasino
    global scoresTab
    global misesJeux
    global Tour 
    Tour = 1
    cartesCasino = []
    cartesJoueur = []
    misesJeux = [0,0]
    scoresTab = [0,0]
    cartes = [
    '1-C','2-C','3-C','4-C','5-C','6-C','7-C','8-C','9-C','10-C','R-C','D-C','V-C',
    '1-L','2-L','3-L','4-L','5-L','6-L','7-L','8-L','9-L','10-L','R-L','D-L','V-L',
    '1-T','2-T','3-T','4-T','5-T','6-T','7-T','8-T','9-T','10-T','R-T','D-T','V-T',
    '1-P','2-P','3-P','4-P','5-P','6-P','7-P','8-P','9-P','10-P','R-P','D-P','V-P'
    ]
    demarrer()

def calculSum(listedecartes):
    Sum = 0
    for i in listedecartes:
        Sum += int(i)
    return Sum

def checkBlackJack(vcartes):
    bcartes = vcartes.copy()
    for i in range(len(bcartes)):
        bcartes[i] = str(bcartes[i]).split('-')[0]
        if(str(bcartes[i]).split('-')[0] in ['10','R','D','V']):
            bcartes[i] = '10'

    if((('1' in bcartes) & ('10' in bcartes ) & (len(bcartes) == 2)) or calculSum(bcartes) == 21):
        return True
    else: return False

def hit():
    cartesJoueur.append(genererCarte())
    uiCartes('Joueur')
    if(scoresTab[1] < 21):
        if(input('Encore ?, O / N ').upper() == 'O'):
            hit()
        else: stand()
    else:
        Bingo('Casino')

def stand():
    global Tour 
    Tour+=1
    cartesCasino.append(genererCarte())
    printLiveResultats()
    

def printLiveResultats():
    os.system('clear')
    calculLiveValues()

    if(Tour == 1):
        if(checkBlackJack(cartesCasino)): 
            Bingo('Casino')
        elif(checkBlackJack(cartesJoueur)) : 
            cagnotteJeux[1] = cagnotteJeux[1]  + (misesJeux[1]*2)
            Bingo('Joueur')

    if((int(scoresTab[0]) == 21) & (int(scoresTab[1] == 21))):
        Bingo('Egalite')
        
    if(int(scoresTab[0]) == 21):
        Bingo('Casino')
    elif(int(scoresTab[0]) > 21):
        cagnotteJeux[1] = cagnotteJeux[1]  + (misesJeux[1]*2)
        Bingo('Joueur')
    

    if(int(scoresTab[1]) == 21):
        cagnotteJeux[1] = cagnotteJeux[1]  + (misesJeux[1]*2)
        Bingo('Joueur')
    elif(int(scoresTab[1]) > 21):
        Bingo('Casino')

    
    print('\n\n')
    print(' ▶	▶	▶ 	▶     Tour ' + str(Tour) + ' 	◀	◀	◀	◀')


    uiCartes('Casino')
    print('⋰ ⋱ ⋰ ⋱ ⋰ ⋱ ⋰ ⋱ ⋰ ⋱ ⋰ ⋱ ⋰ ⋱ ⋰ ⋱ ⋰ ⋱ ⋰ ⋱ ⋰ ⋱ ⋰ ⋱ ⋰ ⋱ ⋰ ⋱ ⋰ ⋱ ⋰ ⋱ ⋰ ⋱ ⋰ ⋱ ⋰ ⋱	 \n')
    uiCartes('Joueur')

    if(votreChoix() == 1):
        hit()
    else: stand()



def Bingo(gagnant):
    global cagnotteJeux
    os.system('clear')
    print('	╳ 	╳ 	▒	▒	 ╳ 	╳ 	 F I N D E L A P A R T I E	╳ 	╳ 	▒	▒	 ╳ 	╳ 	 ')
    uiCartes('Casino')
    print('	╳ 	╳ 	╳	╳ 	╳ 	╳       ╳\n')
    uiCartes('Joueur')
    print('	╳ 	╳ 	▒	▒	 ╳ 	╳ 	 F I N D E L A P A R T I E	╳ 	╳ 	▒	▒	 ╳ 	╳ 	 ')

    scoreCasino = scoresTab[0]
    if((gagnant == 'Casino') & (scoresTab[0] == 11)):
        scoreCasino = 21
    
    scoreJoueur = scoresTab[1]
    if(gagnant == 'Joueur'):
        if (scoresTab[1] == 11):
            scoreJoueur = 21

    if(gagnant != 'Egalite'):
        print('')
        print('                 ┏━━━━ Fin de la partie ! ━━━┓')
        print('                 ┃                           ┃')
        print('                 ┣━━━━┫  ' +gagnant+ ' Gagne !      ┃')
        print('                 ┃                           ┃')
        print('                 ┣━━━━┫    Tours /  ' + str(Tour) + '        ┃')
        print('                 ┃                           ┃')
        print('                 ┣━ ━━┫ Score Casino ' + str(scoreCasino) + (('       ┃') if (len(str(scoreCasino))) < 2 else ('      ┃')) )
        print('                 ┣━ ━━┫ Score Joueur ' + str(scoreJoueur) + (('       ┃') if (len(str(scoreJoueur))) < 2 else ('      ┃')) )
        print('                 ┃                           ┃')
        print('                 ┃━━━━━┫ Votre Solde : '+str(cagnotteJeux[1])+'.')
        print('                 ┃')
        print('                 ┃')
    else:
        print('                 ┏━━━━ Fin de la partie !')
        print('                 ┃')
        print('                 ┣━━━━ Tours /  ' + str(Tour))
        print('                 ┃')
        print('                 ┣━━━━━━━┫ Égalité ! 21 / 21')
        print('                 ┃')
        print('                 ┃━━━━━┫ Votre Solde : '+str(cagnotteJeux[1])+'. ')
        print('                 ┃')
        print('                 ┃')
    if(cagnotteJeux[1] > 0):
        if(input('                 ┗━ ━ Continuer a Jouer ? ? O / N \n ').upper() == 'O'):
            rejouer()
        else: quit()    
    else:
        print('Pas plus de jetons ! Au Revoir.')
    


def votreChoix():
    print('\n\n')
    print('                  ╭──▶  A vous de jouer !   ──╮')
    print('                  │                           │')
    print('                  │        1 > [ Hit ]        │ ')
    print('                  │       2 > [ Stand ]       │')
    print('                  │                           │')
    print('                  │    ╭── Votre Choix  ◀─────╯')
    print('                  │    │                       ')
    print('                  │    │  JARRAR BlackJack     ')
    choix = 3
    while( choix > 2):
       choix = int(input('                  ╰────┴───────────────────▶ '))
    return choix



def jouer():
    demarrer()
    
    
# # # # # # # # # # # # # # # # # # # # # 

jouer()
