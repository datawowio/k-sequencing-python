from k_sequencing.connector import Connector


class ClosedQuestion():

    def __init__(self, token):
        self.token = token

    def create(self, params=None):
        """Create text closed question

        Args:
            data (str): URL of imagee
            postback_url (str): URL for callback
            postback_method (str): Config HTTP method GET POST PUT PATCH DELETE
            custom_id (str): Custom ID

        Returns:
            dict: The value containt in Response class as dict

        """

        return Connector(self.token, model_type='texts', model_class='closed_questions').send(method='POST', data=params)

    def list(self, params=None):
        """Retrive list of text

        Args:
            page (int): Page of data
            per_page (int): Limit of date per page

        Returns:
            dict: The value containt in Response class as dict

         """

        return Connector(self.token, model_type='texts', model_class='closed_questions').send(method='GET', data=params)

    def find_id(self, text_id=None):
        """Retrive text by ID or custom ID

        Args:
            id (int): ID of data
            custom_id (int): custom ID of data

        Returns:
            dict: The value containt in Response class as dict

        """

        return Connector(self.token,
                         model_type='texts',
                         model_class='closed_questions').send(method='GET',
                                                              doc_id=text_id,
                                                              query_str=True)
