import os
import time
import json
import requests
from termcolor import colored
from selenium import webdriver
from urllib.parse import urlparse
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}


def write_logs(url, e):
    with open('log.txt', 'a') as f:
        f.write(f"{url} ==> {e}\n")


def check_url(url):
    try:
        response = requests.head(url, headers=headers)
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
        print(
            f"{colored('  ==>', 'light_red')} CheckUrl error = {url} code = {colored(e, 'light_red', attrs=['underline'])}")
        return False


def download(url, name):
    try:
        try:
            start_time = time.time()
            icon_response = requests.get(url, headers=headers, timeout=4)
            elapsed_time = time.time() - start_time
        except:
            icon_response = requests.get(url)

        if counter == 0:
            name_ = name
        else:
            name_ = name + f"({counter})"

        parsed_url = urlparse(url)
        path = parsed_url.path
        file_extension = os.path.splitext(path)[1]

        with open('extracted/' + name_ + file_extension, 'wb') as file:
            file.write(icon_response.content)
        print(f"{colored('  ==>', 'green')} Successful download {url}")
    except Exception as e:
        write_logs("Failed download error for URL for " + url, e)
        print(
            f"{colored('  ==>', 'light_red')} Failed download error for URL = {url} code = {colored(e, 'light_red', attrs=['underline'])}")


with open('url.json') as f:
    data = json.load(f)

for name, url in data["sites"].items():
    try:
        print(
            f"{colored('::', 'light_blue', attrs=['bold'])} Start with {url}")

        if check_url(url):

            def getUrl(url):
                driver.get(url)
                try:
                    favicon = driver.find_element(
                        By.CSS_SELECTOR, 'link[rel="icon"]')
                    if favicon.get_attribute('href') in ['data:,', '']:

                        favicon = WebDriverWait(driver, 30).until(
                            EC.presence_of_element_located(
                                (By.CSS_SELECTOR, 'link[rel="icon"]'))
                        )

                        WebDriverWait(driver, 30).until(
                            lambda driver: favicon.get_attribute('href') not in [
                                'data:,', '']
                        )
                except Exception as e:
                    pass
                tags = driver.find_elements(
                    By.CSS_SELECTOR, "link[rel*='icon']")
                return tags

            link_tags = getUrl(url)

            if link_tags == []:
                print(colored("  ==> retry with search url", "red"))
                if check_url(url + "/favicon.ico"):
                    counter = 0
                    download(url + "/favicon.ico", name)
                    continue
                else:
                    write_logs(
                        url, "the site does not contain a favicon, or there is a problem in the script")
                    print(
                        f"{colored('  ==>', 'light_red')} Error for URL = {url} code = {colored('the site does not contain a favicon, or there is a problem in the script', 'light_red', attrs=['underline'])}")

            icon_types = [['icon'], ['shortcut', 'icon'], [
                'apple-touch-icon', 'apple-touch-icon-precomposed'], ['fluid-icon', 'mask-icon']]
            counter = 0

            # print([tag.get_attribute('outerHTML')
            #       for tag in link_tags])  # to see the tags

            for link_tag in link_tags:
                rels = link_tag.get_attribute('rel').split()
                rels = [rel.lower() for rel in rels]
                print(rels)  # ['shortcut', 'icon']
                for icon_type in icon_types:
                    if all(rel in rels for rel in icon_type):
                        icon_url = link_tag.get_attribute('href')
                        download(icon_url, name)
                        counter += 1
                        break

        else:
            write_logs(url, "invalid url")
            print(
                f"{colored('  ==>', 'light_red')} Error for URL = {url} code = {colored('invalid url', 'light_red', attrs=['underline'])}")

    except Exception as e:
        write_logs(url, e)
        print(
            f"{colored('  ==>', 'light_red')} Error for URL = {url} code = {colored(e, 'light_red', attrs=['underline'])}")

print(colored('Successful download', 'green'),
      ' look at log.txt to see errors')

driver.quit()
