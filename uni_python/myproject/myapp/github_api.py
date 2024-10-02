import requests
from datetime import datetime

def get_github_data(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        data['created_at'] = datetime.strptime(data['created_at'], '%Y-%m-%dT%H:%M:%SZ')
        data['updated_at'] = datetime.strptime(data['updated_at'], '%Y-%m-%dT%H:%M:%SZ')
        return data
    else:
        return None
