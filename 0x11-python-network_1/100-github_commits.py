#!/usr/bin/python3
import requests
import sys

def fetch_commits(repo_name, owner_name):
    url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()[:10]  # Take the last 10 commits
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print(f"Failed to fetch commits. Status code: {response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <repository_name> <owner_name>")
    else:
        repo_name = sys.argv[1]
        owner_name = sys.argv[2]
        fetch_commits(repo_name, owner_name)
