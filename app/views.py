from app import app
from flask import render_template
from .request import get_resource

@app.route('/')
def index():
	title='Welcome to the best News website'
	sources=get_resource() 
	# kk=print(sources)
	return render_template('index.html',title=title,sources=sources)



@app.route('/news/<int:news_id>')

def news(news_id):

	return render_template('news.html',news_id=news_id)