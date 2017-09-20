__error_code__ = {
    401: 'unauthorized',
    400: 'bad request',
    404: 'not found',
    403: 'not permitted'
}


def _raise_error_by_code(code):
    return __error_code__.get(code)
