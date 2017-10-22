from app import app
import urllib.request,json
from app.models.sources import Sources
from app.models.sources import Articles



#importing api_key
api_key=app.config['NEWS_API_KEY']

#importing article and source urls
article_url=app.config['NEWS_ARTICLE_API_BASE_URL']
source_url=app.config['NEWS_SOURCE_API_BASE_URL']


#Stripping the source url to get information we need 


def get_source(language):

	source_url_info = source_url.format(language)

	with urllib.request.urlopen(source_url_info) as url:
		get_source_data=url.read()
		get_source_response=json.loads(get_source_data)


		source_results=None

		if get_source_response['sources']:
			source_result_list=get_source_response['sources']
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

		
		source_object=Sources(id,name,description,source,category)
		source_results.append(source_object)

	return source_results

#-------------------------------------------------------------
					#END OF SOURCE_URL STRIPING 
#-------------------------------------------------------------


##------------------------------------------------------------
					#STRIPPING OF THE ARTICLE URL
##------------------------------------------------------------
def get_article(id):

	get_article_url=article_url.format(id,api_key)

	article_results=None

	with urllib.request.urlopen(get_article_url) as url:
		article_data=url.read()
		get_article_response=json.loads(article_data)
		get_article_processed=process_article(get_article_response)
	
	return get_article_processed
		

		

def process_article(article_list):

	article_item=[]

	for get_article_response in article_list:
		author=get_article_response.get("author")
		title=get_article_response.get("title")
		description=get_article_response.get("description")
		image=get_article_response.get("urlToImage")
		url=get_article_response.get('url')
		publishedAt=get_article_response.get("publishedAt")


		article_results=Articles(author,title,description,image,url,publishedAt)
		article_item.append(article_results)

	return article_item
	print(article_item)
##---------------------------------------------------------------------
						#THE END
##---------------------------------------------------------------------
