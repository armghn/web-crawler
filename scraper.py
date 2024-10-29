import csv

import requests
from bs4 import BeautifulSoup


def get_request(url):
    response = requests.get(url)
    return (response.status_code, response.text)


def extract_link(html):
    soup = BeautifulSoup(html, 'lxml')
    links = []

    for link in soup.find_all("a", href=True):
        links.append(link)

    return links


def save_link_to_csv(links):
    with open("url_links.csv", 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['links'])
        for link in links:
            writer.writerow([link])


def scrape_links(page_url):
    html_content = get_request(page_url)
    links = extract_link(html_content[1])
    save_link_to_csv(links)


url = input()
scrape_links(url)
