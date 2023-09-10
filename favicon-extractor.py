import requests
import json
import os
import os.path
import re
import validators
from termcolor import colored
from bs4 import BeautifulSoup

def download(url, name):
    try:
        icon_response = requests.get(url)
        if counter == 0:
            name_ = name
        else:
            name_ = name + f"({counter})"

        file_extension = os.path.splitext(url)[1]

        with open('extracted/' + name_ + file_extension, 'wb') as file:
            file.write(icon_response.content)
        print(f"{colored('  ==>', 'green')} Successful download {url}")
    except Exception as e:
        with open('log.txt', 'a') as f:
            f.write(f"{url} ==> {e}\n")
        print(f"{colored('  ==>', 'light_red')} Failed download error for URL = {url} code = {colored(e, 'light_red', attrs=['underline'])}")

def addPathToUrl():
    icon_path = link_tag['href']
    if not icon_path.startswith('http'):
        if not icon_path.startswith('/'):
            icon_path = '/' + icon_path
            download(url + icon_path, name)
        if icon_path.startswith('//'):
            icon_path = 'http:' + icon_path
            download(icon_path, name)
    elif icon_path.startswith('http'):
        download(icon_path, name)
    else:
        print("FATAL ERROR THIS IS NOT THE URL")

with open('url.json') as f:
    data = json.load(f)

for name, url in data["sites"].items():
    try:
        headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}
        response = requests.get(url, headers=headers)  # HTML content
        print((f"{colored('::', 'light_blue')} Start with {name} {url}"))

        soup = BeautifulSoup(response.content, 'html.parser')
        link_tags = soup.find_all("link", rel= 'icon')
        # print(link_tags)

        icon_types = [['icon'], ['shortcut', 'icon'], ['apple-touch-icon', 'apple-touch-icon-precomposed'], ['fluid-icon', 'mask-icon']]

        # found_match = False
        counter = 0
        for link_tag in link_tags:
            rels = link_tag.get('rel')
            for icon_type in icon_types:
                if rels == icon_type:
                    addPathToUrl()
                    counter += 1
            #         found_match = True
            # if found_match == True:
            #     break

    except Exception as e:
        with open('log.txt', 'a') as f:
            f.write(f"{url} ==> {e}\n")
        print(f"{colored('  ==>', 'light_red')} Error for URL = {url} code = {colored(e, 'light_red', attrs=['underline'])}")