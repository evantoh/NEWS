from app import app
import urllib.request,json
from models.news import News


#importing api_key
api_key=app.config['NEWS_API_KEY']

#importing article and source urls
article_url=app.config['NEWS_ARTICLE_API_BASE_URL']
source_url=app.config['NEWS_SOURCE_API_BASE_URL']