from .connector import Connector


class Choice():

    def __init__(self, token):
        self.token = token

    def create(self, params=None):
        """Create new image choices

        Args:
            instruction (str): Detail about image.
            categories (str): The list of choice. sparate by use space.
            data (str): URL of imagee
            postback_url (str): URL for callback
            multiple (bool): Config multiple select
            postback_method (str): Config HTTP method GET POST PUT PATCH DELETE
            custom_id (str): Custom ID
            staff_id (int): assign to staff

        Returns:

        Raises:

        """
        return Connector(self.token).send(
            method='POST',
            url='images/choices',
            data=params)

    def list(self, params=None):
        """Get image choices

        Args:
            page (int): Page of data
            per_page (int): Limit of date per page

        Returns:

        Raises:


         """

        return Connector(self.token).send(
            method='GET',
            url='images/choices',
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


class ClosedQuestion():

    def __init__(self, token): 
        self.token = token

    def create(self, params=None):
        """Create new closed questions

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

        return Connector(self.token).send(
            method='POST',
            url='images/closed_questions',
            data=params)

    def list(self, params=None):
        """Get image closed questions

        Args:
            page (int): Page of data
            per_page (int): Limit of date per page

        Returns:

        Raises:


         """

        return Connector(self.token).send(
            method='GET',
            url='images/closed_questions',
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

        return Connector(self.token).send(
            method='POST',
            url='images/messages',
            data=params)

    def list(self, params=None):
        """Get image messages

        Args:
            page (int): Page of data
            per_page (int): Limit of date per page

        Returns:

        Raises:


         """

        return Connector(self.token).send(
            method='GET',
            url='images/messages',
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


class PhotoTag():

    def __init__(self, token):
        self.token = token

    def create(self, params=None):
        """Create new photo tags

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

        return Connector(self.token).send(
            method='POST',
            url='images/photo_tags',
            data=params)

    def list(self, params=None):
        """Get image photo tags

        Args:
            page (int): Page of data
            per_page (int): Limit of date per page

        Returns:

        Raises:

        """

        return Connector(self.token).send(
            method='GET',
            url='images/photo_tags',
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


class Prediction():

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
