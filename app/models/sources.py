class Articles:

	def __init__(self,author,title,description,article,image,publishedAt):

		self.author=author
		self.title=title
		self.description=description
		self.article=article
		self.image= "https://cdn0.tnwcdn.com/wp-content/blogs.dir/1/files/2017/10/"+image
		self.publishedAt=publishedAt


class Sources:

	def __init__(self,id,name,description,source,category):
		self.id=id
		self.name=name
		self.description=description
		self.source=source
		self.category=category

