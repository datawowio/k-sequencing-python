from k_sequencing.connector import Connector


class Message():

    def __init__(self, token):
        self.token = token

    def create(self, params=None):
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
        return Connector(self.token, model_type="images", model_class="messages").send(
            method='POST',
            data=params)

    def list(self, params=None):
        """Get image messages

        Args:
            page (int): Page of data
            per_page (int): Limit of date per page

        Returns:

        Raises:


         """

        return Connector(self.token, model_type="images", model_class="messages").send(
            method='GET',
            data=params)

    def find_id(self, image_id=None):
        """Get image by ID

        Args:
            id (int): ID of data
            custom_id (int): custom ID of data

        Returns:

        Raises:

        """
        return Connector(self.token, model_type="images", model_class="find").send(
            method='GET',
            data={"id": image_id})
