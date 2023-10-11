import json

import requests


class Discord():
    
    def __init__(self, token: str) -> None:
        self.__token = token

    def SendMessage(self, channels: list[int], data: dict[str, str]) -> None:
        headers = {
            "authorization": self.__token
        }
        for i in channels:
            requests.post(f'https://discord.com/api/v9/channels/{i}/messages', headers=headers, data=data)

    def ChangeNickName(self, guilds: list[int], nickname: str) -> None:
        headers = {
            "Authorization": self.__token,
            "Content-Type": "application/json"
        }
        data = {
            "nick": nickname
        }
        for i in guilds:
            requests.patch(f'https://discord.com/api/v9/guilds/{i}/members/@me', headers=headers, data=json.dumps(data))