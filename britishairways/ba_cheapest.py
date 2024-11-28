import requests
from urllib.parse import urlencode
from .config import BASE_URL, HEADERS
from .utils import build_url, parse_grouped_response


def get_cheapest_round_trips(region, origin):
    """
    Fetch the cheapest round-trip prices for a specific region and origin.

    Args:
        region (str): The region code (e.g., "FEA" for Far East Asia).
        origin (str): The origin airport code (e.g., "LON" for London).

    Returns:
        list: A list of parsed results containing destinations and prices.

    Raises:
        Exception: If the response has unexpected content or a network issue occurs.
    """
    fq_template = (
        "region_code:({region})+AND+departure_city:{origin}+AND+arr_city_name_search:***"
        "+AND+arrival_city:*+AND+trip_type:RT+AND+number_of_nights:1+AND+cabin:M"
    )
    fq = fq_template.format(region=region, origin=origin)

    # Define parameters with + encoding
    params = {
        "fq": fq,
        "facet.pivot": "arrival_city,is_sales_fare",
        "facet": "true",
    }

    # Construct the URL
    url = build_url("lpbd/lpfdestinations", params)

    # Send the GET request
    try:
        response = requests.get(url, headers=HEADERS)

        # Validate Response
        if response.status_code == 404:
            raise Exception("404: Resource not found. Check if the endpoint is correct.")
        elif response.status_code != 200:
            raise Exception(f"HTTP Error {response.status_code}: {response.text}")

        # Handle Content-Type manually
        content_type = response.headers.get("Content-Type", "")
        if "application/json" in content_type:
            response_data = response.json()
        elif "text/plain" in content_type:
            # Attempt to parse raw text as JSON
            try:
                import json
                response_data = json.loads(response.text)
            except json.JSONDecodeError:
                raise Exception(f"Failed to decode JSON from text/plain response. Raw Response: {response.text}")
        else:
            raise Exception(f"Unexpected Content-Type: {content_type}")

        return parse_grouped_response(response_data)

    except requests.RequestException as e:
        raise Exception(f"Network error: {e}")
    except Exception as e:
        raise Exception(f"Error occurred: {e}")