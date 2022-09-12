class ViewsPlayers:
    def __init__(self):
        pass

    def display_players_menu(self):
        print("\n")
        print("♘♔♙♗  MENU JOUEURS ♗♙♔♘")
        print("\n")
        print(" [1] ♗  Ajouter un joueur")
        print(" [2] ♘  Modifier un joueur")
        print(" [3] ♙  Liste des joueurs par nom")
        print(" [4] ♙  Liste des joueurs par rang")
        print("\n")
        print(" [5] ♔  Retour au menu principal")
        print("\n")

        choice_players_menu = int(input("\n Merci de faire un choix :  "))
        if choice_players_menu in ["1", "2", "3", "4", "5"]:
            return choice_players_menu

    def players_added(self, name, surname):
        print("\n", name, surname, "a bien été ajouté !")
