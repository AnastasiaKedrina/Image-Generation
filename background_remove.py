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
