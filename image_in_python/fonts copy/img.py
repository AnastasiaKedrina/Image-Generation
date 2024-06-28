from PIL import Image, ImageFont

text = "Hello world!"
font_size = 36
font_filepath = "image_in_python/fonts/helvetica_regular.otf"
color = (67, 33, 116, 155)

font = ImageFont.truetype(font_filepath, size=font_size)
# text_mask = font.getmask(text, "L")
# img = Image.new("RGBA", text_mask.size)


#Read the two images
back_img = Image.open('back.png')
obj_img = Image.open('front.png')

# back_img = back_img.resize((426, 240))
# back_img_size = back_img.size
# obj_img_size = obj_img.size
new_image = Image.new('RGBA', back_img.size)
new_image.paste(back_img,(0,0))
new_image.paste(obj_img,(100,100))


new_image.im.paste(color, back_img.size)


new_image.save("merged_image.png","PNG")