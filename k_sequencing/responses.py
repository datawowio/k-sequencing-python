class Responses:
    def __init__(self, success_code=None, error_code=None,
                 message=None, data=None):
        self.success_code = success_code
        self.error_code = error_code
        self.message = message
        self.data = data
