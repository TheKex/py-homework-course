import requests


class GoogleDiskUploader:
    base_url = 'https://www.googleapis.com'

    def __init__(self, token):
        self.token = token

    def upload_file(self, path, file):
        url = GoogleDiskUploader.base_url + '/upload/drive/v3/files'
        params = {
            'uploadType': 'media'
        }
        heders = {

        }
