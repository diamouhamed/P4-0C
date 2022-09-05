from swiss_chess_tournament.views import views_players, views_tournaments


class ViewsWelcome:
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

        choice_main_menu = int(input("\n Merci de faire un choix : "))

        while choice_main_menu != 0:
            if choice_main_menu == 1:
                views_players.ViewsPlayers().display_players_menu()
            elif choice_main_menu == 2:
                views_tournaments.ViewsTournaments().display_tournaments_menu()
            elif choice_main_menu == 3:
                print("invalid choice")
            return choice_main_menu
