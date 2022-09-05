from swiss_chess_tournament.models import models_players


class ViewsPlayers:
    def __init__(self):
        pass

    def display_players_menu(self):
        print("\n")
        print("♘♔♙♗  MENU JOUEURS ♗♙♔♘")
        print("\n")
        print(" [1] ♗  Ajouter un joueur")
        print(" [2] ♘  Modifier un joueur")
        print(" [3] ♙  Liste des joueurs")
        print("\n")
        print(" [4] ♔  Retour au menu principal")
        print("\n")

        choice_players_menu = int(input("\n Merci de faire un choix :  "))

        while choice_players_menu != 0:
            if choice_players_menu == 1:
                models_players.PlayerModels()

    def players_added(self, name, surname):
        print("\n", name, surname, "a bien été ajouté !")
