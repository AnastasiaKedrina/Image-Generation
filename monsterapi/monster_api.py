from monsterapi import client
# import monsterapi
import base64
import datetime
              
# Initialize the client with your API key
monster_client = client("api_key")



model = 'sdxl-base' 
# Replace with the desired model name
input_data = {
  'prompt': 'a gaming laptop with an LED keyboard and other peripherals, is in the air in decorative smoke, bright, contrasting, cyberpunk, High Contrast, Cinematic Lighting, illuminated by neon light. . hyper detailed 8k painting, 8k concept, muted colors, bokeh, f1.0 lens',
  'negprompt': 'unreal, fake, meme, joke, disfigured, poor quality, bad, ugly',
  'samples': 2,
  'enhance': True,
  'optimize': True,
  'safe_filter': True,
  'steps': 50,
  'aspect_ratio': 'square',
  'guidance_scale': 7.5,
  'seed': 2414,
}

result = monster_client.generate(model, input_data)

print(result['output'])