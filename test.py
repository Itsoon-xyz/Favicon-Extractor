import requests
import os
import os.path
import re
import json
from termcolor import colored
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"
}




def write_logs(url, e):
    with open('log.txt', 'a') as f:
            f.write(f"{url} ==> {e}\n")

# def check_url(url):
#     try:
#         response = requests.head(url, headers=headers)
#         status_code = response.status_code
#         if status_code >= 400:
#             print(response)
#         return status_code < 400
#     except requests.exceptions.RequestException as e:
#         write_logs(url, e)
#         print(f"{colored('  ==>', 'light_red')} CheckUrl error = {url} code = {colored(e, 'light_red', attrs=['underline'])}")
#         return False

# with open('url.json') as f:
#     data = json.load(f)

# for name, url in data["sites"].items():
#     if check_url(url):
#         print(url, colored("True", 'green'))
#     else:
#         print(url, colored("False", 'red'))



def download(url, name):
    print(colored('download', "magenta"))
    try:
        print("iconrepup")
        print(url)
        icon_response = requests.get(url, headers=headers)
        print("iconrep")
        if counter == 0:
            name_ = name
        else:
            name_ = name + f"({counter})"
        print("fileextension")

        file_extension = os.path.splitext(url)[1]
        if "?" in file_extension:
            file_extension = re.search(r'\.(.*?)\?', url)
        with open('extracted/' + name_ + file_extension, 'wb') as file:
            file.write(icon_response.content)
        print(f"{colored('  ==>', 'green')} Successful download {url}")
    except Exception as e:
        write_logs("Failed download error for URL for " + url, e)
        print(f"{colored('  ==>', 'light_red')} Failed download error for URL = {url} code = {colored(e, 'light_red', attrs=['underline'])}")



url = ["https://www.adobe.com/homepage/img/favicons/favicon.ico", "https://www.adobe.com/homepage/img/favicons/favicon-180.png"]
counter = 0
for _url in url:
    download(_url, "adobe")