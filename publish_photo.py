import telegram
from dotenv import load_dotenv
import os
import random
import argparse

from supporting_file import DIRECTORY, collecting_files, send_file


def send_photo(photo):
    if not photo:
        files = collecting_files(DIRECTORY)
        photo = random.choice(files)
    send_file(os.path.join(DIRECTORY, photo), bot, tg_chat_id)


if __name__ == '__main__':
    load_dotenv()
    tg_token = os.environ['TG_TOKEN']
    tg_chat_id = os.environ['CHAT_ID']
    bot = telegram.Bot(token=tg_token)
    parser = argparse.ArgumentParser(
        description='Программа отправляет фотографию из папки images'
        )
    parser.add_argument('-p', '--photo', help='Фото, которое нужно отправить',
                        default='')
    args = parser.parse_args()
    send_photo(args.photo)