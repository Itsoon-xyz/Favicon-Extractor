import re
import os.path
from urllib.parse import urlparse

urls = ["https://www.nike.com/favicon.ico?v=1",
        "https://ei.phncdn.com/www-static/favicon.ico?cache=2023103101",
        "https://ei.rdtcdn.com/www-static/cdn_files/redtube/icons/favicon.ico?v=b712984e78f36d2e122926925b9dc3b1811b066d",
        "https://static.rocketreach.co/images/favicons/favicon-192x192.png?v=2020120",
        "https://d3nn82uaxijpm6.cloudfront.net/favicon-16x16.png?v=dLlWydWlG8",
        "https://s1.wp.com/i/favicon.ico?v=1447321881"]

extensions = []

for url in urls:
    # file_extension = os.path.splitext(url)[1]
    # print(file_extension)
    parsed_url = urlparse(url)
    path = parsed_url.path
    file_extension = os.path.splitext(path)[1]
    print(file_extension)