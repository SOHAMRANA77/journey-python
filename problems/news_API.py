import requests
import json
Query = input("what type of news are you interested in  :")
url = f"https://newsapi.org/v2/everything?q={Query}&from=2023-08-26&sortBy=publishedAt&apiKey=ff17bf7997c84dcaa361c8040b18d365"
r = requests.get(url)
news = json.loads(r.text)
# print(news, type(news))
for article in news["articles"]:
    print(f'\ntitle :{article["title"]}')
    print(article["description"])
    print("---------------------------------------------------------------------------")
