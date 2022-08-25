from swiss_chess_tournament.views import views_menu
from swiss_chess_tournament.controllers import controllers_tools

class ControllerApp:
    """Controller App"""
    
    def controllers_main_menu(self):
        views_menu.ViewApp().display_main_menu()
        self.menu_number = controllers_tools.ControllerTools().menu_selection(3)

        #Menu Joueur
        if self.menu_number == 1:
            ControllerApp().players_menu()
            
        #Menu Tournois
        if self.menu_number == 1:
            ControllerApp().players_tournaments()
            
        #Fermer le programme
        elif self.menu_number == 3:
            pass
            
    def players_menu(self):
        views_menu.ViewApp().display_players_menu()
        self.menu_number = controllers_tools.ControllerTools().menu_selection(4)
        
        #Retour au menu principale
        if self.menu_number == 4:
            ControllerApp().controllers_main_menu()
        
    def players_tournaments(self):
        views_menu.ViewApp().display_tournaments_menu()
        self.menu_number = controllers_tools.ControllerTools().menu_selection(4)
        
        #Retour au menu principale
        if self.menu_number == 4:
            ControllerApp().controllers_main_menu()