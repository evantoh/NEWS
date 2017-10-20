from app import app
import urllib.request,json
from models.news import News


#importing api_key
api_key=app.config['NEWS_API_KEY']

#importing article and source urls
article_url=app.config['NEWS_ARTICLE_API_BASE_URL']
source_url=app.config['NEWS_SOURCE_API_BASE_URL']

#getting categories of News



def get_news(sortby):

	get_sources_url=article_url.format(sortby,)

	with urllib.request.urlopen(get_sources_url) as url:
		get_source_data=url.read()
		get_source_response=json.loads(get_source_data)

		source_results=None

		if get_source_response['results']:
			source_results_list=get_source_response['results']
			source_results=process_results(source_results_list)


	return source_results


	def process_results(source_list):


		source_output=[]

		for source_item in source_list:


