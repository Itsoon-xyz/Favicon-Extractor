import time
import requests
import urllib.request
from termcolor import colored
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

urls = ["https://chinaphonearena.com",
        "https://codepen.io",
        "https://tellonym.me",
        "https://twitter.com"]


def write_logs(url, e):
    with open('log.txt', 'a') as f:
        f.write(f"{url} ==> {e}\n")


headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
}


# def check_url(url):
#     try:
#         response = requests.head(url, headers=headers)
#         # response = requests.get(url, headers=headers)
#         # try:
#         #     start_time = time.time()
#         #     response = requests.head(url, headers=headers, timeout=4)
#         #     elapsed_time = time.time() - start_time
#         # except:
#         #     response = requests.head(url)

#         status_code = response.status_code
#         print(response)
#         if status_code < 400:
#             return True
#         elif status_code == 403:
#             driver.get(url)
#             time.sleep(5)
#             if "404" not in driver.title:
#     except Exception as e:
#         write_logs(url, e)
#         print(f"{colored('  ==>', 'light_red')} CheckUrl error = {url} code = {colored(e, 'light_red', attrs=['underline'])}")
#         return False


for url in urls:
    print(url, check_url(url))

driver.quit()
