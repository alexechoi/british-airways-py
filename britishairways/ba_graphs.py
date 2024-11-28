import requests
from urllib.parse import urlencode
from .config import BASE_URL, HEADERS
from .utils import build_url, parse_grouped_response


def get_monthly_graphs(origin, destination, trip_length):
    """
    Fetch monthly graphs data for a specific origin-destination pair.

    Args:
        origin (str): Origin airport code (e.g., "LON").
        destination (str): Destination airport code (e.g., "ATL").
        trip_length (int): Number of nights for the trip.

    Returns:
        list: Parsed graphs data with flight details.
    """
    fq_template = "departure_city:{origin}+AND+arrival_city:{destination}+AND+trip_type:RT+AND+number_of_nights:{trip_length}+AND+cabin:M"
    fq = fq_template.format(origin=origin, destination=destination, trip_length=trip_length)

    # Define parameters with + encoding
    params = {
        "fq": fq,
        "facet.pivot": "month_string,is_sales_fare",
        "facet": "true",
    }

    # Construct the URL
    url = build_url("lpbd/lpfgraphs", params)

    # Debugging: Log request details
    print(f"Requesting URL: {url}")
    print(f"Headers: {HEADERS}")

    # Send the GET request
    try:
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