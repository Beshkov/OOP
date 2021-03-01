# from player import Player

class Guild:
    def __init__(self, name):
        self.name = name
        self.players = list()

    def assign_player(self, player):
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        elif  not player.guild == "Unaffiliated":
            return f"Player {player.name} is in another guild."
        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        if not player_name in [el.name for el in self.players]:
            return f"Player {player_name} is not in the guild."
        self.players = [el for el in self.players if not el.name == player_name]
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        result = f"Guild: {self.name}\n"
        result += "".join([player.player_info() for player in self.players])
        return result

# player = Player("George", 50, 100)
# player2 = Player("Mark", 90, 90)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
# guild = Guild("UGT")
# print(guild.assign_player(player))
# print(guild.assign_player(player2))
# print(guild.kick_player("George"))
# print(guild.kick_player("Nik"))
# print(guild.guild_info())
