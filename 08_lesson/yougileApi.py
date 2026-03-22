import requests


class YougileApi:
    def __init__(self, base_url, token=None):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def create_project(self, title):
        return requests.post(
            f"{self.base_url}/projects",
            json={"title": title}, headers=self.headers)

    def get_project(self, project_id):
        return requests.get(
            f"{self.base_url}/projects/{project_id}",
            headers=self.headers)

    def update_project(self, project_id, new_title):
        return requests.put(
            f"{self.base_url}/projects/{project_id}",
            json={"title": new_title}, headers=self.headers)
