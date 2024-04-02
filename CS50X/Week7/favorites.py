from cs50 import SQL

db = SQL("sqlite:///favorites.db")

favorite = input("Favorite: ")

rows = db.execute("SELECT problem, language FROM favorites WHERE language = ?", favorite)

for row in rows:
    print (row["problem"], row["language"])
