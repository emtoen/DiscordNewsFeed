# DiscordNewsFeed
This project uses Flask as a web framework to build a bot that periodically checks for new news articles from a given news source and sends them to a Discord channel. It allows users to stay updated with the latest news headlines without manually checking news sites.

Technology Stack:

    Python
    Flask - To build the web server that runs continuously
    NewsAPI - A free API used to fetch latest news articles from supported sources
    Discord.py - To interface with the Discord API and send messages

Working:

    The Flask server runs continuously on the background
    It checks the NewsAPI endpoint on a configured interval
    The API is queried for latest articles from the selected news source
    New articles that have not been previously sent are identified
    The article title, description and URL is formatted into a message payload
    The payload is sent to the target Discord channel using the webhook URL
    The sent articles are cached to avoid duplication on subsequent polls

Key Features:
    Configurable news source and Discord channel details
    Sends only new articles not seen before
    Lightweight and runs as a background service
    Easy to use and maintain codebase
    
An alternative to this is by using a cronjob which runs at a particular time of the day and push all the top articles to the server.
