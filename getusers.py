import requests
import json

base_url = "https://your-rocket-chat-server/api/v1/users.list"
auth_token = "YOUR_AUTH_TOKEN"
user_id = "YOUR_USER_ID"

count = 100  # Adjust this according to your needs
offset = 0

all_users = []

while True:
    params = {
        "count": count,
        "offset": offset,
    }

    headers = {
        "X-Auth-Token": auth_token,
        "X-User-Id": user_id,
    }

    response = requests.get(base_url, params=params, headers=headers)

    if response.status_code == 200:
        users = response.json().get("users", [])
        if not users:
            break
        all_users.extend(users)
        offset += count
    else:
        print("Error:", response.status_code)
        break

# Now, 'all_users' contains a list of all users retrieved from the Rocket.Chat server.

with open("rocket_chat_users.json", "w") as json_file:
    json.dump(all_users, json_file)

print(f"Total {len(all_users)} users saved to 'rocket_chat_users.json' file.")
