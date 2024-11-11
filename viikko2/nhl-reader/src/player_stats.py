from player_reader import PlayerReader


class PlayerStats:
    def __init__(self, reader: PlayerReader) -> None:
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players_of_nationality = filter(
            lambda x: x.nationality == nationality, self.reader.players
        )
        return sorted(players_of_nationality, key=lambda x: x.score, reverse=True)
