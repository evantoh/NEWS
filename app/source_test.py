import unittest
from models.sources import Sources
#TESTING Sources 

class NewsTest(unittest.TestCase):
	def setUp(self):
		self.new_sources=Sources("abc-news-au","ABC News (AU)","Australia's most trusted source of local, national and world news. Comprehensive, independent, in-depth analysis, the latest business, sport, weather and more.","http://www.abc.net.au/news","general")

	def test_sources_test(self):
		self.assertTrue(isinstance(self.new_sources,Sources))

if __name__ == '__main__':
	unittest.main(verbosity=2)