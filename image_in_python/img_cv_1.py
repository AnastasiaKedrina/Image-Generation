import cv2
import numpy as np
import datetime
from PIL import ImageFont, ImageDraw, Image

from img import get_text_img

def add_text_to_image(text, font, color, background_color=(255, 255, 255), transparency=255):
    # Создаем временное изображение для определения размеров текста
    text_img = Image.new('RGBA', (1, 1))
    draw = ImageDraw.Draw(text_img)

    # Получаем размеры изображения текста
    text_bbox = draw.textbbox((0, 0), text, font)

    # Создаем изображение текста с заданным цветом и фоном
    text_img = Image.new('RGBA', (text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]),
        background_color + (transparency,))
    draw = ImageDraw.Draw(text_img)
    draw.text((-text_bbox[0], -text_bbox[1]), text, font=font, fill=color)

    return np.array(text_img)

def putText(
    cv2_img, text, text_position_x, text_position_y,
    font_size=36, color=(255, 255, 255), background_color=(255, 255, 255), transparency=0):
    font_path = r'image_in_python\fonts\helvetica_regular.otf'
    font = ImageFont.truetype(font_path, font_size)

    text_img = add_text_to_image(text, font, color, background_color, transparency)
    text_height, text_width = text_img.shape[:2]

    # Проверка размера текста перед вставкой
    if (text_position_y + text_height > cv2_img.shape[0]):
        text_img = text_img[:cv2_img.shape[0] - text_position_y, :]
        text_height = text_img.shape[0]
    if (text_position_x + text_width > cv2_img.shape[1]):
        text_img = text_img[:, :(cv2_img.shape[1] - text_position_x)]
        text_width = text_img.shape[1]

    # Обработка альфа-канала
    alpha = text_img[:, :, 3] / 255.0
    for c in range(3):
        cv2_img[text_position_y:text_position_y + text_height, text_position_x:text_position_x + text_width, c] = \
            cv2_img[text_position_y:text_position_y + text_height, text_position_x:text_position_x + text_width, c] * \
            (1 - alpha) + text_img[:, :, c] * alpha


def paste_image(back_img, front_img, x_offset, y_offset):
    y1, y2 = y_offset, y_offset + front_img.shape[0]
    x1, x2 = x_offset, x_offset + front_img.shape[1]
    alpha_s = front_img[:, :, 3] / 255.0
    alpha_l = 1.0 - alpha_s
    for c in range(0, 3):
        back_img[y1:y2, x1:x2, c] = (alpha_s * front_img[:, :, c] +
                                alpha_l * back_img[y1:y2, x1:x2, c])
    return back_img

white = (255, 255, 255)
black = (0, 0, 0)

# aspect_ratios_array = ['square', 'portrait', 'landscape']
back_img = cv2.imread("back.png", -1)
img_size = (back_img.shape[1], back_img.shape[0])

white_diagonal_img = cv2.imread("template_elements/white_diagonal.png", -1)
obj_img = cv2.resize(cv2.imread("obj.png", -1), img_size)

image = paste_image(back_img, white_diagonal_img, 0, 0)
image = paste_image(image, obj_img, *(0, 0))

# photo = np.zeros((*img_size, 3), dtype=np.uint8)
# cv2.line(photo, (100, 100), (600, 100), (101, 44, 158), thickness=3)
cv2.rectangle(image, (100, 150), (220, 350), (101, 44, 158), thickness=3)

helvetica_path = "image_in_python/fonts/helvetica_regular.otf"
text = {
    'title_text':{
        'text':"ИГРОВАЯ МЫШЬ",
        # 'text':"AAA",
        'pos':(10, 10),
        'font': helvetica_path,
        'font_size':56,
        'color': black
    }
}
# current_text = 'title_text'
# title_text = text['title_text']
# putText(image, title_text['text'], *title_text['pos'], title_text['font_size'], title_text['color'])

aspect_ratio = 'portrait'
current_text = 'title_text'
current_text_d = text[current_text]
text_img = get_text_img(aspect_ratio, current_text, current_text_d['text'], current_text_d['font_size'], current_text_d['font'], current_text_d['color'])

uniq_filename = str(datetime.datetime.now().date()) + '_' + str(datetime.datetime.now().time()).replace(':', '-')
cv2.imwrite(f'{uniq_filename}.png', image)

# cv2.imshow('img', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
