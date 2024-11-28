# British Airways API Python Package

This Python package provides an interface to fetch data from the British Airways Low-Price Finder API. Currently, it supports fetching the **cheapest round-trip flights** and **monthly pricing graphs** for specified routes. **This package is in no way affiliated with British Airways**

## Features

- Fetch the **cheapest round-trip flights** for a region and origin airport.
- Retrieve **monthly pricing data** for a specific route.

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

### 1. `get_cheapest_round_trips`

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

#### Example Output:
```json
[
    {
        "destination": "Hong Kong",
        "price": 690,
        "currency": "GBP",
        "departure": "LHR",
        "arrival": "HKG",
        "dates": {
            "outbound": "2024-12-01",
            "inbound": "2024-12-07"
        }
    },
    {
        "destination": "Tokyo",
        "price": 931,
        "currency": "GBP",
        "departure": "LHR",
        "arrival": "HND",
        "dates": {
            "outbound": "2024-12-15",
            "inbound": "2024-12-21"
        }
    }
]
```

### 2. `get_monthly_graphs`

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

#### Example Output:
```json
[
    {
        "destination": null,
        "price": 1488,
        "currency": "GBP",
        "departure": "LHR",
        "arrival": "ATL",
        "dates": {
            "outbound": "2024-10-11",
            "inbound": "2024-10-18"
        }
    },
    {
        "destination": null,
        "price": 1308,
        "currency": "GBP",
        "departure": "LHR",
        "arrival": "ATL",
        "dates": {
            "outbound": "2024-11-12",
            "inbound": "2024-11-19"
        }
    }
]
```

---

## Region Codes

The following region codes are supported:

| Code      | Region                                  |
|-----------|-----------------------------------------|
| `NOA`     | North America                          |
| `SOA`     | Latin America and Caribbean            |
| `EUK`     | Europe, UK, and Ireland                |
| `SAS`     | South and Central Asia                 |
| `MDE+OR+AFR` | Middle East and Africa               |
| `FEA`     | Far East and Australia                 |

---

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue.

---

## License

This project is licensed under the MIT License.

---

Happy Coding!