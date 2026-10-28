from db_init import *
import sys
import random

# MENU = [
#   "Lancer Jeu",
#   "Afficher les scores",
#   "Quitter",
#    ]
MENU = ["Lancer le Jeu",
        "Afficher les scores",
        "Quitter"]


# Menu
def menu():
#   Boucle sur tout element de MENU
    for index, valeur in enumerate(MENU):
#       afficher numero element et texte element
        print(f"{index + 1}. {valeur}")

def is_int(choice):
    try:
        int(choice)
        return True
    except:
        return False


def is_in_range(value,min,max):
    return min <= value <= max

def is_valid_choice(choice,option):
    if not is_int(choice):
         return False
    if not is_in_range(int(choice),1, len(option)):
        return False
    return True



# Choix (options, erreur)
def get_choice(options, erreur):
   from InquirerPy import inquirer
   from InquirerPy.base import Choice

   while True:
       user_choice = inquirer.select(message ="Choisissez une action", choices=[Choice("start", "Lancer le jeu"),Choice ("lead", "Afficher les scores"),Choice ("quit", "Quittez le Jeux"),]).execute
       return user_choice
    #    Verifier si choix est valide
    #    if is_valid_choice(user_choice, options):
    #        return int(user_choice)
    #     #    Sinon
    #     # Lancer fonction erreur
    #    erreur()


def erreur():
     print("Choix invalide. Veuillez réessayer.")

# Process
#    JEU


def is_valid_pseudo(pseudo):
#    choix > 3 characteres et choix < 10 characteres
#    si il n'existe pas déjà
     if len(pseudo) < 3 or len(pseudo) > 10:
          return erreur()
     return True

def choose_pseudo():
    #               Boucle
    while True:
#       recuper choix utilisateur
        pseudo = input("Choisissez un pseudo (3 - 10 charactères) : ")
#       verifier choix utilisateur 
        if is_valid_pseudo(pseudo):
            return pseudo


def create_player():
#   Choisir son pseudo
    pseudo = choose_pseudo()
    return pseudo

def available_characters():
    CHARACTERS = []
    curseur = db.heros.find({},{"_id": 0, "nom": 1, "HP": 1, "attaque": 1, "defense": 1})
#   faire une boucle
#   mettre dans une liste
    for character in curseur:
        CHARACTERS.append(character)
    return CHARACTERS



def show_available_characters(characters):
    i = 1
#   recuperer les personnages de la BD
    for c in characters:
        print(f"{i}.{c['nom']} | Attaque: {c['attaque']} | Défense: {c['defense']} | Vie: {c['HP']}\n")
        i = i + 1

def team_is_full(team):
     if len(team) == 3:
          return True

def choose_characters(characters,team):
    CHARACTERS = available_characters()
#   Boucle
#   Choisir un personnage 1 par 1
    while not team_is_full(team):
#   recuperer choix utilisateur
#       verifier si il est valide
#       si il est présent dans la liste
        chosen_option = get_choice(CHARACTERS, erreur)
        chosen_option -= 1
#           ajouter dans la liste team
        team.append(characters[chosen_option])
#           supprimer de la liste des personnages disponible
        characters.pop(chosen_option)
        print(team)

def create_team():
#           Choisir son équipe
#               Afficher les personnage disponible
                team = []
                characters = available_characters()
                show_available_characters(characters)
                choose_characters(characters,team)
                return team

def get_monsters():
    MONSTER = []
    curseur = db.monsters.find({},{"_id": 0, "nom": 1, "HP": 1, "attaque": 1, "defense": 1})
     #   faire une boucle
     #   mettre dans une liste
    for monstre in curseur:
        MONSTER.append(monstre)
    return MONSTER

def get_random_enemy(liste_monsters):
    monstre = random.choice(liste_monsters)
    return monstre

def is_alive(characters):
#    Si la vie du personnage est supérieur à 0 il est en vie
    if characters["HP"] > 0:
        return True
    else:
        return False

def team_is_dead(team):
#   verifie si la team est morte
#   si la vie de l'équipe est <= 0, l'équipe est morte
    for characters in team:
        if is_alive(characters):
            return False
    return True

def enemy_is_dead(enemy):
#   si la vie de l'ennemy est <= 0, il est mort
    if enemy["HP"] <= 0:
        return True
    else:
        return False

def show_etat_fight(team, enemy):
    for character in team:
          print(f"{character['nom']}, HP : {character['HP']}")
    print(f"{enemy['nom']},{enemy['HP']}")

def count_damage(striker, defender):
    # Calculer les dégats de l'attaque en fonction de la défense de l'ennemi
    degats = striker["attaque"] - defender["defense"]
    # Si les dégats sont inferieur à 1 on met les dégat aléatoire 
    if degats < 1:
        degats = 2 * random.randint(1, 10 )
    return degats

def hit_enemy(team, enemy):
     for characters in team:
        # Si il est en vie lui faire des dégats
        if is_alive(characters):
            degats = count_damage(characters, enemy)
            enemy["HP"] -= degats
            print(f"{characters['nom']} attaque {enemy['nom']} et inflige {degats} points de dégats !")

def hit_team(team, enemy):
 # Récupérer uniquement les membres vivants
    characters_alives = [c for c in team if is_alive(c)]
    # Choisir un membre vivant de l'équipe au hasard pour l'attaquer
    character = random.choice(characters_alives)
    degats = count_damage(enemy, character)
    character["HP"] -= degats
    print(f"{enemy['nom']} attaque {character['nom']} et inflige {degats} points de dégat !")
    if not is_alive(character):
        print(f"{character['nom']} est mort !")

def start_fight(enemy, team):
#          Boucle
    while not enemy_is_dead(enemy) and not team_is_dead(team):
        show_etat_fight(team, enemy)
#               l'equipe attaque l'ennemie
        hit_enemy(team, enemy)
#               verifie si l'ennemie est mort
#               Si il est mort
        if not enemy_is_dead(enemy):
#               l'ennemie attaque l'equipe
            hit_team(team, enemy)

def start_battle(enemy, team):
        waves = 1
        liste_monsters = get_monsters()

        while True:
            enemy = get_random_enemy(liste_monsters)
            start_fight(enemy, team)

            if team_is_dead(team):
                 print(f"Vous avez perdu à la vagues {waves}")
                 break
            else :
                 waves += 1
        return waves

def save_score(team_name, score):
    new_attemp = {
            "pseudo": team_name,
            "vagues" : score
        }
    db.scores.insert_one(new_attemp)
        
def start_game():
#       Crée un joueur
        team_name = create_player()
#       Crée une équipe
        team = create_team()
#       Choisir un ennemie au hasard
#       Combat (ennemie, equipe)
        score = start_battle(team_name, team)
#          Enregistre le score
        save_score(team_name, score)
#               Enregistre le nombre de vague, l'équipe, dans la DB

def get_score():
            liste_score = []
#           ouvrir base
#           acceder a collection score
#           find
#             filtrer les 3 meilleurs
#             prendre 3 derniers elements
            curseur = db.scores.find({},{"_id": 0, "vagues": 1, "pseudo": 1}).sort("vagues", -1)
#           convertir curseur en list
            for score in curseur:
                  liste_score.append(score)
            return liste_score


#        Affiche les score
def show_score():
    scores = get_score()
    for score in scores:
          print(f"Vague: {score['vagues']} | Pseudo: {score['pseudo']}")

#    Quitter
def quit_game():
#     sys.exit()
      sys.exit()


def main():
    menu()

    choix_utilisateur = get_choice(MENU, erreur)
    
    if choix_utilisateur == 1:
        start_game()

    if choix_utilisateur == 2:
        show_score()

    if choix_utilisateur == 3:
        quit_game()

main()