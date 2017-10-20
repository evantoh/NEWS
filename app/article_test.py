import unittest
from models.sources import Articles



class NewsTest(unittest.TestCase):
	def setUp(self):
		self.new_article=Articles("Taylor Hatmaker","Palmer Luckey’s new defense company Anduril looks interested in AR and VR on the battlefield","Palmer Luckey's new defense startup Anduril has aspirations well beyond a high-tech border wall. According to new information on the company's website and its..","https://techcrunch.com/2017/10/19/anduril-trae-stephens-battlefield-vr-ar/","https://tctechcrunch2011.files.wordpress.com/2017/10/22869497253_a453df1541_k.jpg","2017-10-19T22:37:44Z")

	def test_instance(self):
		self.assertTrue(isinstance(self.new_article,Articles))

if __name__ == '__main__':
	unittest.main(verbosity=2)
