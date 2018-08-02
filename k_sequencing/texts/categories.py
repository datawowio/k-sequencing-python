from k_sequencing.connector import Connector

class CategoryClassify():

    def __init__(self, token):
        self.token = token

    def create(self, params=None):
        """Create new photo tags

        Args:
            data (str): URL of imagee
            postback_url (str): URL for callback
            postback_method (str): Config HTTP method GET POST PUT PATCH DELETE
            custom_id (str): Custom ID

        Returns:

        Raises:

        """

        return Connector(self.token).send(
            method='POST',
            url='v1/text/text_categories',
            data=params)
