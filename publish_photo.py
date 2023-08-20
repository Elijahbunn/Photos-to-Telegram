import telegram
from dotenv import load_dotenv
import os
import random
import argparse

from supporting_file import DIRECTORY, send_file


if __name__ == '__main__':
    load_dotenv()
    tg_token = os.environ['TG_TOKEN']
    tg_chat_id = os.environ['CHAT_ID']
    bot = telegram.Bot(token=tg_token)
    files = os.listdir(DIRECTORY)
    parser = argparse.ArgumentParser(
        description='Программа отправляет фотографию из папки images'
        )
    parser.add_argument('-p', '--photo', help='Фото, которое нужно отправить',
                        default=random.choice(files))
    args = parser.parse_args()
    send_file(os.path.join(DIRECTORY, args.photo), bot, tg_chat_id)