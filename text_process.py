import re
import requests
from bs4 import BeautifulSoup
import json
import os

artist = input("artist: ")
# List of URLs to fetch

with open(f'./{artist}/song_list.json', 'r') as file:
    urls = json.load(file)

def fetch_text_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        content_divs = soup.find_all('div', class_='Lyrics__Container-sc-1ynbvzw-1 kUgSbL')
        if content_divs:
            text = ' '.join([div.get_text(separator=' ') for div in content_divs])
            return text
        else:
            print(f"No content found at {url}")
            return ""
    else:
        print(f"Failed to fetch {url}")
        return ""



def clean_text(text):
    text = re.sub(r'\[.*?\]', '', text)
    text = text.replace('"', ' ')
    text = text.replace('<br>', ' ')
    text = re.sub(r'\s+', ' ', text)
    return text.strip()    

cleaned_texts = []

for url in urls:
    text = fetch_text_from_url(url)
    print(url)
    if text:
        cleaned_text = clean_text(text)
        cleaned_texts.append({'url': url, 'cleaned_text': cleaned_text})
        
os.makedirs(f"./{artist}", exist_ok=True)

with open(f'./{artist}/{artist}.json', 'w', encoding='utf-8') as f:
    json.dump(cleaned_texts, f, ensure_ascii=False, indent=4)

print(f"Cleaned texts saved to folder")
