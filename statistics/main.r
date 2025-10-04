setwd("/Users/kianshirazi/Local Files/Calculation/")
library(tidyverse)
library(dplyr)
library(ggplot2)

data <- read.csv("statistics/fuenfsprungU10_test.csv",
                 header = TRUE, sep = ",", dec = ".", stringsAsFactors = FALSE)

# Sum points per team
points_per_team <- data %>%
  group_by(team) %>%
  summarise(total_points = sum(result, na.rm = TRUE)) %>%
  arrange(desc(total_points))

# Plot
print(
ggplot(points_per_team, aes(x = reorder(team, total_points), y = total_points)) + # nolint
  geom_bar(stat = "identity", fill = "steelblue") +
  labs(title = "Total Points per Team",
       x = "Team",
       y = "Total Points") +
  theme_minimal()
)