from datetime import datetime


class ControllersPlayers:
    def __init__(self):
        pass

    def create_players(self):
        """Creating a player"""

        self.name = self.ctrl_input("text", " Prénom: ")
        self.surname = self.ctrl_input("text", " Nom de famille: ")
        self.birthday = self.ctrl_input("date", " Date de naissance: ")
        self.genre = self.ctrl_input("genre", " Sexe F ou M: ")
        self.rank = self.ctrl_input("number", " Classement: ")

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
                dt_convert = datetime.strptime(self.input, "%d/%m/%Y")
                dt_convert = dt_convert.date()
                break
            return self.input
        return
