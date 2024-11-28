# test_api.py
import unittest
from britishairways.api import BritishAirways
from britishairways.exceptions import ValidationError

class TestBritishAirwaysAPI(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.api = BritishAirways(market="gb-en")

    async def test_get_cheapest_round_trips_invalid_date(self):
        with self.assertRaises(ValidationError):
            await self.api.get_cheapest_round_trips("Europe", "LHR", "invalid-date")