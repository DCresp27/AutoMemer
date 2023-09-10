import requests

try:
    response = requests.get("https://meme-api.com/gimme")
    data = response.json()

    image_url = data['url']

    with open("meme.jpg", "wb") as f:
        f.write(requests.get(image_url).content)
        print("Image downloaded and saved as meme.jpg")

except Exception as e:
    print(e)
