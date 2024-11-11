from player_reader import PlayerReader
from player_stats import PlayerStats
from rich.console import Console
from rich.table import Table
from rich import print


def main():
    console = Console()

    allowed_seasons = [
        "2018-19",
        "2019-20",
        "2020-21",
        "2021-22",
        "2022-23",
        "2023-24",
        "2024-25",
    ]

    allowed_nationalities = [
        "AUT",
        "CZE",
        "AUS",
        "SWE",
        "GER",
        "DEN",
        "SUI",
        "SVK",
        "NOR",
        "RUS",
        "CAN",
        "LAT",
        "BLR",
        "SLO",
        "USA",
        "FIN",
        "GBR",
    ]

    print("NHL statistics by nationality")

    season = None

    while season is None or season not in allowed_seasons:
        console.print("\nSelect season ", end="")
        console.print(f"[{"/".join(allowed_seasons)}]", style="blue", end="")
        season = input(": ")

    while True:
        nationality = None

        while nationality is None or nationality not in allowed_nationalities:
            console.print(f"\nSelect nationality ", end="")
            console.print(f"[{"/".join(allowed_nationalities)}]", style="blue", end="")

            nationality = input(": ")

        url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
        reader = PlayerReader(url)
        stats = PlayerStats(reader)
        players = stats.top_scorers_by_nationality(nationality)

        table = Table(show_header=True, header_style="bold blue")
        table.add_column("name", style="magenta")
        table.add_column("team", style="blue")
        table.add_column("goals", style="green")
        table.add_column("assists", style="green")
        table.add_column("points", style="green")

        for player in players:
            table.add_row(
                player.name,
                player.team,
                str(player.goals),
                str(player.assists),
                str(player.score),
            )

        console.print(table)


main()
