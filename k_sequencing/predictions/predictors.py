from k_sequencing.connector import Connector

class Predictor():

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
            url='prime/predictions',
            data=params)

    def list(self, params=None):
        """Get prediction

        Args:
            page (int): Page of data
            per_page (int): Limit of date per page

        Returns:

        Raises:

         """

        return Connector(self.token).send(
            method='GET',
            url='prime/predictions',
            data=params)

    def find_id(self, image_id=None):

        """Get image by ID

        Args:
            id (int): ID of data
            custom_id (int): custom ID of data

        Returns:

        Raises:

        """

        return Connector(self.token).send(
            method='GET',
            url='projects/images/' + image_id,
            data=None)
