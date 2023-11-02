import time
import requests
from termcolor import colored

urls = ["https://chinaphonearena.com",
        "https://codepen.io",
        "https://tellonym.me",
        "https://twitter.com"]


def write_logs(url, e):
    with open('log.txt', 'a') as f:
        f.write(f"{url} ==> {e}\n")


def check_url(url):
    try:
        try:
            start_time = time.time()
            response = requests.head(url, headers=headers, timeout=4)
            elapsed_time = time.time() - start_time
        except:
            response = requests.head(url)

        status_code = response.status_code
        return status_code < 400
    except requests.exceptions.RequestException as e:
        write_logs(url, e)
        print(
            f"{colored('  ==>', 'light_red')} CheckUrl error = {url} code = {colored(e, 'light_red', attrs=['underline'])}")
        return False


for url in urls:
    check_url(url)
