from app import app
from flask import render_template
from .request import get_source

@app.route('/')
def index():
	title='Welcome to the best News website'
	sources=get_source() #removed the s in get_sources and added  
	print(sources)
	return render_template('index.html',title=title,source = sources)


@app.route('/news/<int:news_id>')

def news(news_id):

	return render_template('news.html',news_id=news_id)