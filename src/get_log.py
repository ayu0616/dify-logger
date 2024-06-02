"""
ログテーブルのデータをCSVに出力する
"""

import os

import dotenv
import pandas as pd

from dify_session import DifySession

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    dotenv.load_dotenv()

    DIFY_APP_ID = os.getenv("DIFY_APP_ID")
    DIFY_API_KEY = os.getenv("DIFY_API_KEY")

    if not DIFY_APP_ID:
        raise ValueError("DIFY_APP_ID is not set")
    if not DIFY_API_KEY:
        raise ValueError("DIFY_API_KEY is not set")

    session = DifySession(DIFY_APP_ID, DIFY_API_KEY)

    chat_conversations = session.get_chat_conversations()

    df = pd.DataFrame(chat_conversations)
    df.to_csv("../log/chat_conversations.csv", index=False)

    conv_id_list = df["id"].tolist()
    for id in conv_id_list:
        chat_messages = session.get_chat_messages(id)
        df = pd.DataFrame(chat_messages)
        df.to_csv(f"../log/chat-messages/{id}.csv", index=False)
