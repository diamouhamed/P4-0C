from turtle import mode
from swiss_chess_tournament.models import models_players
from swiss_chess_tournament.views import views_players, views_welcome


class ControllerMenu:
    def __init__(self):
        pass

    def display_main_menu(self):
        views_welcome.ViewsWelcome().display_main_menu()

    def display_players_menu(self):
        exit_requested = False

        while not exit_requested:
            choice = self.display_main_menu()

            if choice == "1":
                print("choice 1")
