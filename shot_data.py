from euroleague_api.shot_data import ShotData
import pandas as pd
import time

season = 2023
competition_code = "E"

shotdata = ShotData(competition_code)

all_mike_shots = []

for game_code in range(1, 50):

    try:
        print(f"Checking game {game_code}...")

        df = shotdata.get_game_shot_data(season, game_code)

        if not df.empty:

            # Filter for Mike James
            mike = df[
                df["PLAYER"].str.contains(
                    "JAMES, MIKE",
                    case=False,
                    na=False
                )
            ]

            if not mike.empty:
                all_mike_shots.append(mike)
                print(f"✓ Mike James found: {len(mike)} shots")

        # Avoid API rate limiting
        time.sleep(2)

    except Exception as e:
        print(f"Game {game_code}: {e}")

        if "429" in str(e):
            print("Rate limited. Waiting 30 seconds...")
            time.sleep(30)


# Combine Mike James' shots
if all_mike_shots:

    mike_james_shots = pd.concat(
        all_mike_shots,
        ignore_index=True
    )

    mike_james_shots.to_csv(
        "mike_james_2023_shots.csv",
        index=False
    )

    print("\n==============================")
    print("FINISHED")
    print("==============================")
    print(f"Total Mike James shots: {len(mike_james_shots)}")
    print("Saved as: mike_james_2023_shots.csv")

else:
    print("No Mike James shots found.")