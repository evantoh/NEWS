import unittest
from .models import news
News = news.News

class NewTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):

    	self.new_news=News(self,)