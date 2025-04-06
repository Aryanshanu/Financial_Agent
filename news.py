import requests
from transformers import pipeline

# Initialize sentiment analysis model
sentiment_model = pipeline("sentiment-analysis")

def fetch_news(api_key):
    url = f"https://newsapi.org/v2/everything?q=finance&apiKey={api_key}"
    response = requests.get(url)
    news_data = response.json()
    return news_data['articles']

def analyze_sentiment(articles):
    sentiments = []
    for article in articles:
        sentiment = sentiment_model(article['title'])[0]
        sentiments.append({
            "title": article['title'],
            "description": article['description'],
            "sentiment": sentiment['label'],
            "score": sentiment['score']
        })
    return sentiments
