import unittest
from toolkit.ingestion.ingest import fetch_spl_list, download_spl_html
import responses 

class TestIngestion(unittest.TestCase):
    
    @responses.activate
    def test_fetch_spl_list(self):
        responses.add(**{
            'method': responses.GET,
            'url': 'http://example.com/api/123',
            'body': '{"data": "content"}',
            'status': 200,
            'content_type': 'application/json',
            'adding_headers': {'X-Foo': 'Bar'}
        })  

        list = fetch_spl_list(
            base_url='http://example.com/api/123',
            limit=1
            )
        
        self.assertEqual("content", list)
        
    def test_download_spl_html(self):
        pass