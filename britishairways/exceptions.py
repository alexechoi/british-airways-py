# exceptions.py

class APIError(Exception):
    """
    Exception raised when an API request fails.
    """
    def __init__(self, message):
        super().__init__(f"APIError: {message}")


class ValidationError(Exception):
    """
    Exception raised for invalid input parameters.
    """
    def __init__(self, message):
        super().__init__(f"ValidationError: {message}")