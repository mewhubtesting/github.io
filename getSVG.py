import requests

# URL of the SVG image to download
url = 'http://127.0.0.1:8080/profile/1'

# Send a GET request to fetch the SVG image
response = requests.get(url)

# Save the SVG image to a local file
with open('image.svg', 'wb') as f:
    f.write(response.content)

print('SVG image saved to image.svg')