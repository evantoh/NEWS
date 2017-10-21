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


def get_source():

	source_url_info = source_url

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
