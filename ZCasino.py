from random import randrange
from math import ceil
continuer="O"
argent=500
a=1
b=1
while continuer=="O":
    print("Vous disposez de",argent,"$.\n\nFaites vos jeux !\n")
    while a==1:
        mise=input("Choisissez combien vous souhaitez miser : ")
        try:
            mise=int(mise)
            assert 0<mise<=argent
        except ValueError:
            print("Vous n'avez pas saisi un nombre.")
        except AssertionError:
            print("Veuillez saisir une valeur entre 1 et",argent,".")
        else:
            a=0
    while b==1:
        choix=input("Choisissez un nombre entre 0 et 49 : ")
        try:
            choix=int(choix)
            assert 0<=choix<=49
        except ValueError:
            print("Vous n'avez pas saisi un nombre.")
        except AssertionError:
            print("Veuillez saisir une valeur entre 0 et 49.")
        else:
            b=0
    gagnant=randrange(50)
    print("\nLes jeux sont faits !\n\nRien ne va plus !\nLa bille est tombée sur le",gagnant,"\n")
    a=1
    b=1
    if choix==gagnant:
        argent+=ceil(3*mise)
        print("Bravo, vous récupérez votre mise et gagnez",ceil(3*mise),"$ !")
        continuer=input("\nVoulez-vous continuer ? (O/N) ")
    elif choix%2==gagnant%2:
        argent+=ceil(0.5*mise)
        print("Bonne couleur, vous récupérez votre mise et gagnez",ceil(0.5*mise),"$ !")
        continuer=input("\nVoulez-vous continuer ? (O/N) ")
    else:
        argent-=mise
        if argent>0:
            print("Oh non ! Vous perdez votre mise :(\nRejouez vite, vous allez vous refaire !")
            continuer=input("\nVoulez-vous continuer ? (O/N) ")
        else:
            continuer="N"
            print("Oh non ! Vous perdez votre mise :(\nVous avez perdu tout votre argent, à la prochaine !")
