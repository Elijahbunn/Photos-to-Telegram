import argparse
import requests
import os
from pathlib import Path
import os.path
import logging
import urllib.parse
import datetime

from dotenv import load_dotenv


DIRECTORY = 'images'


def reading_extension(file_url):
    encoded_string = urllib.parse.unquote(file_url)
    url_parts = urllib.parse.urlsplit(encoded_string)
    path = url_parts.path
    (file_path, file_extension) = os.path.splitext(path)
    return file_extension


def download_file(url, params, path):
    response = requests.get(url, params=params)
    with open(path, 'wb') as file:
        file.write(response.content)


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


def fetch_spacex_launch(launch_id):
    api_url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(api_url)
    response.raise_for_status()
    launch = response.json()
    photo_urls = launch['links']['flickr']['original']
    if not photo_urls:
        logging.warning(
            'В папку ничего не скачалось, т.к. было получено 0 файлов!'
        )
    for photo_number, photo_url in enumerate(photo_urls):
        path = os.path.join(DIRECTORY, f'space_{photo_number}.jpg')
        download_file(photo_url, {}, path)


load_dotenv()
nasa_token = os.environ['NASA_TOKEN']
Path(DIRECTORY).mkdir(parents=True, exist_ok=True)
parser = argparse.ArgumentParser(
    description='Программа скачивает популярные фотографии из космоса'
    )
args = parser.parse_args()
get_day_photos(nasa_token)
get_epic_images(nasa_token)