class Responses:
    def __init__(self, code=None, error_code=None,
                 message=None, data=None):
        self.code = code
        self.error_code = error_code
        self.message = message
        self.data = data
