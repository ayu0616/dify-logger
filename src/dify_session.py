from time import sleep

from requests import Session


class DifySession(Session):
    def __init__(self, app_id: str, api_key: str):
        super().__init__()
        self.headers.update({"Authorization": "Bearer " + api_key})
        self.app_id = app_id

    def get_chat_conversations(self):
        has_more = True
        page = 1
        result = []
        while has_more:
            url = f"https://cloud.dify.ai/console/api/apps/{self.app_id}/chat-conversations?page={page}&limit=100"
            res = self.get(url)
            result.extend(res.json()["data"])
            has_more = res.json()["has_more"]
            page += 1
            if has_more:
                sleep(1)
        return result

    def get_chat_messages(self, conversation_id: str):
        url = f"https://cloud.dify.ai/console/api/apps/{self.app_id}/chat-messages?conversation_id={conversation_id}&limit=100"  # TODO: 100件を超えた場合の処理
        res = self.get(url)
        return res.json()["data"]
