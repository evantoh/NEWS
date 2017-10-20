from app import app
import urllib.request,json
from models.sources import Sources,Articles


#importing api_key
api_key=app.config['NEWS_API_KEY']

#importing article and source urls
article_url=app.config['NEWS_ARTICLE_API_BASE_URL']
source_url=app.config['NEWS_SOURCE_API_BASE_URL']



#Stripping the source url to get information we need 

def get_url():
	with urllib.request.urlopen(source_url) as sourceUrl:
		get_source_data=sourceUrl.read()
		get_source_response=json.loads(get_source_data)


		source_results=None

		if get_source_response['result']:
			source_result_list=get_source_response['result']
			source_results=process_source_result(source_result_list)

	return source_results
#---------------------------------------------------------


##Getting specific items using the function process_source_result()
def process_source_result(source_list):

	source_results=[]

	for source_item in source_list:
		id=source_item.get('id')
		name=source_item.get('name')
		description=source_item.get('description')
		source=source_item.get('source')
		category=source_item.get('category')

		if source:
			source_object=Sources(id,name,description,source,category):
			 source_results.append(source_object):

	return source_results
#-------------------------------------------------------------
					#END OF SOURCE_URL STRIPING 
#-------------------------------------------------------------


#rem to work here


# def get_news(sortby):

# 	get_articles_url=article_url.format()

# 	with urllib.request.urlopen(get_article_url) as url:
# 		get_article_data=url.read()
# 		get_article_response=json.loads(get_article_data)

# 		article_results=None

# 		if get_artcle_response['results']:
# 			article_results_list=get_article_response['results']
# 			article_results=process_results(article_results_list)


# 	return source_results


# 	def process_results(source_list):


# 		source_output=[]

# 		for source_item in source_list:


