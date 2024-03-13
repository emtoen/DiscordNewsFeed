# Alternative option to send news from api using crontab.


#Import necessary libraries
import requests
import time


#Store API key and URLs
api_key = 'xxxxxxxxxxxxxxxx'
url = 'https://newsapi.org/v2/everything'
params = {
  'domains': 'thehackernews.com',
  'apiKey': api_key
}

#configure your discord webhook
webhook_url = 'https://discord.com/api/webhooks/xxxxxxxxxx/xxxxxxxxxx'
response = requests.get(url, params=params)
#Make API request
data = response.json()
articles = data['articles']

#set the number of articles to be sent in a day
for i in range(7):
  article = articles[i]
  #parsing the output to only article title, description and url
  message = f"{article['title']}\n{article['description']}\n{article['url']}"
  payload = {
        'content': message
    }
  response = requests.post(webhook_url, json=payload)
  if response.status_code == 204:
    print('Message sent!')
   # Sleep for 5 minutes (optional)
  time.sleep(900)
