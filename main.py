import os
from dotenv import load_dotenv
from pprint import pprint
from time import sleep

from yandex_disk import YaDiskUploader
from vk_api import VkApiHandler


if __name__ == '__main__':
    load_dotenv()
    ya_disk_token = os.getenv('YA_DISK_TOKEN')
    ya = YaDiskUploader(ya_disk_token)

    # pprint(res.status_code)
    # pprint(res.json(), indent=2)

    vk_api_token = os.getenv('VK_API_TOKEN')
    vk_api_version = os.getenv('VK_API_VERSION')

    vk = VkApiHandler(vk_api_token, vk_api_version)
    _, albums = vk.get_albums('299783284')
    # albums = vk.get_all_albums(None)
    # pprint(albums, indent=2)
    #
    # root_folder_path = '/vk_photos'
    # _, resp = ya.is_folder_exists('root_folder_path')
    # print(resp)

    # resp = vk.get_user_info('id222528601')
    # pprint(resp.json(), indent=2)





