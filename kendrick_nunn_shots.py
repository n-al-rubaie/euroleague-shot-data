from euroleague_api.schedule import Schedule
from euroleague_api.shot_data import ShotData
import pandas as pd
import time

# ==============================
# SETTINGS
# ==============================

season = 2024
competition_code = "E"

player_name = "NUNN, KENDRICK"
team_code = "PAN"

# ==============================
# GET SEASON SCHEDULE
# ==============================

schedule = Schedule(competition_code)

games = schedule.get_gamecodes_season(season)

# ==============================
# GET PANATHINAIKOS GAMES
# ==============================

team_games = games[
    (games["homecode"] == team_code) |
    (games["awaycode"] == team_code)
].copy()

print(f"Panathinaikos games found: {len(team_games)}")

# ==============================
# GET SHOT DATA
# ==============================

shotdata = ShotData(competition_code)

all_player_shots = []

for _, game in team_games.iterrows():

    game_code = game["gameCode"]

    print(
        f"\nChecking game {game_code}: "
        f"{game['hometeam']} vs {game['awayteam']}"
    )

    try:

        df = shotdata.get_game_shot_data(
            season,
            game_code
        )

        if not df.empty:

            player = df[
                df["PLAYER"].str.contains(
                    player_name,
                    case=False,
                    na=False
                )
            ].copy()

            if not player.empty:

                # Add game information
                player["gameCode"] = game_code
                player["date"] = game["date"]
                player["home_team"] = game["hometeam"]
                player["away_team"] = game["awayteam"]

                all_player_shots.append(player)

                print(
                    f"✓ Nunn: {len(player)} shots"
                )

            else:

                print("  Nunn not found")

        else:

            print("  No shot data")

        # Wait to avoid API rate limiting
        time.sleep(2)

    except Exception as e:

        print(f"✗ Error: {e}")

        if "429" in str(e):

            print(
                "Rate limited — waiting 60 seconds..."
            )

            time.sleep(60)

# ==============================
# COMBINE ALL SHOTS
# ==============================

if all_player_shots:

    nunn_shots = pd.concat(
        all_player_shots,
        ignore_index=True
    )

    filename = "kendrick_nunn_2024_shots.csv"

    nunn_shots.to_csv(
        filename,
        index=False
    )

    print("\n==============================")
    print("FINISHED")
    print("==============================")
    print(
        f"Total Kendrick Nunn shots: "
        f"{len(nunn_shots)}"
    )
    print(
        f"Games with shot data: "
        f"{len(all_player_shots)}"
    )
    print(
        f"CSV saved as: {filename}"
    )
    print("==============================")

else:

    print("\n❌ No Kendrick Nunn shot data found.")