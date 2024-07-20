import re
import requests
from bs4 import BeautifulSoup
import json

# List of URLs to fetch
urls = [
    "https://genius.com/Hov1-hon-dansar-vidare-i-livet-lyrics",
    "https://genius.com/Hov1-pari-lyrics",
    "https://genius.com/Hov1-gamora-lyrics"

    # Add more URLs here
]

def fetch_text_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find all elements with the specified class
        content_divs = soup.find_all('div', class_='Lyrics__Container-sc-1ynbvzw-1 kUgSbL')
        if content_divs:
            # Concatenate all the text from the found elements
            text = ' '.join([div.get_text(separator=' ') for div in content_divs])
            return text
        else:
            print(f"No content found at {url}")
            return ""
    else:
        print(f"Failed to fetch {url}")
        return ""

def clean_text(text):
    text = re.sub(r'\[.*?\]', '', text)  # Remove brackets
    text = text.replace('"', ' ')        # Replace double quotes with space
    text = text.replace("'", ' ')        # Replace single quotes with space
    text = text.replace('<br>', ' ')     # Replace <br> tags with space
    text = re.sub(r'\s+', ' ', text)     # Replace multiple spaces with a single space
    text = re.sub(r'(\w)([A-Z])', r'\1 \2', text)  # Add space between words stuck together
    return text.strip()                  # Remove leading and trailing whitespace

cleaned_texts = []

for url in urls:
    text = fetch_text_from_url(url)
    if text:
        cleaned_text = clean_text(text)
        cleaned_texts.append({'url': url, 'cleaned_text': cleaned_text})

# Save cleaned texts to a JSON file
with open('cleaned_texts.json', 'w', encoding='utf-8') as f:
    json.dump(cleaned_texts, f, ensure_ascii=False, indent=4)

print(f"Cleaned texts saved to cleaned_texts.json")
