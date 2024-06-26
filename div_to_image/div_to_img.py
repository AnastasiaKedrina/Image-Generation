from html2image import Html2Image
import datetime
import json
import requests
from PIL import Image
import convertapi


import os
import shutil

def delete_file_is_exists(filename):
    try:
        os.remove(filename)
    except OSError:
        pass

def move_style_file(style_changes_filename):
    try:
        path_from = rf'D:\Downloads\{style_changes_filename}'
        path_to = r'D:\Desktop\Новая папка\ИГУ\git-clone\Image-Generation\div_to_image'
        shutil.move(path_from, path_to)
    except FileNotFoundError:
        print(f'Файл "{style_changes_filename}" не найден в папке загрузок')


# def get_params_dict(css, classname):
#     font_size = 10;
#     is_class = False
#     is_needed_class = False

#     for line in css:
#         if '.'+classname+'{' in line:
#             is_needed_class = True
#         if '{' in line:
#             is_class = True
#         if '}' in line:
#             is_class = False
#             is_needed_class = False

#         if is_class and is_needed_class:
#             if 'font-size' in line:
#                 font_size = int(line.split(':')[1].split(' ')[1])
#             if 'background-color' in line:
#                 background_color = line.split(':')[1].split(' ')[1][:-1]
#     params = {'font_size':font_size, 
#                 'background_color':background_color}
#     return params

def replace_params_in_css(css, classname, params_dict):
    font_size = 10;
    is_class = False
    is_needed_class = False
    new_css = ''

    for line in css:
        if '.'+classname+'{' in line:
            is_needed_class = True
        if '{' in line:
            is_class = True
        elif '}' in line:
            is_class = False
            is_needed_class = False

        if is_class and is_needed_class:
            for parametr, value in params_dict.items():
                if parametr.replace('_', '-') in line:
                    prev_value = line.split(':')[1].split(' ')[1]
                    prev_value = prev_value.replace(';', '').replace('px', '')
                    value = value.replace(';', '').replace('px', '')
                    line = line.replace(prev_value, value)
        new_css += line
    return new_css

style_changes_filename = 'style_changes.json'
delete_file_is_exists(style_changes_filename)
move_style_file(style_changes_filename)

html = open("div_to_image.html", "r").read()
main_css = open("style/style.css", "r").read()
ad_div_css = open("style/ad_div_style.css", "r").readlines()
with open(style_changes_filename) as json_file:
    style_changes = json.load(json_file)

# params_dict = get_params_dict(ad_div_css, 'ad_div')
# font_size = params_dict['font_size']
# background_color = params_dict['background_color']

css = replace_params_in_css(ad_div_css, 'ad_div', style_changes)
# css = css + main_css
# css = ad_div_css

uniq_filename = str(datetime.datetime.now().date()) + '_' + str(datetime.datetime.now().time()).replace(':', '-')
# Html2Image().screenshot(html_str=html, css_str=css, save_as=f'{uniq_filename}.png')


image_url = 'https://hcti.io/v1/image/5fc519b3-f0ea-44a8-8f2e-7d4b9d6d8372'
# # https://hcti.io/v1/image/7ed741b8-f012-431e-8282-7eedb9910b32
# result_image = Image.open(requests.get(image_url, stream=True).raw)
# result_image.save(f"{uniq_filename}.png") 


