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
            if resp.json()['type'] == 'dir':
                return True, resp
            else:
                return False, resp
        return False, resp

    def create_folder(self, path):
        url = YaDiskUploader.base_url + f'resources'
        params = {
            'path': path
        }
        resp = requests.put(url, params=params, headers=self.get_headers())
        return resp

    def force_create_folder(self, path):
        folders = path.split('/')

        if len(folders) == 1:
            is_exists, _ = self.is_folder_exists(folders[0])
            if is_exists:
                return True
            else:
                return self.create_folder(folders[0])

        tmp = folders[0]
        nested_folders = [{'exists': None,
                           'path': tmp}]
        for i in folders[1::]:
            tmp = tmp + '/' + i
            nested_folders.append({'exists': None,
                                   'path': tmp})

        for index, folder in enumerate(nested_folders[::-1]):
            is_exists, resp = self.is_folder_exists(folder['path'])
            nested_folders[-index - 1]['exists'] = is_exists

        for folder in nested_folders:
            if not folder['exists']:
                self.create_folder(folder['path'])
        return True

