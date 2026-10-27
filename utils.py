def show_menu():
    # afficher les différentes options
    print("Bienvenue sur BlackCloverTT")
    print("1 - Lancer une partie")
    print("2 - Afficher le classement")
    print("3 - Quitter")

def valid_choice(choix):
        while choix < 1 or choix > 3:
        # Si le choix est pas compris entre 1 et 3
            print("Veuillez rentrer un chiffre valide")
        # retourne le choix
        else :
            return choix

def start_game():
    # selectionner un nom de joueur
    choose_name()
    # afficher les personnages disponible
    # choix des personnages de l'équipe
    # choix random de l'adversaire
    # systeme de combat
    # fin de partie
    ...

def create_team():
    # nom
    # equipe
    ...

def choose_name():
    while True :
        # Choisir son nom d'utilisateur
        print("Votre pseudo doit faire en 3 et 10 charactères")
        teamname = print(input("Quelles est votre pseudonyme"))
        # Verifier si le nom est valide
        valid_username(teamname)
        # pas valide, on recommence (boucle)
        ...

def valid_username(teamname):
    #tant que supérieur à 3 charactère et inferieur à 10 charactère 
    while len(teamname) >= 3 or len(teamname) <= 10:
        return teamname
    else:
        print("Le nom n'est pas valide")
            # retourn le nom 


def available_characters():
    # faire une liste vide
    # faire une boucle
    # incrémenter chaque personnage de la DB, dans la liste 
    ...

def show_available_characters():
    # faire une boucle
    # afficher chaque perso qui est disponible
    ...

def choose_characters():
    # Faire 3 fois (pour les 3 personnages)
        # utilisateur saisi son choix
        # verification de si son choix est valide
        # ajout dans une liste
        # suppresion dans l'autre
    ...

def  valid_characters():
    # verifier si le personnages est bien dans la db
    # verifier si le personnage n'a pas déjà été selectionner
    ...

def random_enemy():
    # importer random
    # randomiser dans la liste des enemy
    ...

def combat():
    # enemy afficher avec nombre de pv 
    # dégat equipe contre enemy
    # verifier si enemy mort
    # enemy attaquer equipe
    # verifier si equipe mort
    # si enemy mort 
        # donner un nouveau méchant
    # si equipe morte fin de partie
    # enregistrer le score
    # retourner au menu
    ...


def team_attack():
    # additionner toutes l'attaque de l'équipe 
    # diviser l'attaque par la défense de l'enemy
    # retourner les dégats
    ...

def enemy_attack():
    # prendre les dégats de l'enemy 
    # les faire infliger a la team
    ...

def equip_dead():
    # si l'equipe a 0 pv 
    # retourner Vrai
    ...

def enemy_dead():
    # si enemy à 0 pv
    # retourner Vrai
    ...


def show_classement():
    # Afficher 3 meilleurs parties jouer 
    ...
    


def main():
    # Affichage menu
    show_menu()

    choix = int(input("Que voulez-vous faire [1-3]?"))

    # Verifier le choix
    valid_choice(choix)

    # Lancer une partie
    if choix == 1:
        start_game()

    # Afficher le classement
    if choix == 2:
        show_classement()

    # Quitter
    if choix == 3:
        print("Aurevoir")
        quit()
    ...

main()