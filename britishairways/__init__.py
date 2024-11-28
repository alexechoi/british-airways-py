# __init__.py

from .api import BritishAirways
from .data import REGIONS, DESTINATIONS, CABINS
from .exceptions import APIError, ValidationError

__all__ = ["BritishAirways", "REGIONS", "DESTINATIONS", "CABINS", "APIError", "ValidationError"]