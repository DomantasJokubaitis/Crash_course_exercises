import plotly.express as px
from operator import itemgetter
import requests

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:6]:
    url = url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    response_dict = r.json()

    try:
        submission_dict = {
            "title" : response_dict["title"],
            "hn_link" : f"https://news.ycombinator.com/item?id={submission_id}",
            "comments" : response_dict["descendants"]
        }
    except KeyError:
        continue

    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter("comments"), reverse=True)

titles, comments = [], []

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict["title"]}")
    titles.append(submission_dict["title"])
    print(f"Discussion link: {submission_dict["hn_link"]}")
    print(f"Comments: {submission_dict["comments"]}")
    comments.append(submission_dict["comments"])


labels = {"x": "Title", "y": "Comments"}
title = "Hacker news popular posts"
fig = px.bar(x = titles, y = comments, labels = labels, title = title)

fig.show()