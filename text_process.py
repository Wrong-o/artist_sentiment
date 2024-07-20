import re
import requests
from bs4 import BeautifulSoup
import json
import os

artist = input("artist: ")
# List of URLs to fetch
urls = [
    "https://genius.com/Hov1-hon-dansar-vidare-i-livet-lyrics",
    "https://genius.com/Hov1-pari-lyrics",
    "https://genius.com/Hov1-gamora-lyrics",
    "https://genius.com/Hov1-mandy-moore-lyrics",
    "https://genius.com/Hov1-gift-lyrics",
    "https://genius.com/Hov1-barn-av-var-tid-lyrics",
    "https://genius.com/Hov1-karleksbrev-lyrics",
    "https://genius.com/Hov1-hur-kan-du-saga-saker-lyrics",
    "https://genius.com/Hov1-gudarna-pa-vasterbron-lyrics",
    "https://genius.com/Hov1-vindar-pa-mars-lyrics",
    "https://genius.com/Hov1-hov1-lyrics",
    "https://genius.com/Hov1-grazon-lyrics",
    "https://genius.com/Hov1-heartbreak-lyrics",
    "https://genius.com/Hov1-auf-wiedersehen-lyrics",
    "https://genius.com/Hov1-omg-lyrics",
    "https://genius.com/Hov1-hornstullsstrand-lyrics",
    "https://genius.com/Hov1-channel-orange-lyrics",
    "https://genius.com/Hov1-redo-lyrics",
    "https://genius.com/Hov1-do-ung-lyrics",
    "https://genius.com/Hov1-sex-lyrics",
    "https://genius.com/Hov1-forlat-lyrics",
    "https://genius.com/Hov1-mitten-av-september-lyrics",
    "https://genius.com/Hov1-damn-lyrics",
    "https://genius.com/Hov1-nar-jag-ser-dig-lyrics",
    "https://genius.com/Hov1-vill-inte-ha-dig-lyrics",
    "https://genius.com/Hov1-ma-cherie-lyrics",
    "https://genius.com/Hov1-stan-e-mork-lyrics",
    "https://genius.com/Hov1-runaway-bride-lyrics",
    "https://genius.com/Hov1-tokken-lyrics",
    "https://genius.com/Hov1-fodd-i-juni-lyrics",
    "https://genius.com/Hov1-flickorna-i-bastad-lyrics",
    "https://genius.com/Hov1-din-mamma-lyrics",
    "https://genius.com/Hov1-neon-lyrics",
    "https://genius.com/Hov1-hon-dansar-vidare-i-livet-pt2-lyrics",
    "https://genius.com/Hov1-still-lyrics",
    "https://genius.com/Hov1-smokebreak-lyrics",
    "https://genius.com/Hov1-grat-lyrics",
    "https://genius.com/Hov1-langt-bort-harifran-lyrics",
    "https://genius.com/Hov1-hjartslag-lyrics",
    "https://genius.com/Hov1-ska-vi-lyrics",
    "https://genius.com/Hov1-vara-vackra-dar-lyrics",
    "https://genius.com/Hov1-alskling-lyrics",
    "https://genius.com/Hov1-bla-lyrics",
    "https://genius.com/Hov1-exempel-66-lyrics",
    "https://genius.com/Hov1-kara-mamma-lyrics",
    "https://genius.com/Hov1-fri-lyrics",
    "https://genius.com/Hov1-tva-sekunder-pa-loftet-lyrics",
    "https://genius.com/Hov1-i-love-u-so-much-lyrics",
    "https://genius.com/Hov1-rakna-dagar-lyrics",
    "https://genius.com/Hov1-brev-ifran-en-storstad-lyrics",
    "https://genius.com/Hov1-hit-the-club-lyrics",
    "https://genius.com/Hov1-ensammast-i-varlden-lyrics",
    "https://genius.com/Hov1-dig-ormingevisan-lyrics",
    "https://genius.com/Hov1-lilla-b-lyrics",
    "https://genius.com/Hov1-jag-onskar-jag-brydde-mig-mer-lyrics",
    "https://genius.com/Hov1-hur-mycket-pengar-vill-du-ha-lyrics",
    "https://genius.com/Hov1-sex-i-taxin-lyrics",
    "https://genius.com/Hov1-saudade-lyrics",
    "https://genius.com/Hov1-tva-steg-fran-helvetet-lyrics",
    "https://genius.com/Hov1-tjuvheder-lyrics",
    "https://genius.com/Hov1-30-personer-lyrics",
    "https://genius.com/Hov1-458-lyrics",
    "https://genius.com/Hov1-hej-du-lyrics",
    "https://genius.com/Hov1-rosor-av-plast-lyrics",
    "https://genius.com/Hov1-helluva-life-lyrics",
    "https://genius.com/Hov1-banksy-lyrics",
    "https://genius.com/Hov1-alla-vara-minnen-lyrics",
    "https://genius.com/Hov1-burn-bright-die-young-lyrics",
    "https://genius.com/Hov1-rigatoni-lyrics",
    "https://genius.com/Hov1-certified-lyrics",
    "https://genius.com/Hov1-ica-lyrics",
    "https://genius.com/Hov1-en-san-som-mig-lyrics",
    "https://genius.com/Hov1-365-lyrics",
    "https://genius.com/Hov1-sangenjaya-3am-lyrics",
    "https://genius.com/Hov1-vibe-check-lyrics",
    "https://genius.com/Hov1-hundra-lax-karlek-lyrics",
    "https://genius.com/Hov1-30-under-30-lyrics",
    "https://genius.com/Hov1-frankfurt-lyrics",
    "https://genius.com/Hov1-vack-mig-nar-det-ar-over-lyrics",
    "https://genius.com/Hov1-back-to-back-lyrics",
    "https://genius.com/Hov1-sagner-och-myter-lyrics",
    "https://genius.com/Hov1-raindance-lyrics",
    "https://genius.com/Hov1-novemberregn-lyrics",
    "https://genius.com/Hov1-nar-lyktorna-tands-lyrics",
    "https://genius.com/Hov1-forsent-lyrics",
    "https://genius.com/Hov1-nat-i-vattnet-lyrics",
    "https://genius.com/Hov1-free-smoke-lyrics",
    "https://genius.com/Hov1-sprit-och-knark-lyrics",
    "https://genius.com/Hov1-still-recorded-at-spotify-studios-stockholm-lyrics",
    "https://genius.com/Hov1-lilla-gee-lyrics",
    "https://genius.com/Hov1-farval-lyrics",
    "https://genius.com/Hov1-nar-lyktorna-tands-spotify-singles-lyrics",
    "https://genius.com/Hov1-bara-softar-bby-lyrics",
    "https://genius.com/Hov1-tjo-alla-gariz-lyrics",
    "https://genius.com/Hov1-stockholmshistoria-outro-lyrics",
    "https://genius.com/Hov1-jag-kom-lyrics",
    "https://genius.com/Hov1-kysser-mig-med-roda-lappar-lyrics"


    # Add more URLs here
]

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
    text = text.replace("'", ' ')        
    text = text.replace('<br>', ' ')     
    text = re.sub(r'\s+', ' ', text)     
    text = re.sub(r'(\w)([A-Z])', r'\1 \2', text)  
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
