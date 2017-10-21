class Config:
	NEWS_SOURCE_API_BASE_URL='https://newsapi.org/v1/sources?{}'
	NEWS_ARTICLE_API_BASE_URL='https://newsapi.org/v1/articles?source={}&sortBy={}&apiKey={}'

class ProdConfig(Config):
	pass

class DevConfig(Config):

	DEBUG=True


