import requests
import json
from PIL import Image
import datetime

url = "https://api.monsterapi.ai/v1/generate/txt2img"

API_Key = ""

headers = {
"accept": "application/json",
"content-type": "application/json",
"authorization": f"Bearer {API_Key}"
}

payload = {
"prompt": "detailed sketch of lion by greg rutkowski, beautiful, intricate, ultra realistic, elegant, art by artgerm",
"negprompt": "deformed, bad anatomy, disfigured, poorly drawn face",
"samples":1,
"steps": 50,
"aspect_ratio": "square",
"guidance_scale": 7.5,
"seed": 2414
}

response = requests.post(url, headers=headers, json=payload)
print(response.text)

process_id = json.loads(response.text)['process_id']

url = f"https://api.monsterapi.ai/v1/status/{process_id}"

response = requests.get(url, headers=headers)

print(response.text)
result_url = response.text
print(result_url)


uniq_filename = str(datetime.datetime.now().date()) + '_' + str(datetime.datetime.now().time()).replace(':', '-')
result_image = Image.open(requests.get(result_url, stream=True).raw)
result_image.save(f"{uniq_filename}.jpg") 
