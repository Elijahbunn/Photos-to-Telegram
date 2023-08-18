import argparse
from pathlib import Path
import os
from dotenv import load_dotenv

import requests

from supporting_file import DIRECTORY, reading_extension, download_file


def get_day_photos(nasa_token):
    api_url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': nasa_token,
        'count': 30
             }
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    launches = response.json()
    for photo_number, photo in enumerate(launches):
        if photo['media_type'] == 'image':
            extension = reading_extension(photo['url'])
            path = os.path.join(
                DIRECTORY,
                f'nasa_apod_{photo_number}{extension}'
                )
            download_file(photo['url'], params, path)


if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.environ['NASA_TOKEN']
    Path(DIRECTORY).mkdir(parents=True, exist_ok=True)
    parser = argparse.ArgumentParser(
        description='Программа скачивает популярные фотографии из космоса'
        )
    args = parser.parse_args()
    get_day_photos(nasa_token)