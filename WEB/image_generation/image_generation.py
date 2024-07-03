import requests
import datetime
from PIL import Image
import sys
import json


def url_to_img_file(img_url):
  folder_name = 'image_generation/result_templates'
  uniq_filename = str(datetime.datetime.now().date()) + '_' + str(datetime.datetime.now().time()).replace(':', '-')
  result_image = Image.open(requests.get(img_url, stream=True).raw)
  result_image.save(f"{folder_name}/all/{uniq_filename}.png")
  result_image.save(f"{folder_name}/result.png")
  
# if __name__ == "__main__":
#     import sys
#     url_to_img_file(sys.argv[1])
#     # url_to_img_file('https://processed-model-result.s3.us-east-2.amazonaws.com/a6d21138-ec38-4d7a-8bd0-8fcfbf304f61_0.png')


if __name__ == "__main__":
    # Expecting to receive JSON data as input
    input_data = json.load(sys.stdin)
    description = input_data.get("description")
    size = input_data.get("size")
    url_to_img_file(description)