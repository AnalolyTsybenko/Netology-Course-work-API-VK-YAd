import requests
from tqdm import tqdm
import json


class YaD:

    def __init__(self, yad_token: str, yad_folder_name: str):
        self.yad_token = yad_token
        self.yad_folder_name = yad_folder_name
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources/'
        self.headers = {
            'Authorization': f'OAuth {self.yad_token}',
            'Content-Type': 'application/json'
        }

    def create_a_folder(self):
        params = {'path': f'/{self.yad_folder_name}/'}
        requests.put(self.url, headers=self.headers, params=params)

    def upload_photo(self, photos_list: list):
        self.create_a_folder()
        result_upload = []
        status = ''
        for file in tqdm(photos_list, desc='Loading: '):
            params_upload = {
                'url': file['url'],
                'path': f'{self.yad_folder_name}/{file["name"]}',
                'overwrite': 'true'
            }
            res = requests.post(self.url+'upload', params=params_upload, headers=self.headers)
            status = res.status_code
            result_upload.append({'file_name': f'{file["name"]}.jpg', 'size': file['type_size']})

        with open('result.json', 'w') as file:
            json.dump(result_upload, file)

        if status == 202:
            print('Photos uploaded')
        else:
            print('Download interrupted')
