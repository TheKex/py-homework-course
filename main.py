import os
import sys
from dotenv import load_dotenv
from pprint import pprint
from time import sleep
import json
from datetime import datetime


import requests
from tqdm import tqdm

from yandex_disk import YaDiskUploader
from vk_api import VkApiHandler


def backup_vk(vk_token, vk_user, ya_disk_token, vk_api_version='5.131', folder='backup', pb_bar=False):
    ya = YaDiskUploader(ya_disk_token)
    vk = VkApiHandler(vk_token, vk_api_version)
    user_id = vk.resolve_scree_name(vk_user) or vk_user


    json_result = ''
    return json_result


if __name__ == '__main__':
    load_dotenv()

    vk_api_token = os.getenv('VK_API_TOKEN')
    vk_api_version = '5.131'
    vk_user = None
    ya_disk_token = os.getenv('YA_DISK_TOKEN')
    ya_disk_folder = None
    json_folder = None

    # Получение значений из командной строки
    args = sys.argv
    args_len = len(args)
    if args_len > 1:
        vk_api_token = args[1]
    if args_len > 2:
        vk_user = args[2]
    if args_len > 3:
        ya_disk_token = args[3]
    if args_len > 4:
        ya_disk_folder = args[4]
    if args_len > 5:
        json_folder = args[5]

    if vk_api_token is None:
        print('Для работы скрипта, необходимо получить API токкен от ВК: \n'
              'Вы можете использовать инструкцию http://github.com\n'
              'После получения необходимо поместить токен в файл ".env" в папаку со скриптом\n'
              'Пример содержимого файла ".env" можно найти в файле ".env.example"')
        exit(0)

    is_not_user = vk_user is None
    while is_not_user:
        vk_user = input('Введите id пользователя, ссылку на страницу или короткое имя:')
        is_not_user = vk_user is None

    is_not_ya_token = ya_disk_token is None
    while is_not_ya_token:
        ya_disk_token = input('Введине токен яндекс диска:')
        is_not_ya_token = ya_disk_token is None

    default_folder = 'backup_' + datetime.now().strftime("%Y-%m-%d %H:%M:%S").replace(' ', '_')
    if ya_disk_folder is None:
        ya_disk_folder = input(f'Введите название папки на яндекс диске (по-умолчанию {default_folder}):') or default_folder

    if json_folder is None:
        json_folder = input(f'Введите папку, куда сохранить данные о фотографиях (по-умолчнию {os.getcwd()})') or os.getcwd()

    photos = backup_vk(vk_api_token, vk_user, ya_disk_token, vk_api_version='5.131', folder=ya_disk_folder, pb_bar=True)

    if len(photos) > 0:
        with open(json_folder + f'/photos_{default_folder}.json', 'w') as f:
            json.dump(photos, f)

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



