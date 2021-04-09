class Team:

    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
        self.players = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, rating):
        self.__rating = rating

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, players):
        self.__players = players

    def add_player(self, player):
        if player in self.players:
            return f"Player {player.name} has already joined"
        self.players.append(player)
        return f"Player {player.name} joined team {self.name}"

    def remove_player(self, player_name):
        player = [p for p in self.players if p.name == player_name]
        if player:
            player = player[0]
            self.players.remove(player)
            return player
        else:
            return f'Player {player_name} not found'
