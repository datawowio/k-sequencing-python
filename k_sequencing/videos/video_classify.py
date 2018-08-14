from k_sequencing.connector import Connector


class VideoClassify():

    def __init__(self, token):
        self.token = token

    def create(self, params=None):
        """Create video closed question

        Args:
            data (str): URL of video
            muted (bool): Mute video on start (default: true)
            allow_seeking (bool): Allow seeking video player
            play_at (float): Setting video start time
            postback_url (str): URL for callback once video has been checked
            postback_method (str): Configuration HTTP method GET POST PUT PATCH
            custom_id (str): Custom ID that used for search

        Returns:
            dict: The value containt in Response class as dict

        """

        return Connector(self.token, model_type="videos", model_class="closed_questions").send(
            method='POST',
            data=params)

    def list(self, params=None):
        """Retrieve list of video closed question

        Args:
            page (int): Page of data
            per_page (int): Limit of date per page

        Returns:
           dict: The value containt in Response class as dict

         """

        return Connector(self.token, model_type="videos", model_class="closed_questions").send(
            method='GET',
            data=params)

    def find_id(self, video_id=None):
        """Retrieve video by ID or custom ID

        Args:
            id (int): ID of data
            custom_id (int): custom ID of data

        Returns:
           dict: The value containt in Response class as dict

        """

        return Connector(self.token, model_type="videos", model_class="closed_questions").send(
            method='GET',
            doc_id=video_id)
