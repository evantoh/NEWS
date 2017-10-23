from flask import render_template,request,redirect,url_for
from . import main
from flask import render_template
from ..requests import get_source,get_article

@main.route('/')

def index():
	news=get_article('the-next-web')
	print(news)
	title='Welcome to the best News Update website'
	sources=get_source("technology")
	return render_template('index.html',title=title,source = sources,news=news)


@main.route('/source/<id>')
def news(id):
	news=get_article(id)
	new_id = id
	title=f'{new_id}'
	print(news)
	return render_template('source.html',title=title,news=news, new_id=new_id)