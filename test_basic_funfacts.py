import json
from os import listdir
from os.path import isfile, join
import unittest

from endpoints import APP

FUNFACTS_DIRECTORY_NAME = 'funfacts'

class TestBasicFunfact(unittest.TestCase):
    def test_basic_response(self):
        with APP.test_client() as c:
            rv = c.get('/funfacts/owlie')
            json_data = rv.get_json()
            self.assertEqual(json_data, json.loads('{"name": "Owlie", "uid": "owlie", "title": "COMPANY LOGO", "team": "ALL", "fun_fact": "Everyone tries to draw me."}'))

    # @unittest.skip
    def test_all_funfact_files_formatted_correctly(self):
        ''' This test loops through all files in the 'funfacts' directory and pulls the filename, and then uses it to make an http get request to /funfacts/{username}
        If the funfacts file does not have propper formatting, it will return a 500
        '''
        with APP.test_client() as c:
            funfact_usernames = [f for f in listdir(FUNFACTS_DIRECTORY_NAME) if not f.endswith('.md')]
            for username in funfact_usernames:
                rv = c.get(f'/funfacts/{username}')
                self.assertEqual(rv.status_code, 200, f'Endpoint /funfacts/{username} did not return a 200 response')
                json_data = rv.get_json()
                self.assertEqual(json_data['uid'], f'{username}')

if __name__ == '__main__':
    unittest.main(verbosity=2)