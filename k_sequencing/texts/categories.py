from k_sequencing.connector import Connector


class CategoryClassify():

    def __init__(self, token):
        self.token = token

    def create(self, params=None):
        """Create categroy conversation classification

        Args:
            conversation (arr of dict): Example: { "name": "username or indicator as you wish", "message": "message use to classify" }
            title (str): Title of conversation
            postback_url (str): URL for callback
            postback_method (str): Configuration HTTP method GET POST PUT PATCH
            custom_id (str): Custom ID that used for search
            allow_empty (bool) : Answer can be empty

        Returns:
            dict: The value containt in Response class as dict

        """
        headers = {'Content-Type': 'application/json'}
        return Connector(self.token, model_type='texts', model_class='categories', headers=headers).send(method='POST', data=params)

    def list(self, params=None):
        """Retrieve list of conversation

        Args:
            page (int): Page of data
            per_page (int): Limit of date per page

        Returns:
            dict: The value containt in Response class as dict

         """

        return Connector(self.token, model_type='texts', model_class='categories').send(method='GET', data=params)

    def find_id(self, text_id=None):
        """Retrieve conversation by ID or custom ID

        Args:
            text_id (int): Text's ID or custom ID which is you were assigned

        Returns:
            dict: The value containt in Response class as dict

        """

        return Connector(self.token,
                         model_type='texts',
                         model_class='categories').send(method='GET',
                                                        doc_id=text_id,
                                                        query_str=True)
