from k_sequencing.connector import Connector


class ClosedQuestion():

    def __init__(self, token):
        self.token = token

    def create(self, params=None):
        """Create image closed questions

        Args:
            data (str): URL of image
            postback_url (str): URL for callback once image has been checked
            postback_method (str): Config HTTP method GET POST PUT PATCH
            custom_id (str): Custom ID that used for search

        Returns:
            dict: The value containt in Response class as dict.

        """

        return Connector(self.token, model_type="images", model_class="closed_questions").send(
            method='POST',
            data=params)

    def list(self, params=None):
        """Retrieve list of image closed questions

        Args:
            page (int): Page of data
            per_page (int): Limit of date per page

        Returns:
            dict: The value containt in Response class as dict

         """

        return Connector(self.token, model_type="images", model_class="closed_questions").send(
            method='POST',
            data=params)

    def find_id(self, image_id=None):
        """Retrieve image by ID or custom ID

        Args:
            id (int): ID of data
            custom_id (int): custom ID of data

        Returns:
            dict: The value containt in Response class as dict

        """

        return Connector(self.token, model_type="images", model_class="find").send(
            method='POST',
            doc_id=image_id)
