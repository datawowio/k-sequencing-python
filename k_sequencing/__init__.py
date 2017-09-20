# importing the requests library
from requests import Request, Session
import os
import errors
import responses


def info():
    print("k-sequencing-python")


class Requests(object):

    def __init__(self, project_key=None, headers=None):

        if project_key is None:
            if 'PROJECT_KEY' in os.environ:
                self.project_key = os.environ['PROJECT_KEY']
            else:
                raise AttributeError('Project key is missing')
        else:
            self.project_key = project_key

        self.headers = self._build_header(headers)

    def _build_header(self, headers=None):

        if headers is None:
            headers = {}

        headers['Authorization'] = self.project_key
        headers['Accept'] = 'application/json'
        headers['Content-Type'] = 'application/x-www-form-urlencoded'

        return headers

    def _connection(self, method='GET', url=None, data=None, headers=None):

        session = Session()

        builder = Request(method, url, data=data, headers=headers)
        prepare = session.prepare_request(builder)

        response = session.send(prepare)

        if errors._raise_error_by_code(response.status_code):
            return responses.Responses(error_code=response.status_code,
                                       message=response.json())
        else:
            return responses.Responses(success_code=response.status_code,
                                       message=response.json()
                                       .get('meta')
                                       .get('message'), data=response.json()
                                       .get('data'))

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
            url='https://kseq.datawow.io/api/images/choices',
            data=params,
            headers=self.headers)

    def create_image_closed_questions(self, params=None):
        """Create new image

        Args:
            instruction (str): Detail about image.
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
            url='https://kseq.datawow.io/api/images/closed_questions',
            data=params,
            headers=self.headers)

    def create_image_messages(self, params=None):
        """Create image messages

        Args:
            instruction (str): Detail about image.
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
            url='https://kseq.datawow.io/api/images/messages',
            data=params,
            headers=self.headers)

    def create_image_photo_tags(self, params=None):
        """Create new photo tags

        Args:
            instruction (str): Detail about image.
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
            url='https://kseq.datawow.io/api/images/photo_tags',
            data=params,
            headers=self.headers)

    def get_image_choice(self, params=None):
        """Get image messages

        Args:
            page (int): Page of data
            per_page (int): Limit of date per page

        Returns:

        Raises:


         """

        return self._connection(
            method='GET',
            url='https://kseq.datawow.io/api/images/choices',
            data=params,
            headers=self.headers)

    def get_image_closed_question(self, params=None):
        """Get image messages

        Args:
            page (int): Page of data
            per_page (int): Limit of date per page

        Returns:

        Raises:

         """

        return self._connection(
            method='GET',
            url='https://kseq.datawow.io/api/images/closed_question',
            data=params,
            headers=self.headers)

    def get_image_message(self, params=None):
        """Get image messages

        Args:
            page (int): Page of data
            per_page (int): Limit of date per page

        Returns:

        Raises:

        """

        return self._connection(
            method='GET',
            url='https://kseq.datawow.io/api/images/messages',
            data=params,
            headers=self.headers)

    def get_image_photo_tag(self, params=None):
        """Get image messages

        Args:
            page (int): Page of data
            per_page (int): Limit of date per page

        Returns:

        Raises:

        """

        return self._connection(
            method='GET',
            url='https://kseq.datawow.io/api/images/photo_tags',
            data=params,
            headers=self.headers)
