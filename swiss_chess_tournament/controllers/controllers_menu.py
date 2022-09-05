from swiss_chess_tournament.views import views_players, views_welcome


class MenuApp:
    def __init__(self):
        pass

    def display_main_menu(self):
        views_welcome.ViewsWelcome().display_main_menu()

    def display_players_menu(self):
        views_players.ViewsPlayers().display_players_menu()
