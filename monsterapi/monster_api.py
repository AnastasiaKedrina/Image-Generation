from monsterapi import client
from PIL import Image
import datetime
import requests
              
api_key = ''  
monster_client = client(api_key)

aspect_ratios_array = ['square', 'portrait', 'landscape']

# promt = 'a gaming laptop with an LED keyboard and other peripherals, \
#   is in the air in decorative smoke, bright, contrasting, cyberpunk, \
#   High Contrast, Cinematic Lighting, illuminated by neon light. . \
#   hyper detailed 8k painting, 8k concept, muted colors, bokeh, f1.0 lens' # промт

promt = 'gaming chair  \
in a modern and dark gaming data center (full of computer racks with rgb lights and watercooling pipes) \
dolly zoom, dutch angle, lens flare, sharp focus, intrincate details \
#   is in the air in decorative smoke, bright, contrasting, cyberpunk, \
#   High Contrast, Cinematic Lighting, illuminated by neon light. . \
#   hyper detailed 8k painting, 8k concept, muted colors, bokeh, f1.0 lens' # промт

negative_monochrome_color = 'monochrome'
negaive_promt = 'unreal, fake, meme, joke, disfigured, poor quality, bad, ugly, (deformed, distorted, disfigured)' + negative_monochrome_color # негативный промт

samples = 1 # число изображений
enhance = False # улучшенное качество True/False
optimize = True # оптимизация True/False
safe_filter = True # фильтр безопасного контента
steps = 30 # число шагов генерации, минимум 30
guidance_scale = 7.5 # насколько текстовый промт влияет на изображение 
seed = 2000 # случайное число для случайного результата
aspect_ratio = aspect_ratios_array[0] # соотношение сторон


model = 'sdxl-base' 
input_data = {
  'prompt': promt,
  'negprompt': negaive_promt,
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
print(result_url)


uniq_filename = str(datetime.datetime.now().date()) + '_' + str(datetime.datetime.now().time()).replace(':', '-')
result_image = Image.open(requests.get(result_url, stream=True).raw)
result_image.save(f"{uniq_filename}.jpg") 
