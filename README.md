# EuroLeague Basketball Shot Data

A basketball data analysis project using the **EuroLeague API**, Python and R to collect, process and visualise player shot data.

The project currently focuses on **Mike James** and **Kendrick Nunn**, collecting their EuroLeague shot locations and creating shot charts from the data.

## Project Overview

This project demonstrates a data analysis workflow using basketball data:

1. Retrieve EuroLeague game schedules and game codes.
2. Retrieve shot data for individual games using the EuroLeague API.
3. Filter the data for specific players.
4. Combine shot data across multiple games.
5. Save the data as CSV files.
6. Analyse and visualise shot locations using R and `ggplot2`.

## Players

### Mike James

The Python script searches games from the **2023 EuroLeague season** and identifies shots taken by Mike James.

The resulting data is saved as:

```text
mike_james_2023_shots.csv
```

### Kendrick Nunn

The Python script retrieves the **2024 EuroLeague schedule** and identifies games involving Panathinaikos.

It then retrieves the shot data from those games and filters the data for Kendrick Nunn.

Additional game information is added to the dataset, including:

* Game code
* Date
* Home team
* Away team

The resulting data is saved as:

```text
kendrick_nunn_2024_shots.csv
```

## Shot Visualisation

The Kendrick Nunn dataset is visualised using R.

The R script:

* Loads the shot data from CSV
* Filters for made shots
* Removes invalid shot coordinates
* Constructs a basketball court using coordinate geometry
* Plots the locations of Kendrick Nunn's made shots

The visualisation uses `ggplot2` to create a court-based shot chart.

## Technologies

### Python

* Python
* Pandas
* `euroleague_api`
* Time

Python is used to retrieve and process the EuroLeague data.

### R

* R
* `dplyr`
* `ggplot2`
* `readr`

R is used to process the shot data and create the shot visualisation.

## Data Collection

The project uses the `euroleague_api` Python package to retrieve EuroLeague schedules and shot data.

The EuroLeague competition code used is:

```text
E
```

The scripts include delays between API requests to reduce the risk of rate limiting.

If the API returns a `429` response, the scripts wait before continuing.

## Project Structure

```text
basketball-shots-data/
│
├── mike_james_2023.py
├── kendrick_nunn_2024.py
├── kendrick_nunn_shot_chart.R
│
├── mike_james_2023_shots.csv
└── kendrick_nunn_2024_shots.csv
```

*File names may vary depending on how the scripts are organised in the repository.*

## Example Analysis

The R analysis produces a basketball shot chart showing the locations of Kendrick Nunn's made shots during the 2024 EuroLeague season.

The court is constructed using coordinate geometry, including:

* Court boundaries
* Paint
* Free-throw circle
* Restricted area
* Backboard
* Three-point arc

## Purpose

The purpose of this project is to explore basketball shot-location data and demonstrate a practical data-analysis workflow.

It combines:

**API data collection → data cleaning → data processing → CSV datasets → data visualisation**

The project also provides a foundation for further analysis of player shooting patterns, shot selection and shooting locations in the EuroLeague.

## Final results
## Mike James Shotmap
<img width="1517" height="918" alt="shotmap_mike_james" src="https://github.com/user-attachments/assets/56eda8fb-1349-481b-946a-ebf83a74055e" />

## Kendrick Nunn Shotmap
<img width="1528" height="947" alt="shotmap_kendrick_nunn" src="https://github.com/user-attachments/assets/a97b2d1a-61da-4e1e-8059-6d79e40b21a4" />

