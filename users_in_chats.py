import requests

# Замените на ваши реальные данные
auth_token = "AUTH_TOKEN"
user_id = "USER_ID"
rocket_chat_url = "https://rocket.chat"

# Получите список всех чатов (комнат)
def get_all_chats():
    headers = {
        "X-Auth-Token": auth_token,
        "X-User-Id": user_id
    }

    response = requests.get(f"{rocket_chat_url}/api/v1/channels.list", headers=headers)

    if response.status_code == 200:
        return response.json().get("channels", [])
    else:
        print(f"Ошибка при получении списка чатов: {response.status_code}")
        return []

# Получите список пользователей в каждом чате
def get_users_in_chat(chat_id):
    headers = {
        "X-Auth-Token": auth_token,
        "X-User-Id": user_id
    }

    params = {
        "roomId": chat_id
    }

    response = requests.get(f"{rocket_chat_url}/api/v1/channels.members", headers=headers, params=params)

    if response.status_code == 200:
        return response.json().get("members", [])
    else:
        print(f"Ошибка при получении списка пользователей в чате {chat_id}: {response.status_code}")
        return []

# Получите список всех чатов
all_chats = get_all_chats()

# Для каждого чата, получите список пользователей
for chat in all_chats:
    chat_id = chat["_id"]
    users_in_chat = get_users_in_chat(chat_id)
    print(f"Чат: {chat['name']}, Пользователи: {', '.join([user['username'] for user in users_in_chat])}")
