import sys
import requests
import json
import os

# Use DL_DIR to specify where to save wallpapers. If this variable does not
# exist wallpapers will be saved at the same directory of this file(wall-dl.py)

# DL_DIR = os.path.join(os.path.expanduser('~'), "wallpaper")

def get_wallpaper(query):
    url = f"https://wallhaven.cc/api/v1/search?atleast=1920x1080&q={query}"
    response = requests.get(url).json()
    links = []
    for link in response["data"]:
        links.append(link["path"])
    return links

def get_filename(url):
    filename = url.split("/")[-1]
    return filename

def download_wallpaper(url):
    response = requests.get(url)
    path = DL_DIR + "/" + get_filename(url)
    print(f"Downloading {url}")
    open(path, 'wb').write(response.content)

# Check if search query is given
if len(sys.argv) < 2:
    print('Usage: python wall-dl.py "Search query"')
    quit()

# Check DL_DIR is defined
if "DL_DIR" not in globals():
    # Define directory to be the same of this file
    DL_DIR = os.path.dirname(os.path.abspath(__file__))

query = sys.argv[1]
links = get_wallpaper(query)
for link in links:
    download_wallpaper(link)
print(f"Downloaded {len(links)} wallpapers")
