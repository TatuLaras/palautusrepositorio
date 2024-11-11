import requests

from player import Player


class PlayerReader:
    def __init__(self, url) -> None:
        response = requests.get(url).json()
        self.players = []

        for player_dict in response:
            player = Player(player_dict)
            self.players.append(player)