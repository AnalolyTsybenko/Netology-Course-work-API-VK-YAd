from vk import Vk
from ya import YaD

vk_id = str('')
vk_token = str('')
yad_token = str('')
yad_folder_name = str('')
photo_count = int(5)

if __name__ == '__main__':
    vk = Vk(vk_token, vk_id, photo_count)
    yad = YaD(yad_token, yad_folder_name)
    yad.upload_photo(vk.collect_photos())
