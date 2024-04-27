import requests
import plotly.express as px

url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars"
headers = {"Accept": "application/vnd.github.v3+json"}

r = requests.get(url, headers = headers)
print(f"Status code: {r.status_code}")

response_dict = r.json()

print(response_dict.keys())

print(f"Total reps: {response_dict["total_count"]}")
print(f"Complete results: {not response_dict["incomplete_results"]}")

repo_dicts = response_dict["items"]
print(f"Reps returned: {len(repo_dicts)}")

repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")

for key in sorted(repo_dict.keys()):

    stargazers = []
    names = []
    print(key)

for repo_dict in repo_dicts:
    print(f"Name: {repo_dict["name"]}")
    names.append(repo_dict["name"])
    print(f"Repo: {repo_dict["html_url"]}")
    print(f"Stars: {repo_dict["stargazers_count"]}\n")
    stargazers.append(repo_dict["stargazers_count"])

labels = {"x":"Repository", "y":"Star count"}

fig = px.bar(x = names, y = stargazers, title = "GitHub stars", labels=labels)

fig.show()