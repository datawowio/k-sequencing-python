from k_sequencing.connector import Connector


class Choice():

    def __init__(self, token):
        self.token = token

    def create(self, params=None):
        """Create image choices

        Args:
            instruction (str): Tell moderator what answer you expected and what image is
            categories (str): The list of choice that can be possible. sparate by use space
            data (str): URL of image
            postback_url (str): URL for callback once image has been checked
            postback_method (str): Config HTTP method GET POST PUT PATCH
            multiple (bool): Config multiple select
            custom_id (str): Custom ID that used for search

        Returns:
            dict: The value containt in Response class as dict

        """
        return Connector(self.token, model_type="images", model_class="choices").send(
            method='POST',
            data=params)

    def list(self, params=None):
        """Retrive list of image choices

        Args:
            page (int): Page of data
            per_page (int): Limit of date per page

        Returns:
            dict: The value containt in Response class as dict

         """

        return Connector(self.token, model_type="images", model_class="choices").send(
            method='GET',
            data=params)

    def find_id(self, image_id=None):
        """Retrive image by ID or custom ID

        Args:
            id (int): ID of data
            custom_id (int): custom ID of data

        Returns:

        """

        return Connector(self.token, model_type="images", model_class="find").send(
            method='GET',
            doc_id=image_id)
