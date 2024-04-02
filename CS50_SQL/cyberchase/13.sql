SELECT "title", "topic", "season", "episode_in_season"
FROM "episodes"
WHERE "topic" LIKE "%division%"
OR "topic" LIKE "%multiplication%"
OR "topic" LIKE "%numbers%"
ORDER BY "title";
