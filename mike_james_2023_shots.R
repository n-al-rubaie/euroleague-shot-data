library(dplyr)
library(ggplot2)
library(readr)

# ---------- helper: arc constructor ----------
construct_arc <- function(x0, y0, r, start, stop, n = 300) {
  theta <- seq(start, stop, length.out = n)
  x <- x0 + r * cos(theta)
  y <- y0 + r * sin(theta)
  data.frame(x, y)
}

# ---------- 1. load data ----------
setwd("C:/Users/nalru/Desktop/shot data python")

df <- read_csv("mike_james_2023_shots.csv")

shots_made <- df %>%
  filter(!grepl("Missed", ACTION, ignore.case = TRUE)) %>%
  filter(COORD_X != -1 & COORD_Y != -1)

# use actual coordinate ranges from CSV
min_x <- min(shots_made$COORD_X)
max_x <- max(shots_made$COORD_X)
min_y <- min(shots_made$COORD_Y)
max_y <- max(shots_made$COORD_Y)

# ---------- 2. court geometry ----------
shift <- 70
rim_x <- 0
rim_y <- 50 - shift

# widen left/right boundary by 50
new_min_x <- min_x - 50
new_max_x <- max_x + 90

# court boundary
outer_lines <- data.frame(
  x = c(new_min_x, new_min_x, new_max_x, new_max_x, new_min_x),
  y = c(min_y - shift, max_y - shift, max_y - shift, min_y - shift, min_y - shift)
)

# paint
paint <- data.frame(
  x = c(-300, -300, 300, 300, -300),
  y = c(min_y - shift,
        rim_y + 400,
        rim_y + 400,
        min_y - shift,
        min_y - shift)
)

# free-throw circle
ft_circle <- construct_arc(
  x0 = rim_x,
  y0 = rim_y + 425,
  r = 180,
  start = 0,
  stop = pi
)

# restricted area
restricted_area <- construct_arc(
  x0 = rim_x,
  y0 = rim_y,
  r = 125,
  start = 0,
  stop = pi
)

# backboard
backboard <- data.frame(
  x = c(rim_x - 90, rim_x + 90),
  y = c(rim_y + 20, rim_y + 20)
)

# 3-point arc (ONLY curved arc — NO corner lines)
arc3 <- data.frame(
  x = rim_x + 675 * sin(seq(-pi/2, pi/2, length.out = 300)),
  y = rim_y + 675 * cos(seq(-pi/2, pi/2, length.out = 300))
)

arc3_full <- arc3   # ← EXACT SAME AS NUNN VERSION

# ---------- 3. plot ----------
shot_chart <- ggplot() +
  geom_path(data = outer_lines, aes(x, y)) +
  geom_path(data = paint, aes(x, y)) +
  geom_path(data = ft_circle, aes(x, y)) +
  geom_path(data = restricted_area, aes(x, y)) +
  geom_path(data = backboard, aes(x, y)) +
  geom_path(data = arc3_full, aes(x, y)) +
  geom_point(data = shots_made,
             aes(x = COORD_X, y = COORD_Y),
             colour = "blue", alpha = 0.8, size = 3) +
  coord_fixed() +
  theme_minimal() +
  theme(panel.grid = element_blank()) +
  labs(
    title = "Mike James — Made Shot Locations (EuroLeague 2023)",
    subtitle = "Court shifted up 30 & widened by 50 (no corner lines)"
  )

print(shot_chart)
