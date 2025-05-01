import unittest
from toolkit.ingestion.ingest import fetch_spl_list, download_spl_html
import responses 
import os 

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

    @responses.activate
    def test_download_spl_html(self):
        set_id  = "test_set_id"
        base_dir = os.getcwd()
        output_dir = os.path.join(base_dir, "tests/ingestion")
        responses.add(**{
                    'method': responses.GET,
                    'url': 'http://example.com/api/123/test_set_id.json',
                    'body': '{"data": "content"}',
                    'status': 200,
                    'content_type': 'application/json',
                    'adding_headers': {'X-Foo': 'Bar'}
                }) 
        
        download_spl_html(
            set_id = set_id,
            output_dir = output_dir, 
            download_url = 'http://example.com/api/123/'
            )
        
        self.assertEqual(os.path.exists(output_dir), True)