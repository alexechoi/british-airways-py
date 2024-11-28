import requests
from .config import BASE_URL, HEADERS
from .utils import parse_response

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
    endpoint = "lpbd/lpbdcalendar"

    # Construct the query parameters with dynamic values
    query_params = (
        f"fq=month_year:({'%20OR%20'.join(months)})&"
        f"fq=number_of_nights:{trip_length}&"
        f"fq=departure_city:{origin}&"
        f"fq=arrival_city:{destination}&"
        "fq=cabin:M&"
        "fq=trip_type:RT&"
        "fq=-outbound_date:[*+TO+NOW-1DAY]&"
        "wt=json&"
        "group=true&"
        "group.field=outbound_date_string&"
        "sort=outbound_date%20asc,lowest_price%20asc&"
        "group.main=true&"
        "rows=93"
    )

    # Build the request URL
    url = f"{BASE_URL}/{endpoint}?{query_params}"

    try:
        # Send the GET request
        response = requests.get(url, headers=HEADERS)

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