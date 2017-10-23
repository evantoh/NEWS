import urllib.request,json
from .models import Articles,Sources 

#getting the api
api_key=None

#getting source and article url
article_url=None
source_url=None

def configure_request(app):

	global api_key,article_url,source_url
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

def get_article(source):
	get_article_url=article_url.format(source,api_key)
	print(get_article_url)
	
	with urllib.request.urlopen(get_article_url) as url:
		article_data=url.read()
		get_article_response=json.loads(article_data)
		
		article_results=None
		
		if get_article_response['articles']:
				article_results_list =get_article_response['articles']
				article_results=process_article(article_results_list)
# print(article_results)
	return article_results
	

		

def process_article(article_list):

	article_results=[]

	for article_item in article_list:
		author=article_item.get("author")
		title=article_item.get("title")
		description=article_item.get('description')
		url=article_item.get('url')
		image=article_item.get("urlToImage")
		publishedAt=article_item.get("publishedAt")


		article_object=Articles(author,title,description,url,image,publishedAt)
		article_results.append(article_object)

	print(article_object)	
	return article_results
	


##---------------------------------------------------------------------
						#THE END
##---------------------------------------------------------------------
