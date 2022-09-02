from pyrogram import Client
import os
from dotenv import load_dotenv
import pandas as pd


path = os.path.dirname(os.path.abspath(__file__))

dotenv_path = os.path.join(path + '/dot.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
    
API_ID = os.environ['API_ID']
API_HASH = os.environ['API_HASH']

targets = ['datajob', 'foranalysts', 'datasciencejobs']
all_messages = []

try:
    with Client("my_account", API_ID, API_HASH) as app:
        for target in targets:
            for message in app.iter_history(target, limit=20):
                all_messages.append([message.sender_chat, message.message_id, message.date, message.text, message.entities])
    
    df = pd.DataFrame(all_messages)
    df.columns = ["chat", "message_id", "date", "text", "entities"]
    df.to_csv(path + '/telegram.csv', index=False)
    print('Success: ', path + '/telegram.csv')
except Exception as e:
    print('Error: ', e)
