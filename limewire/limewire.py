import requests

url = "https://api.limewire.com/api/image/outpainting"

payload = {
  "image_asset_id": "116a972f-666a-44a1-a3df-c9c28a1f56c0",
  "direction": "UP",
  "crop_side": "LEFT"
}

headers = {
  "Content-Type": "application/json",
  "X-Api-Version": "v1",
  "Accept": "application/json",
  "Authorization": "Bearer <API_KEY>"
}

response = requests.post(url, json=payload, headers=headers)

data = response.json()
print(data)