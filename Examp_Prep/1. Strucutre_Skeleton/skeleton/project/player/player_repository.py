from project.player.player import Player


class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players = []

    def add(self, player: Player):
        if player in self.players:
            raise ValueError(f"Player {player.username} already exists!")

        self.players.append(player)
        self.count += 1

    def remove(self, player: str):
        if not player:
            raise ValueError("Player cannot be an empty string!")

        player_to_remove = self.find(player)

        self.players.remove(player_to_remove)
        self.count -= 1

    def find(self, username: str):
        return [player for player in self.players if player.username == username][0]

