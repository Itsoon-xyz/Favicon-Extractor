import requests
import json
from termcolor import colored
from bs4 import BeautifulSoup

def download(url, name):
    try:
        icon_response = requests.get(url)
        # print(icon_response)
        with open('extracted/' + name, 'wb') as file:
            file.write(icon_response.content)
        print(f"{colored('==>', 'green')} Successful download {url}")
    except Exception as e:
        with open('log.txt', 'a') as f:
            f.write(f"{url} ==> {e}\n")
        print(f"Error for URL = {url} code = {colored(e, 'light_red', attrs=['underline'])}")

def addPathToUrl():
    icon_path = link_tag['href']
    if not icon_path.startswith('http'):
        if not icon_path.startswith('/'):
            icon_path = '/' + icon_path
        if icon_path.startswith('//'):
            icon_path = 'http' + icon_path
                        
        print('if url + icon_path, name')
        download(url + icon_path, name)
    elif icon_path.startswith('http'):
        print('elif icon_path, name')
        download(icon_path, name)
    else:
        print("FATAL ERROR THIS IS NOT THE URL")

with open('url.json') as f:
    data = json.load(f)

for name, url in data["sites"].items():
    try:
        response = requests.get(url)  # HTML content
        print((f"{colored('::', 'light_blue')} Start with {name} {url}"))

        soup = BeautifulSoup(response.content, 'html.parser')
        link_tags = soup.find_all("link", rel=True)
        print(link_tags)

        icon_types = [['icon'], ['shortcut icon'], ['apple-touch-icon', 'apple-touch-icon-precomposed'], ['fluid-icon', 'mask-icon']]

        # for link_tag in link_tags:
            # verify = link_tag.get('icon')
            # print(link_tag)
            # found_match = False
            # for icon_type in icon_types:
            #     if verify == icon_type:
            #         print(verify.get('href'))
            #         addPathToUrl()
            #         found_match = True
            # if found_match:
            #     break

    except Exception as e:
        with open('log.txt', 'a') as f:
            f.write(f"{url} ==> {e}\n")
        print(f"Error for URL = {url} code = {colored(e, 'light_red', attrs=['underline'])}")