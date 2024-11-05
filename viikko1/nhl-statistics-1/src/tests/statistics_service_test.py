import unittest
from statistics_service import SortBy, StatisticsService
from player_reader import Player

players = [
    Player("Semenko", "EDM", 4, 12),
    Player("Lemieux", "PIT", 45, 54),
    Player("Kurri", "EDM", 37, 53),
    Player("Yzerman", "DET", 42, 56),
    Player("Gretzky", "EDM", 35, 89),
]


class PlayerReaderStub:
    def get_players(self):
        return players


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        player_reader_stub = PlayerReaderStub()
        self.statistics_service = StatisticsService(player_reader_stub)

    def test_constructor(self):
        self.assertEqual(len(self.statistics_service._players), 5)

    def test_search(self):
        self.assertEqual(self.statistics_service.search("Lemieux").team, "PIT")

    def test_team(self):
        team_players = self.statistics_service.team("EDM")
        self.assertTrue(players[0] in team_players)
        self.assertTrue(players[2] in team_players)
        self.assertTrue(players[4] in team_players)

    def test_top_invalid_sort_by(self):
        top_players = self.statistics_service.top(3, 10)
        self.assertEqual(top_players[0], players[4])
        self.assertEqual(top_players[1], players[1])
        self.assertEqual(top_players[2], players[3])

    def test_top_points(self):
        top_players = self.statistics_service.top(3, SortBy.POINTS)
        self.assertEqual(top_players[0], players[4])
        self.assertEqual(top_players[1], players[1])
        self.assertEqual(top_players[2], players[3])

    def test_top_assists(self):
        top_players = self.statistics_service.top(3, SortBy.ASSISTS)
        self.assertEqual(top_players[0], players[4])
        self.assertEqual(top_players[1], players[3])
        self.assertEqual(top_players[2], players[1])

    def test_top_goals(self):
        top_players = self.statistics_service.top(3, SortBy.GOALS)
        self.assertEqual(top_players[0], players[1])
        self.assertEqual(top_players[1], players[3])
        self.assertEqual(top_players[2], players[2])

    def test_search_nonexistent(self):
        self.assertIsNone(self.statistics_service.search("Nonexistent"))
