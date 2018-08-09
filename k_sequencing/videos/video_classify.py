from k_sequencing.connector import Connector


class VideoClassify():

    def __init__(self, token):
        self.token = token

    def create(self, params=None):
        """Create video closed question

        Args:
            data (str): URL of image
            muted (bool): Mute viode on start (default: true)
            allow_seeking (bool): Allow seeking video player
            play_at (float): Setting video start time
            postback_url (str): URL for callback once image has been checked
            postback_method (str): Config HTTP method GET POST PUT PATCH
            custom_id (str): Custom ID that used for search

        Returns:
            dict: The value containt in Response class as dict

        """

        return Connector(self.token, model_type="videos", model_class="closed_questions").send(
            method='POST',
            data=params)

    def list(self, params=None):
        """Retrive list of video closed question

        Args:
            page (int): Page of data
            per_page (int): Limit of date per page

        Returns:
           dict: The value containt in Response class as dict

         """

        return Connector(self.token, model_type="videos", model_class="closed_questions").send(
            method='GET',
            data=params)

    def find_id(self, image_id=None):
        """Retrive video by ID or custom ID

        Args:
            id (int): ID of data
            custom_id (int): custom ID of data

        Returns:
           dict: The value containt in Response class as dict

        """

        return Connector(self.token, model_type="videos", model_class="closed_questions").send(
            method='GET',
            doc_id=image_id)
