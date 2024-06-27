import json
import requests

def remove_background(img_url, api_key='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZjczM2VjYjItMmY0NS00ZjRmLWE0NWMtMTYzNWY1MTE3OTM3IiwidHlwZSI6ImFwaV90b2tlbiJ9.I6nbV889koTKmJlLvUjkGKrXwELVH2KlY75yMlpCBp8'):
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
