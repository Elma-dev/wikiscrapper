<div align="center">
  <img src=img/logo.png alt="Wikipedia Scraper Logo" />

  # Wikipedia Scraper ...
  
  A tool to scrape and process Wikipedia articles for dataset creation
</div>

## 📝 Description

This project is a Wikipedia scraper specifically designed to collect articles from the Moroccan Arabic Wikipedia (ary.wikipedia.org). It processes the articles and creates a dataset that can be pushed to the Hugging Face Hub.

## 🚀 Features

- Scrapes articles from Wikipedia
- Removes Wiki markup using `mwparserfromhell`
- Automatically pushes data to Hugging Face Hub
- Processes articles in batches of 1000
- Maintains article titles and content

## 🛠️ Installation
To install and use the Wikipedia Scraper, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/wikipedia-scraper.git
   cd wikipedia-scraper
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory of the project and add your Hugging Face repository and token:
   ```env
   HF_DS_REPO="your_huggingface_repo"
   HF_WRITE_TOKEN="your_huggingface_token"
   ```

5. **Run the scraper:**
   ```bash
   python wikiscrapper.py
   ```

This will start the scraping process and push the collected articles to your Hugging Face repository in batches of 1000 articles.

