import telegram
from dotenv import load_dotenv
import os


load_dotenv()
BOT_TOKEN = os.environ['BOT_TOKEN']
bot = telegram.Bot(token=BOT_TOKEN)
bot.send_document(chat_id=['CHAT_ID'], document=open('images/epic_photo_0.png', 'rb'))