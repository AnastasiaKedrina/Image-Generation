import requests
import datetime
from PIL import Image


def url_to_img_file(img_url, filename='uniq', filename_prefix=''):
  if filename == 'uniq':
    img_filename = str(datetime.datetime.now().date()) + '_' + str(datetime.datetime.now().time()).replace(':', '-')
    if filename_prefix and not filename_prefix.isspace():
        img_filename = f'{filename_prefix}___{img_filename}'
    result_image = Image.open(requests.get(img_url, stream=True).raw)
    result_image.save(f"image_generation/{img_filename}.png")
  else:
    img_filename = filename
    result_image = Image.open(requests.get(img_url, stream=True).raw)
    result_image.save(f"{img_filename}.png")
  
if __name__ == "__main__":
    import sys
    url_to_img_file(sys.argv[1])
    # url_to_img_file('https://processed-model-result.s3.us-east-2.amazonaws.com/a6d21138-ec38-4d7a-8bd0-8fcfbf304f61_0.png')