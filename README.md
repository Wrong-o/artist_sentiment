# Artist Sentiment

This directory is a combined webscraper, tokenization and wordcloud generator for artists on the website "genius.com".
A fun conversation starter for nerds like myself.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Contact](#contact)

## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the repository:**

   Open your terminal and run the following command to clone the repository from GitHub:

   ```bash
   git clone https://github.com/Wrong-o/artist_sentiment.git
   ```
2.
   Change your directory to the project folder:

   ```bash
   cd ./artist_sentiment
   ```
3.
   Create a virtual enviroment to manage dependencies. Choose script depending on you os:

      ### For macOS or Linux:

      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```
      ### For Windows:

      ```bash
      python -m venv venv
      .\venv\Scripts\activate
      ```

4.
   Install dependencies and download NLTK stopwords:
      ```bash
      pip install -r requirements.txt
      import nltk
      nltk.download
      ```
   
## Usage
Once setup, you will have some examples folders. New artists will appear in the same structure.
   First thing you need to do is run the url_scraper.py:
      ```bash
      python3 url_scraper.py
      ```
The script will ask for an input, write the artist name as seen on genius.com but substitute spaces with "-" 

A song_list.json will be created in a subdirectory named /artist-name. This file contains the url for all songs found on genius.com

# Download and process the text
 Download and process all the text by running
          ```bash
    python3 text_process.py
      ```
 Input the same artist name as in the previous step. 
 A new file called "artist-name" will appear in /artist-name, containing all the text from the urls in song_list.json

 # Generate wordcloud
 To generate wordcloud, run: 
           ```bash
    python3 generate_wordclound.py
      ```

**NOTE** Masks are not automaticly generated, they will have to be done manually. The ones used in the examples are in 4k resolution. The program defaults to "None" if no mask if found in the /artist-name directory with the name "artist-name_mask.png"

##License
      Feel free to use and modify this code however you want. 
      Please give credit and link back to this project if used.

##Contact:
      Contact me on 
