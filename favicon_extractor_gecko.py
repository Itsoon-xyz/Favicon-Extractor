import json
import requests
import os
import os.path
import re
import time
from termcolor import colored
from selenium import webdriver
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
    # print(colored('checkUrl', "magenta"))
    try:
        response = requests.head(url, headers=headers)
        status_code = response.status_code
        return status_code < 400
    except requests.exceptions.RequestException as e:
        write_logs(url, e)
        print(f"{colored('  ==>', 'light_red')} CheckUrl error = {url} code = {colored(e, 'light_red', attrs=['underline'])}")
        return False
        

def download(url, name):
    # print(colored('download', "magenta"))
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

        file_extension = os.path.splitext(url)[1]
        if "?" in file_extension:
            file_extension = re.search(r'\.(.*?)\?', url)
        with open('extracted/' + name_ + file_extension, 'wb') as file:
            file.write(icon_response.content)
        print(f"{colored('  ==>', 'green')} Successful download {url}")
    except Exception as e:
        write_logs("Failed download error for URL for " + url, e)
        print(f"{colored('  ==>', 'light_red')} Failed download error for URL = {url} code = {colored(e, 'light_red', attrs=['underline'])}")

with open('url.json') as f:
    data = json.load(f)

for name, url in data["sites"].items():
    try:
        print(f"{colored('::', 'light_blue')} Start with {url}")

        if check_url(url):

            def getUrl(url):
                # print(colored('getUrl', "magenta"))
                driver.get(url)
                try:
                    favicon = driver.find_element(By.CSS_SELECTOR, 'link[rel="icon"]')
                    if favicon.get_attribute('href') in ['data:,', '']:

                        favicon = WebDriverWait(driver, 30).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, 'link[rel="icon"]'))
                        )

                        WebDriverWait(driver, 30).until(
                            lambda driver: favicon.get_attribute('href') not in ['data:,', '']
                        )
                except Exception as e:
                    pass

                tags = driver.find_elements(By.CSS_SELECTOR, "link[rel*='icon']")
                return tags
            
            link_tags = getUrl(url)
            # print(colored('first linktagsdef', "magenta"))

            # print([tag.get_attribute('outerHTML') for tag in link_tags]) # to see the tags
            

            if link_tags == []:
                # print(colored('secondlinktagsdef', "magenta"))
                print(colored("  ==> retry with search url", "red"))
                if check_url(url + "/favicon.ico"):
                    counter = 0
                    download(url + "/favicon.ico", name)
                    continue
                else:
                    write_logs(url, "the site does not contain a favicon, or there is a problem in the script")
                    print(f"{colored('  ==>', 'light_red')} Error for URL = {url} code = {colored('the site does not contain a favicon, or there is a problem in the script', 'light_red', attrs=['underline'])}")

            icon_types = [['icon'], ['shortcut', 'icon'], ['apple-touch-icon', 'apple-touch-icon-precomposed'], ['fluid-icon', 'mask-icon']]
            counter = 0
            for link_tag in link_tags:
                # print(colored('firstloop', "magenta"))
                rels = link_tag.get_attribute('rel').split()
                for icon_type in icon_types:
                    # print(colored('secondloop', "magenta"))
                    if all(rel in rels for rel in icon_type):
                        icon_url = link_tag.get_attribute('href')
                        download(icon_url, name)
                        counter += 1

        else:
            write_logs(url, "invalid url")
            print(f"{colored('  ==>', 'light_red')} Error for URL = {url} code = {colored('invalid url', 'light_red', attrs=['underline'])}")


    except Exception as e:
        write_logs(url, e)
        print(f"{colored('  ==>', 'light_red')} Error for URL = {url} code = {colored(e, 'light_red', attrs=['underline'])}")

print(colored('Successful download', 'green'), ' look at log.txt to see errors')

driver.quit()
