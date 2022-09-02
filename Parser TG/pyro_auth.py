from pyrogram import Client
import os
from dotenv import load_dotenv



path = os.path.dirname(os.path.abspath(__file__))

dotenv_path = os.path.join(path + '/dot.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
    
API_ID = os.environ['API_ID']
API_HASH = os.environ['API_HASH']
with Client("my_account", API_ID, API_HASH) as app: 
    app.send_message("me", "Авторизация прошла успешно")