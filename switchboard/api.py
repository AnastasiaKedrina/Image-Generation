import requests

headers = {
    'Content-Type': 'application/json',
    'X-API-Key': '--------------',
}

json_data = {
    'template': 'golden-gate',
    'sizes': [
        {
            'width': 1920,
            'height': 1080,
        },
    ],
    'elements': {
        'backdrop': {
            'url': 'https://via.placeholder.com/500/500',
        },
        'quote': {
            'text': 'Gray skies are just clouds passing over.',
        },
        'person': {
            'text': 'Duke Ellington ',
        },
        'quote-symbol': {
            'url': 'https://via.placeholder.com/500/500',
        },
    },
}

response = requests.post('https://api.canvas.switchboard.ai/', headers=headers, json=json_data)
print(response.json())
# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{\n         "template": "golden-gate",\n         "sizes": [\n           {\n               "width": 1920,\n               "height": 1080\n           }\n         ],\n         "elements": {\n            "backdrop": {\n                 "url": "https://via.placeholder.com/500/500"\n             },\n            "quote": {\n                 "text": "Gray skies are just clouds passing over."\n             },\n            "person": {\n                 "text": "Duke Ellington "\n             },\n            "quote-symbol": {\n                 "url": "https://via.placeholder.com/500/500"\n             }\n         }\n     }'
#response = requests.post('https://api.canvas.switchboard.ai/', headers=headers, data=data)
