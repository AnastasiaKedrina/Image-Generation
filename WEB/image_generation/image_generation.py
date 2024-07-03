import requests
import datetime
import json
import sys
from PIL import Image
from rembg import remove

from monster_api import SD_background_generation, SD_transparent_object_generation
from template import create_square_template_1, create_square_template_2
from template import create_portrait_template_1
from template import create_landscape_template_1
from text_funcs import get_GPT_headings, phone_format


def removed_bg_url_edenai_API(img_url, api_key='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZjczM2VjYjItMmY0NS00ZjRmLWE0NWMtMTYzNWY1MTE3OTM3IiwidHlwZSI6ImFwaV90b2tlbiJ9.I6nbV889koTKmJlLvUjkGKrXwELVH2KlY75yMlpCBp8'):
    url="https://api.edenai.run/v2/image/background_removal"
    providers = "api4ai"
    
    headers = {"Authorization": f"Bearer {api_key}"}
    json_payload={
        "providers": providers,
        "file_url": img_url
    }
    response = requests.post(url, json=json_payload, headers=headers)
    result = json.loads(response.text)
    print(f'Изображение без фона: {result[providers]["image_resource_url"]}')
    return result[providers]['image_resource_url']

def removed_bg_url_removal_API(file_path):
  url = "https://api.removal.ai/3.0/remove"
  payload={'image_url': 'url_to_image'}
  files=[('image_file',('(PNG Image, 1024 × 1024 pixels).png',open(file_path+'.png','rb'),'image/png'))]
  headers = {
    'Rm-Token': 'E6BEE6CF-995E-CFF5-F0FA-60EEE4D48102'
  }
  response = requests.request("POST", url, headers=headers, data=payload, files=files)
  return response.text


def url_to_img_file(img_url, filename = 'uniq'):
  result_image = Image.open(requests.get(img_url, stream=True).raw)
  if filename == 'uniq':
    uniq_filename = str(datetime.datetime.now().date()) + '_' + str(datetime.datetime.now().time()).replace(':', '-')
    file_path = f"image_generation/rest_images/{uniq_filename}.png"
  else:
    file_path = f"{filename}.png"
  result_image.save(file_path)
  print(f'Изображение {file_path} сохранено')


# def url_to_img_file(img_url, filename='uniq', filename_prefix=''):
#   if filename == 'uniq':
#     img_filename = str(datetime.datetime.now().date()) + '_' + str(datetime.datetime.now().time()).replace(':', '-')
#     if filename_prefix and not filename_prefix.isspace():
#         img_filename = f'{filename_prefix}___{img_filename}'
#     result_image = Image.open(requests.get(img_url, stream=True).raw)
#     result_image.save(f"rest_images/{img_filename}.png")
#   else:
#     img_filename = filename
#     result_image = Image.open(requests.get(img_url, stream=True).raw)
#     result_image.save(f"{img_filename}.png")
  

def get_promt_style(input_style):
    styles_file = open("image_generation/generation_styles.csv", "r").readlines()
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
    img = remove(input)
    img.save(f'{file_name}_transparent.png')
    print(f'Изображение {file_name}_transparent.png сохранено')

def generate_and_save_image(img_type, object_promt, file_path, style, color):
  style_promt, style_negative_promt = style
  colors_promt, colors_negative_promt = color

  if img_type=='back':
    input_promt = f'room designed for {object_promt}, all the objects in the room are positioned correctly and stylized, ' + style_promt + colors_promt
    # background_img_url = SD_background_generation(input_promt, style_negative_promt) #colors_negative_promt
    background_img_url = 'https://processed-model-result.s3.us-east-2.amazonaws.com/8a4077ee-f1dd-4821-934e-98a090ae3126_0.png'
    print(f'Сгенерировано изображение для фона: {background_img_url}')
    url_to_img_file(background_img_url)#, filename_prefix=style_name)
    url_to_img_file(background_img_url, file_path)
    return file_path
  else:
    # obj_img_url = SD_transparent_object_generation(object_promt)#, style_negative_promt)
    obj_img_url = 'https://processed-model-result.s3.us-east-2.amazonaws.com/f2246e88-0749-4ff6-bf40-1d5fa5af1e8c_0.png'
    print(f'Сгенерировано изображение на белом фоне:{obj_img_url}')
    url_to_img_file(obj_img_url, file_path)#, style_name)
    url_to_img_file(removed_bg_url_edenai_API(obj_img_url), file_path+'_transparent')
    # url_to_img_file(removed_bg_url_removal_API(file_path), file_path+'_transparent')
    # remove_background(file_path)




if __name__ == "__main__":

  input_data = json.load(sys.stdin)

  form = [
          input_data.get("field_1"),
          input_data.get("field_2"),
          input_data.get("field_3"),
          input_data.get("field_4"),
          input_data.get("field_5"), 
          input_data.get("field_6"), 
          input_data.get("field_7"),
          input_data.get("field_8"),
          input_data.get("field_9"), 
          input_data.get("field_10"), 
          input_data.get("field_11")
  ]
  
  print(form)
  # description = input_data.get("description")
  # size = input_data.get("size")
  # url_to_img_file(description)














  fonts = {
      'helvetica': "image_generation/fonts/helvetica_regular.otf"
      }
  colors = {
      # RGBA
      # используются для текста, расчитано только на белый и черный, так как убирается фон
      'white' : (255, 255, 255, 255),
      'black' : (0, 0, 0, 255)
  }

  aspect_ratios = {'square': {'size':(1024, 1024), 'funcs':[create_square_template_1, create_square_template_2]},
                        'portrait': {'size':(768, 1024), 'funcs':[create_portrait_template_1]},
                        'landscape': {'size':(1024, 768), 'funcs':[create_landscape_template_1]}}

  style_name = 'PHOTOGRAPHY'
  # object_promt = 'gaming laptop, open, led keyboard, led lighting around the screen, gaming computers and peripherals'
  object_promt = 'computer gaming mouse, led light, led mouse buttons'

  style_promt, style_negative_promt = get_promt_style(style_name)
  colors_promt = 'dark, contrasting, decorative smoke in the air, contrasting, cyberpunk, illuminated by neon light'
  style = [style_promt, style_negative_promt] 
  color = [colors_promt, '']

  parsed_data, gpt_output = get_GPT_headings()
  text_data = {
    'title_text': gpt_output['Заголовок'].replace('Заголовок: ', ''),
    'subtitle_text': gpt_output['Текст'].replace('Текст: ', ''),
    'address_text': 'ул. Ленина д.3',
    'phone_text': phone_format('88005353500'),
    'button_text': 'Купить'
  }

  obj_file_path = 'image_generation/generated_images/obj'
  back_file_path = 'image_generation/generated_images/back'
  # --генерация изображений
  # generate_and_save_image('back' , object_promt, back_file_path, style, color)
  # generate_and_save_image('object' , object_promt, obj_file_path, style, color)
  obj_file_path = obj_file_path+'_transparent'
 
  # --создание шаблона
  aspect_ratio = 'square'
  # create_square_template_1(back_file_path, obj_file_path, aspect_ratio, (1024, 1024), fonts, colors, text_data)
  # create_portrait_template_1(back_file_path, obj_file_path, aspect_ratio, (768, 1024), fonts, colors, text_data)
  # create_landscape_template_1(back_file_path, obj_file_path, aspect_ratio, (1024, 768), fonts, colors, text_data)

