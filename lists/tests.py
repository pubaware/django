from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page

# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        '''
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        '''

        '''
        expected_html = render_to_string('home.html')
        self.assertEqual(html, expected_html)
        '''
        '''
        self.assertTrue(html.startswith('<html>'))

        self.assertIn('<title>To-Do lists</title>', html)
        #print(html.strip()+'\\')
        self.assertTrue(html.strip().endswith('</html>'))
        '''
        self.assertTemplateUsed(response, 'home.html')
        
