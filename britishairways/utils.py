# utils.py
from urllib.parse import urlencode
from .config import BASE_URL
from datetime import datetime

# Helper function to build URLs with encoded parameters
def build_url(endpoint, params):
    """
    Constructs a fully encoded URL with query parameters.
    
    Args:
        endpoint (str): API endpoint.
        params (dict): Dictionary of query parameters.

    Returns:
        str: Complete URL with encoded query parameters.
    """
    encoded_params = urlencode(params, safe="():*+")
    return f"{BASE_URL}/{endpoint}?{encoded_params}"

def validate_date(date_string):
    """
    Validates whether a given string is in the format YYYY-MM-DD.
    :param date_string: Date string to validate.
    :return: True if valid, False otherwise.
    """
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def encode_query_params(params):
    """
    Encodes query parameters while preserving special characters like ():*+.
    :param params: Dictionary of query parameters.
    :return: Encoded query string.
    """
    return urlencode(params, safe="():*+")

def parse_grouped_response(response_data):
    """
    Parses the 'grouped' section of the response.
    :param response_data: API response JSON.
    :return: Parsed data as a list of dictionaries.
    """
    if not response_data or "grouped" not in response_data:
        return []

    results = []
    grouped = response_data["grouped"]
    for key, value in grouped.items():
        for doc in value.get("doclist", {}).get("docs", []):
            results.append({
                "destination": doc.get("arr_city_name"),
                "price": doc.get("rounded_lowest_price"),
                "currency": doc.get("currency_code"),
                "departure": doc.get("departure_airport"),
                "arrival": doc.get("arrival_airport"),
                "dates": {
                    "outbound": doc.get("outbound_date"),
                    "inbound": doc.get("inbound_date")
                }
            })
    return results

def parse_response(response_data):
    """
    Parses the 'response' section of the API response.
    :param response_data: API response JSON.
    :return: Parsed data as a list of dictionaries.
    """
    if not response_data or "response" not in response_data:
        return []

    return [
        {
            "outbound_date": doc.get("outbound_date"),
            "price": doc.get("rounded_lowest_price"),
            "cabin": doc.get("cabin"),
        }
        for doc in response_data["response"].get("docs", [])
    ]