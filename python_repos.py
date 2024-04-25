import requests

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
    print(key)

for repo_dict in repo_dicts:
    print(f"Name: {repo_dict["name"]}")
    print(f"Repo: {repo_dict["html_url"]}")

print(repo_dict["name"])