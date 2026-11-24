"""
faire un tableau pour chaque joueur et l'afficher
leur demander de placer leur bateau dans le tableau
placer leur bateau dans leur tableau respectif
demander ou il veulent frapper dans le tableau de leur adversaire
afficher le resultat de la frappe si touché ou non
enlever lemplacement ou il frappe de leur propre tableau si ils ont touché ou non
faire arreter la partie si le bateau est touché coulé
afficher le gagnant

"""



def creer_grille():
    tableau = [
        ["~", "~", "~", "~", "~"],
        ["~", "~", "~", "~", "~"],
        ["~", "~", "~", "~", "~"],
        ["~", "~", "~", "~", "~"],
        ["~", "~", "~", "~", "~"]
    ]

    return tableau

taille = 5
eau = "~"
bateau = "b"
tir_rate = "o"
tir_reussi = "x"


def afficher_grille(tableau):
    print("  0 1 2 3 4")

    for ligne in range(taille):
        print(ligne, end = " ")
        for colonne in range(taille):
            print(tableau[ligne][colonne], end = " ")
        print()


def placer_bateau(tableau, ligne, colonne):
    if verifier_coordonnees(ligne, colonne):
        if tableau[ligne][colonne] == eau:
            tableau[ligne][colonne] = bateau
            return True

    return False


def afficher_tableau(tableau):
    afficher_grille(tableau)


def verifier_coordonnees(ligne, colonne):
    return (0 <= ligne < taille and
            0 <= colonne < taille)


def verifier_frappe(tableau, ligne, colonne):
    if not verifier_coordonnees(ligne, colonne):
        return "coordonnees pas valides"

    if tableau[ligne][colonne] == bateau:
        tableau[ligne][colonne] = tir_reussi

        for rangee in tableau:
            if bateau in rangee:
                return "touche"

        return "coule"

    elif tableau[ligne][colonne] == eau :
        tableau[ligne][colonne] = tir_rate
        return "rate"

    else:
        return "deja visee"


def changer_joueur(joueur_actuel):
    if joueur_actuel == 1:
        return 2
    else:
        return 1


def afficher_gagnant(joueur_actuel):
    print("le joueur", joueur_actuel, "a gagne !")


# creer les grilles des deux joueurs
joueur1 = creer_grille()
joueur2 = creer_grille()

# nombre de bateaux par joueur
nombre_bateaux = 3


# placement des bateaux
for joueur in [1, 2]:

    if joueur == 1:
        tableau = joueur1
    else:
        tableau = joueur2

    print("joueur", joueur, "- Placement des bateaux")

    bateaux_places = 0

    while bateaux_places < nombre_bateaux:

        afficher_tableau(tableau)

        try:
            ligne = int(input("Ligne du bateau (0 a 4) : "))
            colonne = int(input("Colonne du bateau (0 a 4) : "))

            if placer_bateau(tableau, ligne, colonne):
                bateaux_places += 1
                print("Bateau place ")
            else:
                print("Case invalide ou deja occupee.")

        except ValueError:
            print("Entre des nombres entiers.")


joueur_actuel = 1
partie_terminee = False


while not partie_terminee:

    print("=" * 30)
    print("Tour du joueur", joueur_actuel)

    # selectionner tableau de lautre
    if joueur_actuel == 1:
        tableau_adverse = joueur2
    else:
        tableau_adverse = joueur1

    # afficher grille de lautre sans reveler bateaux
    grille_visible = creer_grille()

    for ligne in range(taille):
        for colonne in range(taille):

            case = tableau_adverse[ligne][colonne]

            if case == tir_rate:
                grille_visible[ligne][colonne] = tir_rate

            elif case == tir_reussi:
                grille_visible[ligne][colonne] = tir_reussi

    print("Grille adverse :")
    afficher_tableau(grille_visible)

    try:
        ligne = int(input("Ligne ciblee (0 a 4) : "))
        colonne = int(input("Colonne ciblee (0 a 4) : "))

        # regardé si coordonnees ok
        if not verifier_coordonnees(ligne, colonne):
            print("Coordonnees invalides. Recommencez.")

        else:

            resultat_frappe = verifier_frappe(tableau_adverse, ligne, colonne)

            if resultat_frappe == "deja visee":
                print("Cette case a deja ete visee.")

            else:

                print("Resultat de la frappe :", resultat_frappe)

                # reste til des bateau?
                bateaux_restants = False

                for rangee in tableau_adverse:
                    for case in rangee:
                        if case == bateau:
                            bateaux_restants = True

                # bateau coulé ?
                if bateaux_restants == False:
                    partie_terminee = True
                    afficher_gagnant(joueur_actuel)

                else:
                    input("Appuyez sur Entree pour passer au joueur suivant...")
                    joueur_actuel = changer_joueur(joueur_actuel)

    except ValueError:
        print("Entre des nombres entiers.")


# afficher grilles finales
print("Fin de la partie")

print("Grille finale du joueur 1 :")
afficher_tableau(joueur1)

print("Grille finale du joueur 2 :")
afficher_tableau(joueur2)

print("Merci d'avoir joue !")


