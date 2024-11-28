# test_utils.py
import unittest
from britishairways.utils import validate_date, format_response


class TestUtils(unittest.TestCase):
    def test_validate_date_valid(self):
        self.assertTrue(validate_date("2025-01-01"))

    def test_validate_date_invalid(self):
        self.assertFalse(validate_date("01-01-2025"))

    def test_format_response_empty(self):
        response = {}
        self.assertEqual(format_response(response), [])

    def test_format_response_with_data(self):
        response = {
            "grouped": {
                "arr_city_name": {
                    "doclist": {
                        "docs": [
                            {
                                "arr_city_name": "Tokyo",
                                "rounded_lowest_price": 500,
                                "currency_code": "GBP",
                                "departure_airport": "LHR",
                                "arrival_airport": "HND",
                                "outbound_date": "2025-01-10",
                                "inbound_date": "2025-01-17"
                            }
                        ]
                    }
                }
            }
        }
        formatted = format_response(response)
        self.assertEqual(len(formatted), 1)
        self.assertEqual(formatted[0]["destination"], "Tokyo")
        self.assertEqual(formatted[0]["price"], 500)