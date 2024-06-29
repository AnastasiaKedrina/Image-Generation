import requests
import datetime
from PIL import Image
import json
from rembg import remove

from monster_api import SD_background_generation, SD_transparent_object_generation
from template import create_template_1



def url_to_img_file(img_url, filename='uniq', filename_prefix=''):
  if filename == 'uniq':
    img_filename = str(datetime.datetime.now().date()) + '_' + str(datetime.datetime.now().time()).replace(':', '-')
    if filename_prefix and not filename_prefix.isspace():
        img_filename = f'{filename_prefix}___{img_filename}'
    result_image = Image.open(requests.get(img_url, stream=True).raw)
    result_image.save(f"rest_images/{img_filename}.png")
  else:
    img_filename = filename
    result_image = Image.open(requests.get(img_url, stream=True).raw)
    result_image.save(f"{img_filename}.png")
  



def get_promt_style(input_style):
    styles_file = open("styles.csv", "r").readlines()
    for style in styles_file[1:]:
        s = style.split(',\"')
        if len(s)==2: s.append('')
        stylename, promt, negative_promt = s
        promt = promt.replace('\"', '')
        negative_promt = negative_promt.replace('\"', '')  
        if input_style in stylename:
            return promt, negative_promt


def remove_background(file_name):
    input = Image.open(f'{file_name}.png')
    remove(input).save(f'{file_name}_transparent.png')
    print(f'Изображение {file_name}_transparent.png сохранено')


aspect_ratio = 'portrait'
style_name = 'PHOTOGRAPHY'
style_promt, style_negative_promt = get_promt_style(style_name)

# object_promt = 'gaming laptop, open, led keyboard, led lighting around the screen, gaming computers and peripherals'
object_promt = 'computer gaming mouse, led light, led mouse buttons'
colors_promt = 'dark, contrasting, decorative smoke in the air, contrasting, cyberpunk, illuminated by neon light'

input_promt = f'room designed for {object_promt}, all the objects in the room are positioned correctly and stylized, ' + style_promt + colors_promt
background_image_url = SD_background_generation(input_promt, style_negative_promt,  aspect_ratio=aspect_ratio)
print(f'Сгенерировано изображение для фона: {background_image_url}')
back_file_path = 'generated_images/back'
url_to_img_file(background_image_url)#, filename_prefix=style_name)
url_to_img_file(background_image_url, back_file_path)

input_promt = object_promt
obj_image_url = SD_transparent_object_generation(input_promt)#, style_negative_promt)
print(f'Сгенерировано изображение на белом фоне:{obj_image_url}')
obj_file_path = 'generated_images/obj'
url_to_img_file(obj_image_url)#, style_name)
url_to_img_file(obj_image_url, obj_file_path)#, style_name)

# x = input('----')
remove_background(obj_file_path)
obj_file_path = obj_file_path+'_transparent'

create_template_1(back_file_path, obj_file_path, aspect_ratio)
