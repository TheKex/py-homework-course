import requests


class VkApiHandler:
    base_url = 'https://api.vk.com/method/'

    def __init__(self, token, version='5.131'):
        self.params = {
            'access_token': token,
            'v': version
        }

    def get_albums(self, owner_id):
        '''
        Возвращает список альбомов пользователя или сообщества
        :param owner_id: Идентификатор пользователя или сообщества, которому принадлежат альбомы.
        :return:
        '''
        url = VkApiHandler.base_url + 'photos.getAlbums'
        params = {'owner_id':owner_id, **self.params}
        resp = requests.get(url, params=params)
        return resp.status_code, resp.json()

    def get_all_albums(self, owner_id):
        _, albums = self.get_albums(owner_id)
        albums_dict = {
            'wall': 'фотографии со стены',
            'profile': 'фотографии профиля',
            'saved': 'сохраненные фотографии'
        }
        for alb in albums['response']['items']:
            albums_dict[alb['id']] = alb['title']
        return albums_dict

    def get_user_info(self, user_id):
        url = VkApiHandler.base_url

