# importing the requests library
from requests import Request, Session
import os
import errors
import responses


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
            if 'PROJECT_KEY' in os.environ:
                self.project_key = os.environ['PROJECT_KEY']
            else:
                raise AttributeError('Project key is missing')
        else:
            self.project_key = project_key

        self.headers = self._build_header(headers)
        # self.base_api = 'https://k-sequencing.datawow.io/api/'
        self.base_api = 'https://kseq.datawow.io/api/'

    def _build_header(self, headers=None):

        if headers is None:
            headers = {}

        headers['Authorization'] = self.project_key
        headers['Accept'] = 'application/json'
        headers['Content-Type'] = 'application/x-www-form-urlencoded'

        return headers

    def _connection(self, method='GET', url=None, data=None, headers=None):

        session = Session()

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

    """ ----- get by id  metohd ----- """
    def get_image_by_id(self, image_id=None):
        """Get image by ID 

        Args:
            id (int): ID of data
            custom_id (int): custom ID of data

        Returns:

        Raises:

        """

        return self._connection(
            method='GET',
            url='projects/images/' + image_id,
            data=None,
            headers=self.headers)

    """ ----- create metohd ----- """
    def create_image_choices(self, params=None):
        """Create new image choices

        Args:
            instruction (str): Detail about image.
            categories (str): The list of choice. sparate by use space.
            data (str): URL of imagee
            postback_url (str): URL for callback
            multiple (bool): Config multiple select
            postback_method (str): Config HTTP method GET POST PUT PATCH DELETE
            custom_id (str): Custom ID
            staff_id (int): assign to staff

        Returns:

        Raises:

        """
        return self._connection(
            method='POST',
            url='images/choices',
            data=params,
            headers=self.headers)

    def create_image_closed_questions(self, params=None):
        """Create new closed questions

        Args:
            instruction (str): Detail about image.
            data (str): URL of imagee
            postback_url (str): URL for callback
            postback_method (str): Config HTTP method GET POST PUT PATCH DELETE
            custom_id (str): Custom ID
            staff_id (int): assign to staff

        Returns:

        Raises:

        """

        return self._connection(
            method='POST',
            url='images/closed_questions',
            data=params,
            headers=self.headers)

    def create_image_messages(self, params=None):
        """Create image messages

        Args:
            instruction (str): Detail about image.
            data (str): URL of imagee
            postback_url (str): URL for callback
            postback_method (str): Config HTTP method GET POST PUT PATCH DELETE
            custom_id (str): Custom ID
            staff_id (int): assign to staff

        Returns:

        Raises:

         """

        return self._connection(
            method='POST',
            url='images/messages',
            data=params,
            headers=self.headers)

    def create_image_photo_tags(self, params=None):
        """Create new photo tags

        Args:
            instruction (str): Detail about image.
            data (str): URL of imagee
            postback_url (str): URL for callback
            postback_method (str): Config HTTP method GET POST PUT PATCH DELETE
            custom_id (str): Custom ID
            staff_id (int): assign to staff

        Returns:

        Raises:

        """

        return self._connection(
            method='POST',
            url='images/photo_tags',
            data=params,
            headers=self.headers)

    def create_prediction(self, params=None):
        """Create new photo tags

        Args:
            data (str): URL of imagee
            postback_url (str): URL for callback
            postback_method (str): Config HTTP method GET POST PUT PATCH DELETE
            custom_id (str): Custom ID

        Returns:

        Raises:

        """

        return self._connection(
            method='POST',
            url='prime/predictions',
            data=params,
            headers=self.headers)

    """ ----- get metohd ----- """
    def get_image_choices(self, params=None):
        """Get image choices

        Args:
            page (int): Page of data
            per_page (int): Limit of date per page

        Returns:

        Raises:


         """

        return self._connection(
            method='GET',
            url='images/choices',
            data=params,
            headers=self.headers)

    def get_image_closed_questions(self, params=None):
        """Get image closed questions

        Args:
            page (int): Page of data
            per_page (int): Limit of date per page

        Returns:

        Raises:

         """

        return self._connection(
            method='GET',
            url='images/closed_questions',
            data=params,
            headers=self.headers)

    def get_image_messages(self, params=None):
        """Get image messages

        Args:
            page (int): Page of data
            per_page (int): Limit of date per page

        Returns:

        Raises:

        """

        return self._connection(
            method='GET',
            url='images/messages',
            data=params,
            headers=self.headers)

    def get_image_photo_tags(self, params=None):
        """Get image photo tags

        Args:
            page (int): Page of data
            per_page (int): Limit of date per page

        Returns:

        Raises:

        """

        return self._connection(
            method='GET',
            url='images/photo_tags',
            data=params,
            headers=self.headers)

    def get_prediction(self, params=None):
        """Get prediction

        Args:
            page (int): Page of data
            per_page (int): Limit of date per page

        Returns:

        Raises:

         """

        return self._connection(
            method='GET',
            url='prime/predictions',
            data=params,
            headers=self.headers)
