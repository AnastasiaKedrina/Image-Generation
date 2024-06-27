import requests
import datetime
from PIL import Image

from dynapictures_api import create_template
from monster_api import SD_background_generation, SD_transparent_object_generation


def url_to_img_file(img_url, filename_prefix=''):
  uniq_filename = str(datetime.datetime.now().date()) + '_' + str(datetime.datetime.now().time()).replace(':', '-')
  result_image = Image.open(requests.get(img_url, stream=True).raw)
  if filename_prefix and not filename_prefix.isspace():
    uniq_filename = f'{filename_prefix}___{uniq_filename}'
  result_image.save(f"{uniq_filename}.png")



input_promt = 'dark room with several computers in the distance, contrasting, \
                background for the announcement of the sale of gaming computers and peripherals, \
                decorative smoke in the air, bright, contrasting, cyberpunk'
background_image_url = SD_background_generation(input_promt)
print(f'Сгенерировано изображение для фона: {background_image_url}')
url_to_img_file(background_image_url)

input_promt = 'gaming laptop isolated on white background, open, \
                led keyboard, led lighting around the screen, thumbnail, sale, buy, \
                preview, Amazon, eBay, checkout, isolated on white background\
                clear silhouette of the object on a white background'
obj_image_url, transparent_image_url = SD_transparent_object_generation(input_promt)
print(f'Сгенерировано изображение на белом фоне:{obj_image_url}')
print(f'Изображение без фона:{transparent_image_url}')
url_to_img_file(obj_image_url)
url_to_img_file(transparent_image_url)
image_list = [background_image_url, transparent_image_url]



# image_list = ['https://img.freepik.com/free-vector/vibrant-summer-ombre-background-vector_53876-105765.jpg?size=626&ext=jpg&ga=GA1.1.1141335507.1719496800&semt=ais_user', 'https://png.pngtree.com/png-clipart/20230927/original/pngtree-man-in-shirt-smiles-and-gives-thumbs-up-to-show-approval-png-image_13146336.png']



header_text = 'Супер-заголовок'
subheader_text = 'какой-то текст о компании'
button_text = 'КУПИТЬ ВЫГОДНО'
text_list = [header_text, subheader_text, button_text]

template_url = create_template(image_list, text_list)['imageUrl']
print(f'Шаблон сгенерирован: {template_url}')

# img_url = 'https://processed-model-result.s3.us-east-2.amazonaws.com/48ea8e66-7600-457d-b16e-b6b8aa5f113b_0.png'
url_to_img_file(template_url)
print(f'Шаблон сохранен в файл png')