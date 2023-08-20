import argparse
from pathlib import Path
import datetime
import os

import requests
from dotenv import load_dotenv

from supporting_file import DIRECTORY, download_file


def get_epic_images(nasa_token):
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {
        'api_key': nasa_token
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    images = response.json()
    for photo_number, image in enumerate(images):
        url = 'https://api.nasa.gov/EPIC/archive/natural'
        date = datetime.datetime.fromisoformat(image['date'])
        date = date.strftime("%Y/%m/%d")
        image_name = image['image']
        path = os.path.join(DIRECTORY, f'epic_photo_{photo_number}.png')
        download_file(
            f'{url}/{date}/png/{image_name}.png',
            params, path
            )


if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.environ['NASA_TOKEN']
    Path(DIRECTORY).mkdir(parents=True, exist_ok=True)
    get_epic_images(nasa_token)
