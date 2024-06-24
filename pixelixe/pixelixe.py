import requests

def main():
    r = requests.post("https://studio.pixelixe.com/api/graphic/automation/v2", 
        data={ "json": 
            '{ "document_uid": "---------", \
            "format": "image", "api_key": "---------------", \
            "modifications": [ { "element_name": "text-0", "type": "text", "text": "THIS IS" }, \
            { "element_name": "text-1", "type": "text", "text": "A reusable Template" } ] }'})

    print(r.status_code, r.reason)
    file = open("automated_image.png", "wb")
    file.write(r.content)
    file.close()

if __name__ == "__main__":
    main()