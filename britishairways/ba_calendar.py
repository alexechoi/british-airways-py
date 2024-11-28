import requests
from .config import BASE_URL, HEADERS
from .utils import build_url, parse_response


def get_calendar_prices(origin, destination, trip_length, months):
    """
    Fetch calendar pricing data for a specific origin-destination pair.

    Args:
        origin (str): The origin airport code (e.g., "LHR").
        destination (str): The destination airport code (e.g., "NYC").
        trip_length (int): The number of nights for the trip.
        months (list): A list of months in "YYYYMM" format.

    Returns:
        list: A list of parsed results containing calendar pricing data.
    """
    # Construct the query parameters
    params = {
        "fq": f"month_year:({' OR '.join(months)})",
        "fq": f"number_of_nights:{trip_length}",
        "fq": f"departure_city:{origin}",
        "fq": f"arrival_city:{destination}",
        "fq": "cabin:M",
        "fq": "trip_type:RT",
        "fq": "-outbound_date:[* TO NOW-1DAY]",
        "wt": "json",
        "group": "true",
        "group.field": "outbound_date_string",
        "sort": "outbound_date asc,lowest_price asc",
        "group.main": "true",
        "rows": "93",
    }

    # Build the request URL
    url = build_url("lpbd/lpbdcalendar", params)

    # Debugging: Log the request details
    print(f"Requesting URL: {url}")
    print(f"Headers: {HEADERS}")

    try:
        # Send the GET request
        response = requests.get(url, headers=HEADERS)

        # Debugging Response
        print(f"Response Status: {response.status_code}")
        print(f"Response Headers: {response.headers}")
        print(f"Raw Response: {response.text}")

        # Validate Response
        if response.status_code == 404:
            raise Exception("404: Resource not found. Check if the endpoint is correct.")
        elif response.status_code != 200:
            raise Exception(f"HTTP Error {response.status_code}: {response.text}")

        # Handle content type
        content_type = response.headers.get("Content-Type", "")
        if "application/json" in content_type:
            response_data = response.json()
        elif "text/plain" in content_type:
            # Attempt to parse plain text as JSON
            try:
                import json
                response_data = json.loads(response.text)
            except json.JSONDecodeError:
                raise Exception(f"Failed to decode JSON from text/plain response. Raw Response: {response.text}")
        else:
            raise Exception(f"Unexpected Content-Type: {content_type}")

        return parse_response(response_data)

    except requests.RequestException as e:
        raise Exception(f"Network error: {e}")
    except Exception as e:
        raise Exception(f"Error occurred: {e}")