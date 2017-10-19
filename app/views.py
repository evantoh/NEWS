from app import app
from flask import render_template

@app.route('/')

def index():
	title='Yeah am working push the boundary' 
	return render_template('index.html',title=title)


@app.route('/news/<int:news_id>')

def news(news_id):

	return render_template('news.html',news_id=news_id)