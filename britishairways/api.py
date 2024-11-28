from .ba_cheapest import get_cheapest_round_trips
from .ba_graphs import get_monthly_graphs
from .ba_calendar import get_calendar_prices
from .config import BASE_URL, HEADERS
from datetime import datetime, timedelta

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

    def get_calendar_prices(self, origin, destination, trip_length, months, trip_type):
        """
        Wrapper for fetching calendar pricing data.

        Args:
            origin (str): The origin airport code (e.g., "LHR").
            destination (str): The destination airport code (e.g., "NYC").
            trip_length (int): The number of nights for the trip.
            months (list): A list of months in "YYYYMM" format.

        Returns:
            list: A list of parsed results containing calendar pricing data.
        """
        return get_calendar_prices(origin, destination, trip_length, months)
    
    def get_specific_round_trip(self, origin, destination, departure_date, return_date):
        """
        Fetch specific round-trip flights for a given destination on certain dates.

        Args:
            origin (str): The origin airport code (e.g., "LHR").
            destination (str): The destination airport code (e.g., "JFK").
            departure_date (str): The departure date in "YYYY-MM-DD" format.
            return_date (str): The return date in "YYYY-MM-DD" format.

        Returns:
            list: Filtered flight options for the specified dates.
        """
        if not return_date:
            raise ValueError("A return_date is required for round trips.")

        # Parse the departure and return dates
        departure_dt = datetime.strptime(departure_date, "%Y-%m-%d")
        return_dt = datetime.strptime(return_date, "%Y-%m-%d")

        # Calculate the trip length
        trip_length = (return_dt - departure_dt).days

        if trip_length <= 0:
            raise ValueError("return_date must be after departure_date.")

        # Determine months for the calendar query
        months = list({departure_dt.strftime("%Y%m"), return_dt.strftime("%Y%m")})

        # Fetch calendar prices
        calendar_data = self.get_calendar_prices(origin, destination, trip_length, months, trip_type="RT")

        # Filter flights for the specific departure date
        filtered_flights = [
            flight for flight in calendar_data
            if flight.get('outbound_date') == f"{departure_date}T00:00:00Z"
        ]

        return filtered_flights
    
    def get_one_way_price(self, origin, destination, departure_date):
        """
        Fetch the price for a one-way flight on a specific date.

        Args:
            origin (str): The origin airport code (e.g., "LHR").
            destination (str): The destination airport code (e.g., "JFK").
            departure_date (str): The departure date in "YYYY-MM-DD" format.

        Returns:
            list: Filtered flight options for the specified departure date.
        """
        # Parse the departure date
        departure_dt = datetime.strptime(departure_date, "%Y-%m-%d")
        months = [departure_dt.strftime("%Y%m")]

        # Fetch calendar prices with trip_type="OW"
        calendar_data = self.get_calendar_prices(origin, destination, 0, months, trip_type="OW")

        # Filter flights for the specific departure date
        filtered_flights = [
            flight for flight in calendar_data
            if flight.get('outbound_date') == f"{departure_date}T00:00:00Z"
        ]

        return filtered_flights
