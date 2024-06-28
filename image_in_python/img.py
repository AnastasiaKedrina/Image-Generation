from PIL import Image, ImageFont, ImageDraw


# def get_text_img(img_size, file_name, text, font_size, font_path, color):
#     font = ImageFont.truetype(font_path, size=font_size)
#     text_mask = font.getmask(text, "L")
#     img = Image.new("RGBA", text_mask.size)

#     back_img = Image.open('back.png')
#     # obj_img = Image.open('front.png')

#     # back_img = back_img.resize((426, 240))
#     back_img_size = back_img.size
#     # obj_img_size = obj_img.size
#     print(img_size)
#     print(back_img_size)
#     text_img = Image.new('RGBA',  (0, 0))
#     # text_img.paste(back_img,(0,0))
#     # text_img.paste(obj_img,(100,100))
#     text_img.im.paste(color, (0, 0, 100, 100))

#     img.save(f"{file_name}.png","PNG")
#     print(f'Изображение {file_name}.png сохранено')
#     return text_img


helvetica_path = "image_in_python/fonts/helvetica_regular.otf"
text = 'LAUGHING IS THE \n BEST MEDICINE'
font_size = 20
position = (10, 10)
align = 'left'

def get_text_img(aspect_ratio, file_name, text, font_size, font_path, color):
    img = Image.open(f'template_elements/transparent_{aspect_ratio}.png') 
    draw = ImageDraw.Draw(img) 
    font = ImageFont.truetype(font_path, font_size)

    draw.text(position, text, font = font, align = align, color = color) 
    img.save(f"{file_name}.png","PNG")
    print(f'Изображение {file_name}.png сохранено')
    # image.show()
    return img

