# importing the requests library
from requests import Request, Session
import os
from k_sequencing import errors
from k_sequencing import responses

class Connector(object):

    def __init__(self, project_key=None, headers=None):
        """Create new image choices

        Args:
            project_key (str): Key of project has been generated by system
            hearders (obj): Config request header
        Returns:

        Raises:

        """
        if project_key is None:
            if 'Authorization' in os.environ:
                self.project_key = os.environ['Authorization']
            else:
                raise AttributeError('Project key is missing')
        else:
            self.project_key = project_key

        self.headers = self._build_header(headers)
        # self.base_api = 'https://k-sequencing.datawow.io/api/'
        self.base_api = 'http://localhost:3001/api/'

    def _build_header(self, headers=None):

        if headers is None:
            headers = {}

        headers['Authorization'] = self.project_key
        headers['Accept'] = 'application/json'
        headers['Content-Type'] = 'application/x-www-form-urlencoded'

        return headers

    def send(self, method='GET', url=None, data=None, headers=None):

        session = Session()
        if headers is None:
            headers = self.headers

        builder = Request(
            method,
            self.base_api + url,
            data=data,
            headers=headers)

        prepare = session.prepare_request(builder)

        response = session.send(prepare)

        if errors._raise_error_by_code(response.status_code):
            return responses.Responses(error_code=response.status_code,
                                       message=response.json())
        else:
            return responses.Responses(code=response.json()
                                       .get('meta').get('code'),
                                       message=response.json()
                                       .get('meta').get('message'),
                                       meta=response.json().get('meta'),
                                       data=response.json()
                                       .get('data'))


