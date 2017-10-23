class Config:
	NEWS_API_KEY="1cb501be99634f37bc9b75d54fa7756c"
	NEWS_SOURCE_API_BASE_URL='https://newsapi.org/v1/sources?{}'
	NEWS_ARTICLE_API_BASE_URL='https://newsapi.org/v1/articles?source={}&apiKey={}'

class ProdConfig(Config):
	pass

class DevConfig(Config):

	DEBUG=True
	
config_options={
'development':DevConfig,
'prodConfig':ProdConfig
}

