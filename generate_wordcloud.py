import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os
import nltk
from collections import Counter
import re
import numpy as np
from PIL import Image
from nltk.corpus import stopwords

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

text = re.sub(r'([^\w\s])', r' \1 ', text)
text = re.sub(r'[^\w\s]', '', text)

#Lowercase, tokenize
tokens = nltk.word_tokenize(text)
lowercase_tokens = [token.lower() for token in tokens]

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

#Load mask in same dir as json
mask_path = os.path.join(artist, f'{artist}_mask.png')
mask = np.array(Image.open(mask_path))

#Max words
max_words = 150
wordcloud = WordCloud(width=3840, height=2160, background_color='black', max_words=max_words, mask=mask, contour_width=3, contour_color='black', collocations=False).generate(processed_text)

#Display cloud
plt.figure(figsize=(10, 10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Hide the axis
plt.show()
