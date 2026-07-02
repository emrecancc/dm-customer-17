import json
import requests

class UserService:
    def get_user(self, user_id):
        response = requests.get(f"https://api.example.com/users/{user_id}")
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            return None
