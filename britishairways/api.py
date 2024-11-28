from .ba_cheapest import get_cheapest_round_trips
from .config import BASE_URL, HEADERS
from .utils import parse_response, build_url


class BritishAirways:
    def __init__(self):
        """
        Initialize the British Airways API client.
        """
        self.base_url = BASE_URL
        self.headers = HEADERS

    def get_cheapest_round_trips(self, region, origin):
        """
        Wrapper for fetching the cheapest round-trip flights.

        Args:
            region (str): The region code (e.g., "FEA").
            origin (str): The origin airport code (e.g., "LON").

        Returns:
            list: A list of parsed results containing destinations and prices.
        """
        return get_cheapest_round_trips(region, origin)