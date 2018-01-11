class Responses:
    def __init__(self, code=None, error_code=None,
                 message=None, data=None, meta=None):
        self.code = code
        self.error_code = error_code
        self.message = message
        self.meta = meta
        self.data = data
