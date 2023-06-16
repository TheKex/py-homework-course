import requests
from pprint import pprint

class VkApiHandler:
    base_url = 'https://api.vk.com/method/'

    def __init__(self, token, version='5.131'):
        self.params = {
            'access_token': token,
            'v': version
        }

    def get_albums(self, owner_id):
        url = VkApiHandler.base_url + 'photos.getAlbums'
        params = {'owner_id': owner_id, **self.params}
        resp = requests.get(url, params=params)
        return resp.status_code, resp.json()

    def get_all_albums(self, owner_id):
        status_code, albums = self.get_albums(owner_id)
        if status_code == 200:
            albums_dict = {
                'wall': 'фотографии со стены',
                'profile': 'фотографии профиля',
                'saved': 'сохраненные фотографии'
            }
            for alb in albums['response']['items']:
                albums_dict[alb['id']] = alb['title']
            return status_code, albums_dict
        else:
            return status_code, None

    def get_user_info(self, user_ids):
        url = VkApiHandler.base_url + 'users.get'
        params = {
            'user_ids': user_ids,
            **self.params
        }
        resp = requests.get(url, params=params)
        return resp

    def get_max_size(sizes):
        max_size_img_data = max(sizes, key=lambda size: size['height'])
        return max_size_img_data

    def get_photos(self, owner_id, album_id):
        url = VkApiHandler.base_url + 'photos.get'
        params = {
            'owner_id': owner_id,
            'album_id': album_id,
            'extended': 1,
            **self.params
        }
        resp = requests.get(url, params=params)
        if resp.status_code == 200:
            if 'response' not in resp.json():
                return None
            max_sizes = [{'id': item['id'],
                          'likes': item['likes'],
                          'photo': VkApiHandler.get_max_size(item['sizes'])} for item in resp.json()['response']['items']]
            return max_sizes
        return None

    def resolve_scree_name(self, screen_name):
        url = VkApiHandler.base_url + 'utils.resolveScreenName'
        params = {
            'screen_name': screen_name,
            **self.params
        }
        resp = requests.get(url, params=params)
        if resp.status_code == 200 and 'response' in resp.json():
            if len(resp.json().get('response')):
                return resp.json().get('response').get('object_id')
            return None
        else:
            return None

