from tinydb import TinyDB, Query
import datetime

from swiss_chess_tournament.views import views_players
from swiss_chess_tournament.controllers import controllers_players


class PlayerModels:
    def __init__(self):
        pass

    def __init__(self, id=None):
        self.name = ""
        self.surname = ""
        self.birthday = ""
        self.genre = ""
        self.rank = ""
        self.id = id

        if id:
            self.data_db(id)
        else:
            self.data_input()

    def data_db(self, id):
        """Serialized informations using TinyDB"""
        query = Query()
        data = (
            TinyDB("swiss_chess_tournament/data/db.json")
            .table("players")
            .search(query.id == id)
        )
        self.name = data[0]["name"]
        self.surname = data[0]["surname"]
        self.birthday = data[0]["birthday"]
        self.genre = data[0]["genre"]
        self.rank = data[0]["rank"]

    def data_input(self):
        """Save multiple players"""
        table = TinyDB("swiss_chess_tournament/data/db.json").table("players")
        call_input = controllers_players.PlayersApp().create_players()

        self.name = call_input[0]
        self.surname = call_input[1]
        self.birthday = call_input[2]
        self.genre = call_input[3]
        self.rank = call_input[4]
        self.id = str(datetime.datetime.now())

        table.insert(
            {
                "name": self.name,
                "surname": self.surname,
                "birthday": self.birthday,
                "genre": self.genre,
                "rank": self.rank,
                "id": self.id,
            }
        )
        views_players.ViewsPlayers().players_added(self.name, self.surname)
        return self.id
