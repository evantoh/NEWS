from app import app
from flask import render_template
from .request import get_source,get_article

@app.route('/')

def index():

	title='Welcome to the best News Update website'
	sources=get_source("technology")
	
	return render_template('index.html',title=title,source = sources)


@app.route('/news/<string:id>')

	
def news(id):
	news=get_article(id)
	title=f'{news.description}'
	print(title)
	return render_template('news.html','index.html',title=title,news=news)