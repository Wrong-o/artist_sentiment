import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os
import nltk
from collections import Counter
import re
import numpy as np
from PIL import Image
import subprocess
from nltk.corpus import stopwords
import tempfile
nltk.download('stopwords')
#The artist name will be used to identify dir, mask and json
artist = input("artist: ")

#File path for json
file_path = os.path.join(artist, f'{artist}.json')

#Load text from json
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)
    # Combine all cleaned_text entries if data is a list
    if isinstance(data, list):
        text = ' '.join(entry['cleaned_text'] for entry in data)
    else:
        text = data['cleaned_text']

text = re.sub(r"([^\w\s]')", r' \1 ', text)
text = re.sub(r'[^\w\s]', '', text)

#Lowercase, tokenize
tokens = nltk.word_tokenize(text)
filtered_token = [token for token in tokens if len(token) > 1]
lowercase_tokens = [token.lower() for token in filtered_token]

#Stop words
swedish_stop_words = set(stopwords.words('swedish'))
filtered_tokens = [token for token in lowercase_tokens if token not in swedish_stop_words]

word_counts = Counter(filtered_tokens)
most_common_words = word_counts.most_common(15)
sorted_most_common_words = sorted(most_common_words, key=lambda x: x[0])

#Print common words
print("15 most common words (sorted alphabetically):")
for word, count in sorted_most_common_words:
    print(f"{word}: {count}")

processed_text = ' '.join(filtered_tokens)

mask_path = os.path.join(artist, f'{artist}_mask.png')
#Is there a mask?
if os.path.exists(mask_path):
    # Load the mask image
    mask = np.array(Image.open(mask_path))
else:
    # No mask found, set mask to None
    mask = None



#Max words
max_words = 150
wordcloud = WordCloud(width=3840, height=2160, background_color='black', max_words=max_words, mask=mask, contour_width=3, contour_color='black', collocations=False).generate(processed_text)
with open ('processed_text', 'w') as json_file:
    json.dump({'processed_text': processed_text}, json_file)

#Display cloud
plt.figure(figsize=(10, 10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Hide the axis
plt.show()
wordcloud_path = os.path.join(artist, f'{artist}_wordcloud.png')
wordcloud.to_file(wordcloud_path)
