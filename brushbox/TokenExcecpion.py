# Token Exception
class TokenException(Exception):
    """Exception raised for errors in the token."""
    def __init__(self, message="Token expired"):
        self.message = message
        super().__init__(self.message)