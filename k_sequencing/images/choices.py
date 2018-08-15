from k_sequencing.connector import Connector


class Choice():

    def __init__(self, token):
        self.token = token

    def create(self, params=None):
        """Create image choices

        Args:
            instruction (str): Tell moderator what answer you expected and what image is
            categories (str): List of answers that you were expected. sparate by use space
            data (str): URL of image
            postback_url (str): URL for answer callback once image has been checked
            postback_method (str): Configuration HTTP method GET POST PUT PATCH
            multiple (bool): Configuration for multiple selection of category to answer
            allow_empty (bool): Allow answer can be blank
            custom_id (str): Custom ID that used for search

        Returns:
            dict: The value containt in Response class as dict

        """
        return Connector(self.token, model_type="images", model_class="choices").send(
            method='POST',
            data=params)

    def list(self, params=None):
        """Retrieve list of image choices

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
        """Retrieve image by ID or custom ID

        Args:
            image_id (int): Image's ID or custom ID which is you were assigned

        Returns:

        """

        return Connector(self.token, model_type="images", model_class="find").send(
            method='GET',
            doc_id=image_id)
