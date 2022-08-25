from swiss_chess_tournament.views import views_menu
from swiss_chess_tournament.controllers import controllers_tools

class ControllerApp:
    """Controller App"""
    
    def controllers_main_menu(self):
        views_menu.ViewApp().display_main_menu()
        self.menu_number = controllers_tools.ControllerTools().menu_selection(3)
    