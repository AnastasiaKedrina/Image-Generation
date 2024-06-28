from PIL import Image, ImageFilter, ImageDraw

back_img = Image.open('back.png')
obj_img = Image.open('front.png')


# cord = (10, 10, 640, 340) # лево, верх, право, низ
# new_picture = picture.crop(cord)
# resized_image = image.resize((320, 320))
# edges = image.filter(ImageFilter.FIND_EDGES)

# url = 'http://pena.marketing/images/Logo1.png'
# raw = requests.get(url, stream=True).raw
# Image.open(raw).show()


# draw = ImageDraw.Draw(new_img)
# draw.rectangle((200, 50, 300, 300), fill ='green')


rgba = obj_img.convert("RGBA") 
datas = rgba.getdata() 
  
newData = [] 
for item in datas: 
    if item[0] == 0 and item[1] == 0 and item[2] == 0:  # finding black colour by its RGB value 
        # storing a transparent value when we find a black colour 
        newData.append((255, 255, 255, 0)) 
    else: 
        newData.append(item)  # other colours remain unchanged 
  
rgba.putdata(newData) 

# new = Image.new(mode, shape, color)
new_img = Image.new('RGBA', back_img.size)
new_img.paste(back_img,(0,0))
new_img.paste(rgba,(0,0))

result = new_img


result.show()
result.save("merged_image.png","PNG")

  