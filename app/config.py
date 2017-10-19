class Config:
	NEWS_SOURCE_API_BASE_URL='https://newsapi.org/v1/articles?source=the-next-web&{}=latest&apiKey={}'
	NEWS_ARTICLE_API_BASE_URL='https://newsapi.org/v1/articles?source=techcrunch&apiKey={}'

class ProdConfig(Config):
	pass

class DevConfig(Config):

	DEBUG=True