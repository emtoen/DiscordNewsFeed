#Import necessary libraries
from flask import Flask, request
import requests
import json

#Create Flask app
app = Flask(__name__)

#Store API key and URLs
api_key = 'your news api key'
url = 'https://newsapi.org/v2/everything'
#choose any new source you want, make sure to check its availabe. 
# I am using thehackernews.com as an example
params = {'domains': 'thehackernews.com', 'apiKey': api_key}

webhook_url = 'your discord webhook url'


#Route to check for new articles
@app.route('/')
def get_articles():
  #Make API request
  response = requests.get(url, params=params)
  #Parse response
  data = response.json() 
  articles = data['articles']
  

  #Get newest article
  newest_article = articles[0]
  
  if newest_article not in articles_cache:
    message = f"{newest_article['title']}\n{newest_article['description']}\n{newest_article['url']}"
    payload = {'content': message}
    # Send to Discord
    requests.post(webhook_url, json=payload)
    # Add to cache
    articles_cache.append(newest_article)
    
  return "Checked for new articles"

if __name__ == '__main__':
#Cache to store already sent articles
  articles_cache = []
 #run app 
  app.run()
