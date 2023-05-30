import requests


class YaDiskUploader:
    base_url = 'https://cloud-api.yandex.net/v1/disk/'

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def upload_photo_to_disk(self, path, file_name, photo_data):
        url = YaDiskUploader.base_url + f'resources/upload'
        params = {
            'path': f'{path}/{file_name}'
        }
        resp = requests.get(url=url, params=params, headers=self.get_headers())
        if 'href' not in resp.json():
            return None
        return requests.post(url=resp.json()['href'], files={'file': photo_data})

    def is_folder_exists(self, path_in_disk):
        url = YaDiskUploader.base_url + f'resources'
        params = {
            'path': path_in_disk
        }
        resp = requests.get(url, params=params, headers=self.get_headers())
        if resp.status_code == 200:
            return True, resp
        if resp.status_code == 404:
            return False, resp
        return None, resp

    def create_folder(self, path):
        url = YaDiskUploader.base_url + f'resources'
        params = {
            'path': path
        }
        resp = requests.put(url, params=params, headers=self.get_headers())



