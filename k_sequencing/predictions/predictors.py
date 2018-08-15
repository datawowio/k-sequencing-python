from k_sequencing.connector import Connector


class Predictor():

    def __init__(self, token):
        self.token = token

    def create(self, params=None):
        """Create prediction data

        Args:
            data (str): URL of image
            postback_url (str): URL for callback once image has been checked
            postback_method (str): Config HTTP method GET POST PUT PATCH
            custom_id (str): Custom ID that used for search

        Returns:
            dict: The value containt in Response class as dict

        """
        return Connector(self.token, model_type="ai", model_class="predictor").send(
            method='POST',
            data=params)

    def list(self, params=None):
        """Retrieve list of prediction data

        Args:
            page (int): Page of data
            per_page (int): Limit of date per page

        Returns:
            dict: The value containt in Response class as dict

         """

        return Connector(self.token, model_type="ai", model_class="predictor").send(
            method='GET',
            data=params)

    def find_id(self, image_id=None):
        """Retrieve image by ID or custom ID

        Args:
            image_id (int): Text's ID or custom ID which is you were assigned

        Returns:
            dict: The value containt in Response class as dict

        """
        return Connector(self.token, model_type="ai", model_class="find").send(
            method='GET',
            doc_id=image_id)
