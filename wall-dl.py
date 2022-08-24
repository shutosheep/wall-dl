import sys
import requests
import json
import os

def get_wallpaper(query):
    url = f"https://wallhaven.cc/api/v1/search?atleast=1920x1080&q={query}"
    response = requests.get(url).json()
    links = []
    for link in response["data"]:
        links.append(link["path"])
    return links

def get_path():
    path = os.path.dirname(os.path.abspath(__file__))
    return path

def get_filename(url):
    filename = url.split("/")[-1]
    return filename

def download_wallpaper(url, path):
    response = requests.get(url)
    print(f"Downloading {url}")
    open(path, 'wb').write(response.content)

# Check if search query is given
if len(sys.argv) < 2:
    print('Usage: python wall-dl.py "Search query"')
    quit()

query = sys.argv[1]
links = get_wallpaper(query)
for link in links:
    path = os.path.join(get_path(), get_filename(link))
    download_wallpaper(link, path)
print(f"Downloaded {len(links)} wallpapers")
