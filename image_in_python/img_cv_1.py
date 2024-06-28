import cv2
import numpy as np
import datetime
from PIL import ImageFont, ImageDraw, Image

from img import get_text_img

def paste_image(back_img, front_img, x_offset, y_offset):
    y1, y2 = y_offset, y_offset + front_img.shape[0]
    x1, x2 = x_offset, x_offset + front_img.shape[1]
    alpha_s = front_img[:, :, 3] / 255.0
    alpha_l = 1.0 - alpha_s
    for c in range(0, 3):
        back_img[y1:y2, x1:x2, c] = (alpha_s * front_img[:, :, c] +
                                alpha_l * back_img[y1:y2, x1:x2, c])
    return back_img

def add_line_break(text, length):
    s = []
    c = 0 
    for i in text.split(' '):
        c += len(i)+1
        if c>length:
            s.append('\n')   
        s.append(i)
    return ' '.join(s)

def rotate_img(file_name, deg):
    img = Image.open(f"{file_name}.png")
    img = img.rotate(deg)
    file_name = f"{file_name}_rotated.png"
    img.save(file_name,"PNG")
    print(f'Изображение {file_name} сохранено')
    return img

helvetica_path = "image_in_python/fonts/helvetica_regular.otf"
colors = {
    'white' : (255, 255, 255),
    'black' : (0, 0, 0)
}
texts = {
    'title_text':{
        'text':add_line_break("ИГРОВАЯ МЫШЬ", 7),
        'pos':(10, 10),
        'font': helvetica_path,
        'font_size':56,
        'color': colors['white']
    }, 
    'subtitle_text':{
        'text':add_line_break("6 кнопок полностью программируемые", 20),
        'pos':(10, 300),
        'font': helvetica_path,
        'font_size':36,
        'color': colors['white']
    } 
}
aspect_ratios_array = ['square', 'portrait', 'landscape']
aspect_ratio = aspect_ratios_array[1]


back_img = cv2.imread("back.png", -1)
img_size = (back_img.shape[1], back_img.shape[0])

white_diagonal_img = cv2.imread("template_elements/white_diagonal.png", -1)
rotate_img("obj", -45)
obj_img = cv2.resize(cv2.imread("obj_rotated.png", -1), img_size)
# obj_img = cv2.rotate(obj_img, cv2.ROTATE_180)

texts_layers = []
for text, params in texts.items():
    current_text = text
    current_text_d = texts[current_text]
    text_img = get_text_img(aspect_ratio, current_text, 
                            current_text_d['text'], current_text_d['font_size'], 
                            current_text_d['font'], current_text_d['color'], 
                            current_text_d['pos'], align = 'left')
    current_text_img = cv2.imread(f"{current_text}.png", -1)
    texts_layers.append(current_text_img)

design_elements = [white_diagonal_img]
layers = [back_img, *design_elements, obj_img, *texts_layers]

image = paste_image(layers[0], layers[1], 0, 0)
for layer in layers[2:]:
    image = paste_image(image, layer, 0, 0)
    image = paste_image(image, layer, 0, 0)

uniq_filename = str(datetime.datetime.now().date()) + '_' + str(datetime.datetime.now().time()).replace(':', '-')
cv2.imwrite(f'{uniq_filename}.png', image)
print('---итоговый шаблон сохранен')

# cv2.imshow('img', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
