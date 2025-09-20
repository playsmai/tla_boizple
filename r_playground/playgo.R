# playgo.R --------------------------------------------
# Demo script for "PlayGo"
# This simulates a game round and prints results.

set.seed(42)

# Demo players
players <- data.frame(
  name = c("alice", "bob", "carol"),
  score = c(0, 0, 0),
  stringsAsFactors = FALSE
)

# Simulate one round
players$gain <- sample(1:6, nrow(players), replace = TRUE)
players$score <- players$score + players$gain

# Summarise
summary_tbl <- aggregate(score ~ name, data = players, FUN = mean)

# Report
top_player <- players$name[which.max(players$score)]
message <- if (max(players$score) > 10) "big" else "small"

cat("Round results:\n")
print(players)
cat("\nSummary (average score):\n")
print(summary_tbl)
cat("\nTop player:", top_player, "\n")
cat("Message:", message, "\n")
