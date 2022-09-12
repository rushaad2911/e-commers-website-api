from django.test import TestCase

class HoamePageTest(TestCase):
    
    def test_home_page(self):
        
        res = self.client.get('/')
        self.assertEqual(res.status_code,200)
        
    
    