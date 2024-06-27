import requests

def create_template(image_list, text_list, UID = '', api_key=''):
  def get_text_style(text, font_size, font_weight='normal', font_style='normal'):
    # можно сделать параметры словарем и добавлять любые
    return f'<span class=\"textFitted\" style=\"display: inline-block; font-size: {font_size}px;font-weight:{font_weight};font-style:{font_style};\">{text}</span>'

  headers = {
      'Authorization': f'Bearer {api_key}',
      'Content-Type': 'application/json',
  }

  background_image_url, transparent_image_url = image_list
  header_text, subheader_text, button_text = text_list

  json_data = {
    "format": "jpeg",
    "metadata": "some text",
    "params": [
      {
        "name": "triangle_bg",
        "imageUrl": background_image_url
      },
      {
        "name": "product_image",
        "imageUrl": transparent_image_url
      },
      {
        "name": "dots_image",
        "imageUrl": "https://dynapictures.com/b/rest/public/media/94bc143016/images/ec3647afa9.png"
      },
      {
        "name": "button_text",
        "text": get_text_style(button_text, 50)
      },
      {
        "name": "text_subheading",
        "text": get_text_style(subheader_text, 40, font_style='italic')
      },
      {
        "name": "image16",
        "imageUrl": "https://dynapictures.com/b/rest/public/media/94bc143016/images/e6ff7ef2e6.png"
      },
      {
        "name": "text_heading",
        "text": get_text_style(header_text, 60, font_weight='bold')
      },
      {
        "name": "logo",
        "text": get_text_style('лого', 30)
      }
    ]
  }

  result = requests.post(f'https://api.dynapictures.com/designs/{UID}', headers=headers, json=json_data).json()
  return result
