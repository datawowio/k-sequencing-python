import mock
import unittest


class ChoiceTest(unittest.TestCase):

    def _getChoiceClass(self):
        from .. import Choice
        return Choice

    @mock.patch('requests.post')
    def test_create(self, api_caller):
        choice_class = self._getChoiceClass()
        
        api_caller.return_value = {
                'code': 200,
                'data': {
                    'allow_empty': False,
                    'answer': [],
                    'categories': ['face,', 'eye'],
                    'credit_charged': 0,
                    'custom_id': None,
                    'data': 'test_image.test',
                    'id': '5a5d744dcaac76418bb72ec0',
                    'instruction': 'face',
                    'multiple': False,
                    'postback_url': 'localhost/callbacks',
                    'processed_at': None,
                    'project_id': 82,
                    'status': 'unprocess'
                    },
                'error_code': None,
                'message': 'success',
                'meta': {'code': 200, 'message': 'success'}
                }

        params = {'categories': 'face, eye',
                  'instruction': 'face',
                  'data': 'test_image.test'}
        response = choice_class('test_auth').create(params)
        self.assertIsNotNone(response)

