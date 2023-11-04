import time
import json
import requests
from termcolor import colored
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

# urls = ["https://chinaphonearena.com",
#         "https://codepen.io",
#         "https://tellonym.me",
#         "https://twitter.com"]


def write_logs(url, e):
    with open('log.txt', 'a') as f:
        f.write(f"{url} ==> {e}\n")


headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
}


def check_url(url):
    try:
        response = requests.head(url, headers=headers)
        print(response)
        status_code = response.status_code
        if status_code <= 400:
            return True
        elif status_code == 403:
            driver.get(url)
            if "404" not in driver.title:
                return True
        else:
            response = requests.head(url)
            if response.status_code <= 400:
                return True

    except Exception as e:
        write_logs(url, e)
        return False


with open('url.json') as f:
    data = json.load(f)

for name, url in data["sites"].items():
    # print(url, check_url(url))
    link = check_url(url)
    if link == True:
        print(url, colored(True, "green"))
    elif link == False:
        print(url, colored(False, "red"))

driver.quit()
