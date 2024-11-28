from .ba_cheapest import get_cheapest_round_trips
from .ba_graphs import get_monthly_graphs
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

    def get_monthly_graphs(self, origin, destination, trip_length):
        """
        Wrapper for fetching monthly graphs data.

        Args:
            origin (str): The origin airport code (e.g., "LON").
            destination (str): The destination airport code (e.g., "ATL").
            trip_length (int): The number of nights for the trip.

        Returns:
            list: A list of parsed results containing graphs data.
        """
        return get_monthly_graphs(origin, destination, trip_length)