import os
from dotenv import load_dotenv
from pprint import pprint
from time import sleep
import json
from datetime import datetime

import requests
from tqdm import tqdm

from yandex_disk import YaDiskUploader
from vk_api import VkApiHandler


def backup_vk(vk_token, vk_user_id, ya_disk_token, vk_api_version='5.131'):
    ya = YaDiskUploader(ya_disk_token)
    vk = VkApiHandler(vk_token, vk_api_version)
    json_result = ''
    return json_result


if __name__ == '__main__':
    default_folder = 'backup/' + datetime.now().strftime("%Y-%m-%d %H:%M:%S").replace(' ', '_')
    load_dotenv()
    ya_disk_token = os.getenv('YA_DISK_TOKEN')
    ya = YaDiskUploader(ya_disk_token)

    # vk_api_token = os.getenv('VK_API_TOKEN')
    # vk_api_version = os.getenv('VK_API_VERSION') | '5.131'
    # vk = VkApiHandler(vk_api_token, vk_api_version)

    path_on_dir = 'backup/dir/help'

    ya.force_create_folder(path_on_dir)


    #
    # resp = ya.create_folder('backup/dir/help')
    # pprint(resp.json())
    #
    # is_exists, resp = ya.is_folder_exists('backup/dir/help')
    # print(is_exists)
    # pprint(resp.json(), indent=2)





    # owner_id = 1
    # owner_id = None
    #
    # albums = vk.get_all_albums(owner_id)
    # pbar_alb = tqdm(albums, desc='Общий прогресс', unit='album')
    # photos_info = list()
    # for index, alb in enumerate(albums):
    #     sleep(0.34)
    #     photos = vk.get_photos(owner_id, alb)
    #
    #     if photos is None or len(photos) == 0:
    #         pbar_alb.update(1)
    #         continue
    #
    #     total_pbar_incr = round(1 / len(photos), 2) if photos is not None else 0
    #     for photo in tqdm(photos, desc=albums[alb], unit='photo'):
    #         img_data = requests.get(photo['photo']['url']).content
    #         ya.upload_photo_to_disk('backup', f'{photo["id"]}.jpg', img_data)
    #         photos_info.append({
    #             'file_name': f'{photo["id"]}.jpg',
    #             'size': photo['photo']['type']
    #         })
    #         pbar_alb.update(total_pbar_incr)
    #
    #     pbar_alb.n = index + 1
    #     pbar_alb.refresh()
    #
    # if len(photos_info) > 0:
    #     with open('photo_info.json', 'w') as f:
    #         json.dump(photos_info, f)



