from euroleague_api.schedule import Schedule
from euroleague_api.shot_data import ShotData
import pandas as pd
import time

# ==============================
# SETTINGS
# ==============================

season = 2023
competition_code = "E"
player_name = "JAMES, MIKE"

# ==============================
# GET SEASON SCHEDULE
# ==============================

schedule = Schedule(competition_code)

games = schedule.get_gamecodes_season(season)

# ==============================
# GET ONLY MONACO GAMES
# ==============================

monaco_games = games[
    (games["homecode"] == "MCO") |
    (games["awaycode"] == "MCO")
]

print(f"Monaco games found: {len(monaco_games)}")

# ==============================
# DOWNLOAD SHOT DATA
# ==============================

shotdata = ShotData(competition_code)

all_mike_shots = []

for _, game in monaco_games.iterrows():

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

            # Find Mike James
            mike = df[
                df["PLAYER"].str.contains(
                    player_name,
                    case=False,
                    na=False
                )
            ].copy()

            if not mike.empty:

                # Add game information
                mike["gameCode"] = game_code
                mike["date"] = game["date"]
                mike["home_team"] = game["hometeam"]
                mike["away_team"] = game["awayteam"]

                all_mike_shots.append(mike)

                print(
                    f"✓ Mike James: "
                    f"{len(mike)} shots"
                )

            else:

                print("  Mike James not found")

        else:

            print("  No shot data")

        # Wait between requests
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

if all_mike_shots:

    mike_james_shots = pd.concat(
        all_mike_shots,
        ignore_index=True
    )

    # Save CSV
    filename = "mike_james_2023_shots.csv"

    mike_james_shots.to_csv(
        filename,
        index=False
    )

    print("\n")
    print("==============================")
    print("FINISHED")
    print("==============================")
    print(
        f"Total Mike James shots: "
        f"{len(mike_james_shots)}"
    )
    print(
        f"Games with Mike James shots: "
        f"{len(all_mike_shots)}"
    )
    print(
        f"CSV saved as: {filename}"
    )
    print("==============================")

else:

    print("\n❌ No Mike James shot data found.")