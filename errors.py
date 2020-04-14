class Error(Exception):
    """Base class for other exceptions """
    pass


class InvalidAuthKeyError(Error):
    """Raised when auth key is invalid"""
    pass

