import re

url = input("URL: ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
#username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
    print(f"useranme {matches.group(1)}")
