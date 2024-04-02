k = input("Item: ").strip().lower()

d = [
    {"item": "apple", "calories": "130"},
    {"item": "avocado", "calories": "50"},
    {"item": "banana", "calories": "110"},
    {"item": "cantaloupe", "calories": "50"},
    {"item": "grapefruit", "calories": "60"},
    {"item": "grape", "calories": "90"},
    {"item": "honeydew melon", "calories": "50"},
    {"item": "kiwifruit", "calories": "90"},
    {"item": "lemon", "calories": "15"},
    {"item": "lime", "calories": "20"},
    {"item": "nectarine", "calories": "60"},
    {"item": "orange", "calories": "80"},
    {"item": "peach", "calories": "60"},
    {"item": "pear", "calories": "100"},
    {"item": "pineapple", "calories": "50"},
    {"item": "plums", "calories": "70"},
    {"item": "strawberries", "calories": "50"},
    {"item": "sweet cherries", "calories": "100"},
    {"item": "sweet tengerine", "calories": "50"},
    {"item": "watermelon", "calories": "80"},

]

for item in d:
    if k in item.values():
        print (f"Calories: {item["calories"]}")
