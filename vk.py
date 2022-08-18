import requests


class Vk:

    def __init__(self, vk_token: str, vk_id: str, photo_count: int):
        self.vk_token = vk_token
        self.vk_id = vk_id
        self.url = 'https://api.vk.com/method/photos.get'
        self.params = {
            'access_token': vk_token,
            'v': '5.131',
            'owner_id': vk_id,
            'album_id': 'profile',
            'extended': 'likes',
            'photo_sizes': '1',
            'count': photo_count
        }

    def get_photo(self):
        response = requests.get(self.url, params=self.params)
        return response.json()['response']['items']

    def collect_photos(self):
        photos_list = []
        size_types = ('w', 'z', 'y', 'x', 'm', 's')
        for item in self.get_photo():
            data = {}
            name_photo = str(item['likes']['count'])
            if name_photo in [file['name'] for file in photos_list]:
                data['name'] = name_photo + '_' + str(item['date'])
            else:
                data['name'] = name_photo
            for size_type in reversed(size_types):
                if size_type in [size['type'] for size in item['sizes']]:
                    data['type_size'] = size_type
            for size in item['sizes']:
                if size['type'] == data['type_size']:
                    data['url'] = size['url']
            photos_list.append(data)

        return photos_list
