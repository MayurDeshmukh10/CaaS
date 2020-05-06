class Error(Exception):
    """Base class for other exceptions """
    pass


class InvalidAuthKeyError(Error):
    """Raised when auth key is invalid"""
    pass

class ImageTooSmallError(Error):
    """Raised when image is too small to compression"""
    pass
	

