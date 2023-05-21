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



