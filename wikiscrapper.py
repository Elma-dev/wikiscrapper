from dotenv import load_dotenv
from datasets import Dataset
import os
import mwparserfromhell
# set before importing pywikibot
os.environ["PYWIKIBOT_NO_USER_CONFIG"]="1"
import pywikibot

load_dotenv()
print("[INFO] Loading environment variables ....")
HF_DS_REPO=os.getenv("HF_DS_REPO")
HF_WRITE_TOKEN=os.getenv("HF_WRITE_TOKEN")
print("[INFO] Done!")

if __name__=="__main__":
   print("[INFO] Starting scrapping process ....")
   site=pywikibot.Site("ary","wikipedia")          # Site language and website (eg. ary.wikipedia.com)
   articles={"title":[],"content":[]}
   i=0
   for page in site.allpages():
     page=pywikibot.Page(site,page.title())
     header=page.extract()
     if header:
       post = mwparserfromhell.parse(page.text)
       post= post.strip_code()
       articles["content"].append(post)
       articles["title"].append(page.title())
       i+=1
       if i%1000==0:                     # Push each 1000 articles to the hub / Logs
        print(f"[INFO] Article {i} push to the hub ....")
        ds=Dataset.from_dict(articles)
        ds.push_to_hub(HF_DS_REPO,token=HF_WRITE_TOKEN,private=True)
        print("[INFO] Done!")