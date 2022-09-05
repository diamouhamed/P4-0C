from datetime import datetime


class PlayersApp:
    def __init__(self):
        pass

    def create_players(self):
        """Creating a player"""

        self.name = PlayersApp().ctrl_input("text", " Prénom: ")
        self.surname = PlayersApp().ctrl_input("text", " Nom de famille: ")
        self.birthday = PlayersApp().ctrl_input("date", " Date de naissance: ")
        self.genre = PlayersApp().ctrl_input("genre", " Sexe F ou M: ")
        self.rank = PlayersApp().ctrl_input("number", " Classement: ")
        return [self.name, self.surname, self.birthday, self.genre, self.rank]

    def ctrl_input(self, form, desc):
        """Selected input informations by form"""

        self.form = form

        if self.form == "text":
            self.input = str(input(desc)).upper()
            while len(self.input) == 0:
                self.input = str(input(desc)).upper()
            return self.input

        elif self.form == "genre":
            while True:
                self.input = input(desc).upper()
                if self.input == "M" or self.input == "F":
                    break
            return self.input

        elif self.form == "number":
            self.input = -1
            while self.input < 0:
                self.input = int(input(desc))

        elif self.form == "date":
            while True:
                self.input = input(desc)
                date = datetime.strptime(self.input, "%d/%m/%Y")
                date = date.date()
                break
            return self.input
        return
