from euroleague_api.schedule import Schedule

season = 2024
schedule = Schedule("E")

games = schedule.get_gamecodes_season(season)

print(
    games[
        (games["hometeam"].str.contains("PANATHINAIKOS", case=False, na=False)) |
        (games["awayteam"].str.contains("PANATHINAIKOS", case=False, na=False))
    ][
        ["gameCode", "hometeam", "homecode", "awayteam", "awaycode"]
    ]
)