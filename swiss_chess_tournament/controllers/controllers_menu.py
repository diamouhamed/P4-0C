from swiss_chess_tournament.views import views_menu


class ControllerApp:
    def __init__(self):
        pass

    def main_menu(self):
        views_menu.ViewApp().display_main_menu()
