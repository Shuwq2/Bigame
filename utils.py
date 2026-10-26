def show_menu():
    # afficher les différentes options
    ...

def user_choice():
    # prendre le choix utilisateur 
    # verifier si le choix est valid
    # renvoyer le choix
    ...

def valid_choice():
    # Si le choix est bien compris entre 1 et 3
    # retourne le choix
    ...

def start_game():
    # selectionner un nom de joueur
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
    # Choisir son nom d'utilisateur
    # Verifier si le nom est valide
    # pas valide, on recommence (boucle)
    ...

def valid_username():
    # Si le nom est 
        # supérieur à 3 charactère et inferieur à 10 charactère 
        # retourn le nom 
    ...


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

