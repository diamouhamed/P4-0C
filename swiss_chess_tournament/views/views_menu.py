class ViewApp:
    def __init__(self):
        pass

    def display_main_menu(self):
        print("\n")
        print("♘  Bienvienue dans SWISS CHESS TOURNAMENT ♘")
        print("\n")
        print("♘♔♙♗  MENU PRINCIPAL ♗♙♔♘")
        print("\n")
        print(" [1] ♔  Menu joueurs")
        print(" [2] ♕  Menu tournois")
        print("\n")
        print(" [3] ♖  Quitter l'application")
        print("\n")

        choice_main_menu = int(input("\n Veuillez faire un choix : "))

        while choice_main_menu != 0:
            if choice_main_menu == 1:
                self.display_players_menu()
            elif choice_main_menu == 2:
                self.display_tournaments_menu()
            elif choice_main_menu == 3:
                print("invalid choice")
            return choice_main_menu

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

    def display_tournaments_menu(self):
        print("\n")
        print("♘♔♙♗  MENU TOURNOIS ♗♙♔♘")
        print("\n")
        print(" [1] ♗  Nouveau tournoi")
        print(" [2] ♘  Charger un tournoi")
        print(" [3] ♙  Liste des tournois")
        print("\n")
        print(" [4] ♔  Retour au menu principal")
        print("\n")
