import os
from dotenv import load_dotenv
from pprint import pprint
from time import sleep

import requests
from tqdm import tqdm

from yandex_disk import YaDiskUploader
from vk_api import VkApiHandler


if __name__ == '__main__':
    load_dotenv()
    ya_disk_token = os.getenv('YA_DISK_TOKEN')
    ya = YaDiskUploader(ya_disk_token)

    vk_api_token = os.getenv('VK_API_TOKEN')
    vk_api_version = os.getenv('VK_API_VERSION')
    vk = VkApiHandler(vk_api_token, vk_api_version)

    # owner_id = 1
    owner_id = None

    albums = vk.get_all_albums(owner_id)
    pbar_alb = tqdm(albums, desc='Общий прогресс', unit='album')
    for index, alb in enumerate(albums):
        sleep(0.34)
        photos = vk.get_photos(owner_id, alb)

        if photos is None or len(photos) == 0:
            pbar_alb.update(1)
            continue

        total_pbar_incr = round(1 / len(photos), 2) if photos is not None else 0
        for photo in tqdm(photos, desc=albums[alb], unit='photo'):
            img_data = requests.get(photo['photo']['url']).content
            ya.upload_photo_to_disk('backup', f'{photo["id"]}.jpg', img_data)
            pbar_alb.update(total_pbar_incr)

        pbar_alb.n = index + 1
        pbar_alb.refresh()




