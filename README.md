# British Airways API Python Package

This Python package provides an interface to fetch data from the British Airways Low-Price Finder API. It supports fetching **round-trip flight prices**, **one-way flight prices**, **monthly pricing graphs**, and **calendar pricing data**.

⚠️ **Disclaimer:** This package is in no way affiliated with British Airways.

---

## Features

- Fetch the **specific round-trip flight price** for given departure and return dates.
- Fetch the **specific one-way flight price** for a given date.
- Fetch the **cheapest round-trip flights** for a region and origin airport.
- Retrieve **monthly pricing data** for a specific route and trip length.
- Fetch **calendar-based pricing data** for specific months, showing daily flight prices.

---

## Installation

Clone the repository and install the package using pip:

```bash
git clone <repo-url>
cd british-airways-py
pip install .
```

---

## Functions

### 1. `get_one_way_price`

Fetch the price for a one-way flight on a specific date.

#### Parameters:
- `origin` (str): The origin airport code (e.g., "LHR").
- `destination` (str): The destination airport code (e.g., "JFK").
- `departure_date` (str): The departure date in `YYYY-MM-DD` format.

#### Example Usage:
```python
from britishairways.api import BritishAirways

# Initialize the client
ba = BritishAirways()

# Get a one-way flight price
one_way_flight = ba.get_one_way_price(
    origin="LON",
    destination="NYC",
    departure_date="2024-12-15"
)
print(one_way_flight)
```

Please note that sometimes this does not work with an IATA airport code. If there is a group of airports in a city, you should use that code for example LON will work but LHR will not work.

#### Example Output:
```json
[
    {
        "outbound_date": "2024-12-15T00:00:00Z",
        "price": 700,
        "cabin": "M"
    }
]
```

---

### 2. `get_specific_round_trip`

Fetch details for a specific round trip, given a departure and return date.

#### Parameters:
- `origin` (str): The origin airport code (e.g., "LHR").
- `destination` (str): The destination airport code (e.g., "JFK").
- `departure_date` (str): The departure date in `YYYY-MM-DD` format.
- `return_date` (str): The return date in `YYYY-MM-DD` format.

#### Example Usage:
```python
from britishairways.api import BritishAirways

# Initialize the client
ba = BritishAirways()

# Get details for a specific round trip
flights = ba.get_specific_round_trip(
    origin="LON",
    destination="NYC",
    departure_date="2024-12-15",
    return_date="2024-12-22"
)
print(flights)
```

Please note that sometimes this does not work with an IATA airport code. If there is a group of airports in a city, you should use that code for example LON will work but LHR will not work.

#### Example Output:
```json
[
    {
        "outbound_date": "2024-12-15T00:00:00Z",
        "price": 1934,
        "cabin": "M"
    }
]
```

---

### 3. `get_cheapest_round_trips`

Fetch the cheapest round-trip flights for a given region and origin.

#### Parameters:
- `region` (str): The region code (e.g., "FEA").
- `origin` (str): The origin airport code (e.g., "LON").

#### Example Usage:
```python
from britishairways.api import BritishAirways

# Initialize the client
ba = BritishAirways()

# Get the cheapest flights for Far East and Australia from London
cheapest_flights = ba.get_cheapest_round_trips(region="FEA", origin="LON")
print(cheapest_flights)
```

---

### 4. `get_monthly_graphs`

Retrieve monthly pricing data for a specific origin and destination.

#### Parameters:
- `origin` (str): The origin airport code (e.g., "LHR").
- `destination` (str): The destination airport code (e.g., "ATL").
- `trip_length` (int): The length of the trip in days (e.g., 7).

#### Example Usage:
```python
from britishairways.api import BritishAirways

# Initialize the client
ba = BritishAirways()

# Get monthly pricing data for a 7-day trip from London to Atlanta
monthly_graphs = ba.get_monthly_graphs(origin="LHR", destination="ATL", trip_length=7)
print(monthly_graphs)
```

---

### 5. `get_calendar_prices`

Retrieve calendar-based pricing data for specific months, displaying daily flight prices.

#### Parameters:
- `origin` (str): The origin airport code (e.g., "LHR").
- `destination` (str): The destination airport code (e.g., "NYC").
- `trip_length` (int): The number of nights for the trip (e.g., 7).
- `months` (list): A list of months in `YYYYMM` format (e.g., `["202412", "202501"]`).

#### Example Usage:
```python
from britishairways.api import BritishAirways

# Initialize the client
ba = BritishAirways()

# Get calendar pricing data for a 7-day trip from London to New York for specific months
calendar_prices = ba.get_calendar_prices(
    origin="LHR",
    destination="NYC",
    trip_length=7,
    months=["202412", "202501", "202502"]
)
print(calendar_prices)
```

---

## Region Codes

The following region codes are supported:

| Code           | Region                                   |
|-----------------|-----------------------------------------|
| `NOA`          | North America                           |
| `SOA`          | Latin America and Caribbean             |
| `EUK`          | Europe, UK, and Ireland                 |
| `SAS`          | South and Central Asia                  |
| `MDE+OR+AFR`   | Middle East and Africa                  |
| `FEA`          | Far East and Australia                  |

---

## Contributing

Contributions are welcome! If you find a bug or have a feature suggestion, feel free to open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License.

---

Happy Coding! 😊