from PIL import Image, ImageFont, ImageDraw, ImageEnhance
import cv2
from PIL import Image
import numpy as np



# from rembg import remove
# input = Image.open('generated_images/obj_1.png')
# remove(input).save('obj_1.png')

def paste_image(back_img, front_img, x_offset, y_offset):
    # накладывает два изображения с отступом
    y1, y2 = y_offset, y_offset + front_img.shape[0]
    x1, x2 = x_offset, x_offset + front_img.shape[1]
    alpha_s = front_img[:, :, 3] / 255.0
    alpha_l = 1.0 - alpha_s
    for c in range(0, 3):
        back_img[y1:y2, x1:x2, c] = (alpha_s * front_img[:, :, c] +
                                alpha_l * back_img[y1:y2, x1:x2, c])
    return back_img

def rotate_resize_brightness(file_path, file_name, deg, img_size, size=1, brightness=1):
    # поворот изображение через PIL - сохранение повернутого изображение
    # чтение повернутого изображения через cv2
    # resize изображения по размеру шаблона
    img = Image.open(file_path)
    if deg!=0:
        img = img.rotate(deg)
    if brightness!=1:
        img = ImageEnhance.Brightness(img).enhance(brightness)
        
    file_name = f"temp_images/{file_name}_rotated.png"
    img.save(file_name,"PNG")
    print(f'Изображение {file_name} сохранено')

    img = cv2.imread(file_name, -1)
    if size!=1:
        img_size = (int(img_size[0]*size), int(img_size[0]*size))
        img = cv2.resize(img, img_size)
    
    # cv2.imwrite(f'resize.png', img)
    return img


def get_text_img(aspect_ratio, file_name, text, font_size, font_path, color, position, align):
    # сохраняет изображние с текстом по заданным параметрам
    file_name = f"temp_images/{file_name}.png"
    font = ImageFont.truetype(font_path, font_size)
    text_mask = font.getmask(text, "L")
    break_num = text.count('\n')+1
    img = Image.new("RGBA", (text_mask.size[0], text_mask.size[1]*break_num*2))
    # img = Image.open(f'template_elements/transparent_{aspect_ratio}.png') 
    draw = ImageDraw.Draw(img)
    draw.text((0,0), text, font = font, align = align, fill = color) 
    img.save(file_name,"PNG")
    
    img = cv2.imread(file_name, cv2.IMREAD_UNCHANGED)
    if color == (255, 255, 255, 255):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        x, y, w, h = cv2.boundingRect(cv2.findNonZero(gray))
        img = img[y:y+h, x:x+w]
        try:
            img = cv2.cvtColor(img, cv2.COLOR_RGB2RGBA)
            cv2.imwrite(file_name, img)
        except:
            pass
    print(f'Изображение {file_name}.png сохранено')
    return img



 

# import numpy as np
# from PIL import Image

# im_cv = cv2.imread('temp_images/title_text.png')
# gray = cv2.cvtColor(im_cv, cv2.COLOR_BGR2GRAY)
# x, y, w, h = cv2.boundingRect(cv2.findNonZero(gray))
# print(x, y, h, w)
# print(im_cv.shape)
# im = Image.open('temp_images/title_text.png')
# im.save('new_file_1.png')
# im.crop((10, 10, 10, 10))
# print(im.size)

# im = im.convert('RGBA')
# data = np.array(im)
# # just use the rgb values for comparison
# rgb = data[:,:,:3]
# color = [246, 213, 139]   # Original value
# black = [0,0,0, 255]
# white = [255,255,255,255]
# mask = np.all(rgb == color, axis = -1)
# # change all pixels that match color to white
# data[mask] = white

# # change all pixels that don't match color to black
# ##data[np.logical_not(mask)] = black
# new_im = Image.fromarray(data)
# new_im.save('new_file.png')