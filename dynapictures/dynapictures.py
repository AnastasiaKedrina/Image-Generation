import requests

headers = {
    'Authorization': 'Bearer API_KEY',
    'Content-Type': 'application/json',
}

json_data = {
    'params': [
        {
            'name': 'triangle_bg',
            'imageUrl': 'https://dynapictures.com/images/banners/cat1.jpeg',
            'borderColor': '#ddd',
            'borderWidth': '2px',
            'borderRadius': '5px',
            'opacity': 1,
        },
    ],
}

response = requests.post('https://api.dynapictures.com/designs/694417c06e', headers=headers, json=json_data)
print(response.json())
# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"params":[{"name":"triangle_bg","imageUrl":"https://dynapictures.com/images/banners/cat1.jpeg","borderColor":"#ddd","borderWidth":"2px","borderRadius":"5px","opacity":1}]}'
#response = requests.post('https://api.dynapictures.com/designs/694417c06e', headers=headers, data=data)