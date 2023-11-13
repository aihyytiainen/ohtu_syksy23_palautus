from player_reader import PlayerReader

class PlayerStats:
    def __init__(self, reader:PlayerReader):
        self.players = reader.players

    def top_scorers_by_nationality(self, nationality:str):
        player_list = []
        for player in self.players:
            if player.nationality == nationality:
                player_list.append(player)
        player_list.sort(key=lambda x: x.points, reverse=True)
        return player_list
