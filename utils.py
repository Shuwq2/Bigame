# MENU = [
#   "Lancer Jeu",
#   "Afficher les scores",
#   "Quitter",
#    ]
Menu = ["Lancer le Jeu",
        "Afficher les scores",
        "Quitter"]


# Menu
def menu():
#   Boucle sur tout element de MENU
    for index, valeur in enumerate(Menu):
#       afficher numero element et texte element
        print(f"{index}. {valeur}")

# Choix (options, erreur)
def choice(options, erreur):
#    while True:
    while True:
#       Recuperer choix utilisateur
        user_choice = input("Choisissez une option : [1 - 3]")
#        Verifier si choix est valide
        if choice_isvalid(user_choice):
            return user_choice
        #        Sinon
#             Lancer fonction erreur
        else:
            erreur()

def choice_isvalid(user_choice):
#        Si valide
        if user_choice ... :
#             return choix
                return user_choice

def erreur():
     print("Choix invalide. Veuillez réessayer.")

# Process
#    JEU
#       Crée son équipe
#           Choisir son pseudo
#               Boucle
    #               recuper choix utilisateur
    #               verifier choix utilisateur 
    #                   choix > 3 characteres et choix < 10 characteres
    #                   si il n'existe pas déjà
    #               enregistrer le choix
#           Choisir son équipe
#               Afficher les personnage disponible
#                   recuperer les personnages de la BD
#                       faire une boucle
#                       mettre dans une liste
#               Choisir un personnage 1 par 1
#                   Boucle
    #                   recuperer choix utilisateur
    #                   verifier si il est valide
    #                       si il est présent dans la liste
    #                       si n'est pas déjà dans l'équipe
    #                   ajouter dans la liste equipe
    #                   supprimer de la liste des personnages disponible
#         Choisir un ennemie au hasard
#         Combat (ennemie, equipe)
#           Boucle
#               l'equipe attaque l'ennemie
#                   addition de toutes l'atk des alliés divisier par la defense de l'ennemie
#               verifie si l'ennemie est mort
#                   si la vie de l'ennemy est <= 0, il est mort
#               Si il est mort
#                   ajoute 1 à vague
#                   choisir un ennemie au hasard
#               l'ennemie attaque l'equipe
#                   On enleve la vie du premier combatant correspondant à l'atk de l'ennemie
#               verifie si la team est morte
#                   si la vie de l'équipe est <= 0, l'équipe est morte
#          Enregistre le score
#               Enregistre le nombre de vague, l'équipe, dans la DB
#          Retour au Menu
#               
#          
#       
#       
#    Afficher les scores
#        Recuperer scores base
#            ouvrir base
#            acceder a collection score
#            find
#            convertir curseur en list
#        filtrer les 3 meilleurs
#             trie le tableau sur element.waves
#             prendre 3 derniers elements
#                    array[-3:-1]
#        Affiche les score
#    Quitter
#       sys.exit()


def main():
     menu()
     choice([1, 2, 3], erreur)

main()