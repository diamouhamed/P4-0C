class ControllerTools:

    #Selection du menu principale 
    def menu_selection(self, menu_len):
        self.menu_len = menu_len
        self.menu_number = 0
        while self.menu_number < 1:
            self.menu_number = int(input("Quel est votre choix ? "))
        return self.menu_number