import unittest
from britishairways.api import BritishAirways
from britishairways.exceptions import ValidationError

class TestBritishAirwaysAPI(unittest.TestCase):
    def setUp(self):
        self.api = BritishAirways()

    def test_get_cheapest_round_trips(self):
        result = self.api.get_cheapest_round_trips("FEA", "LON")
        self.assertIsInstance(result, list)
        for flight in result:
            self.assertIn("destination", flight)
            self.assertIn("price", flight)
            self.assertIn("dates", flight)

    def test_get_specific_round_trip(self):
        result = self.api.get_specific_round_trip(
            origin="LON",
            destination="NYC",
            departure_date="2024-12-15",
            return_date="2024-12-22"
        )
        self.assertIsInstance(result, list)
        for flight in result:
            self.assertIn("outbound_date", flight)
            self.assertIn("price", flight)
            self.assertIn("cabin", flight)

    def test_get_specific_round_trip_invalid_dates(self):
        with self.assertRaises(ValueError):
            self.api.get_specific_round_trip(
                origin="LON",
                destination="NYC",
                departure_date="2024-12-22",
                return_date="2024-12-15"
            )

    def test_get_one_way_price(self):
        result = self.api.get_one_way_price(
            origin="LON",
            destination="NYC",
            departure_date="2024-12-15"
        )
        self.assertIsInstance(result, list)
        for flight in result:
            self.assertIn("outbound_date", flight)
            self.assertIn("price", flight)
            self.assertIn("cabin", flight)

    def test_get_one_way_price_invalid_date(self):
        with self.assertRaises(ValueError):
            self.api.get_one_way_price(
                origin="LON",
                destination="NYC",
                departure_date="invalid-date"
            )
