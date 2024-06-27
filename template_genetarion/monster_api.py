from monsterapi import client
import random
import json
import requests

def remove_background(img_url, api_key=''):
    url="https://api.edenai.run/v2/image/background_removal"
    providers = "api4ai"
    
    headers = {"Authorization": f"Bearer {api_key}"}
    json_payload={
        "providers": providers,
        "file_url": img_url
    }
    response = requests.post(url, json=json_payload, headers=headers)
    result = json.loads(response.text)
    return result[providers]['image_resource_url']


def get_generation_parametrs(aspect_ratio='landscape', # соотношение сторон
                            steps = 30, # число шагов генерации, минимум 30
                            guidance_scale = 7.5, # насколько текстовый промт влияет на изображение 
                            enhance = False, # улучшенное качество True/False
                            optimize = True, # оптимизация True/False
                            safe_filter = True, # фильтр безопасного контента
                            seed = random.randint(1, 3000), # случайное число для случайного результата                           
                            samples = 1 # число изображений
                            ):
  if aspect_ratio not in ['square', 'portrait', 'landscape']:
    aspect_ratio = 'square'
  generation_parametrs = [aspect_ratio, steps, guidance_scale, enhance, optimize, safe_filter, seed, samples]
  return generation_parametrs

def get_default_promts():
  negative_promt = '(Easy Negative), (negative_hand-neg), (worst quality:1.5),\
                            ( low quality:1.5), (normal quality:1.5), (low res), \
                            ((grayscale)),paintings, sketches, bad anatomy text, error,bad hands, \
                            extra digit, fewer digits, cropped,jpegartifacts,signature, watermark,\
                            bad feet,cropped,mutation,deformed,bad proportions,gross proportions, \
                            unreal, fake, meme, joke, disfigured, poor quality, bad, ugly,\
                            (deformed, distorted, disfigured)'
                            
  high_quality_promt = 'High Contrast, Cinematic Lighting, illuminated by neon light. . \
                        hyper detailed 8k painting, 8k concept, muted colors, bokeh, f1.0 lens'
  return high_quality_promt, negative_promt

def SDXL_generate_img(promt, negative_promt, generation_parametrs, api_key = ''):
  monster_client = client(api_key)
  aspect_ratio, steps, guidance_scale, enhance, optimize, safe_filter, seed, samples = generation_parametrs
  model = 'sdxl-base' 
  input_data = {
    'prompt': promt,
    'negprompt': negative_promt,
    'samples': samples, 
    'enhance': enhance,
    'optimize': optimize,
    'safe_filter': safe_filter,
    'steps': steps,
    'aspect_ratio': aspect_ratio,
    'guidance_scale': guidance_scale,
    'seed': seed,
  }
  result = monster_client.generate(model, input_data)
  result_url = result['output'][0]
  return result_url


def SD_background_generation(input_promt, input_negative_promt=''):
  generation_parametrs = get_generation_parametrs()
  high_quality_promt, negative_promt = get_default_promts()

  promt = ','.join([input_promt, 'no close-up, blurred background', high_quality_promt])
  negative_promt = ','.join([input_negative_promt, negative_promt])
        
  image_url = SDXL_generate_img(promt, negative_promt, generation_parametrs)
  return image_url


def SD_transparent_object_generation(input_promt, input_negative_promt=''):
  generation_parametrs = get_generation_parametrs()
  high_quality_promt, negative_promt = get_default_promts()

  promt = ','.join([input_promt,high_quality_promt])
  negative_promt = ','.join([input_negative_promt, negative_promt, 
  'colored background, clear background, blurred edges of the object'])
        
  image_url = SDXL_generate_img(promt, negative_promt, generation_parametrs)
  transparent_image_url = remove_background(image_url)
  return image_url, transparent_image_url


# input_promt = 'background for the announcement of the sale of gaming computers and peripherals, \
#             contrasting, dark room with several computers in the distance, \
#             no close-up, blurred background, good quality, photorealistic \
#             decorative smoke in the air, bright, contrasting, cyberpunk'
# image_url = SD_background_generation(input_promt)

# input_promt = 'gaming laptop isolated on white background, open, \
#                     led keyboard, led lighting around the screen, thumbnail, sale, buy, \
#                     preview, Amazon, eBay, checkout, isolated on white background\
#                     clear silhouette of the object on a white background'
# image_url = SD_transparent_object_generation(input_promt)