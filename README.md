# British Airways Python Package

The **British Airways Python Package** provides an easy-to-use interface for interacting with British Airways APIs. **This package is in no way affiliated with British Airways** This package simplifies fetching travel data such as the cheapest round-trip flight options. The package is modular and extendable, making it easy to add more features in the future.

---

## Installation

Clone this repository and install the required dependencies:

```bash
git clone <repository_url>
cd british-airways-py
pip install -r requirements.txt
```

---

## Features

### `get_cheapest_round_trips`

This function allows you to fetch the cheapest round-trip flight options for a specified region and origin airport.

#### Parameters

- **`region`**: The region code where you want to search for flights. See the **Region Codes** section below for details.
- **`origin`**: The airport code of the departure location (e.g., `LON` for London).

#### Returns

A list of flight options, including destination cities, prices, and currency.

#### Example

```python
from britishairways.api import BritishAirways

# Initialize the British Airways API client
ba = BritishAirways()

# Fetch the cheapest round-trip flights
region = "FEA"  # Far East and Australia
origin = "LON"  # London
try:
    results = ba.get_cheapest_round_trips(region=region, origin=origin)
    print("Cheapest Flights:", results)
except Exception as e:
    print(f"Error: {e}")
```

#### Sample Output

```json
[
    {
        "destination": "Hong Kong",
        "price": 690,
        "currency": "GBP",
        "departure": "LHR",
        "arrival": "HKG",
        "dates": {
            "outbound": "2025-01-01",
            "inbound": "2025-01-02"
        }
    },
    {
        "destination": "Singapore",
        "price": 593,
        "currency": "GBP",
        "departure": "LHR",
        "arrival": "SIN",
        "dates": {
            "outbound": "2025-01-03",
            "inbound": "2025-01-04"
        }
    }
]
```

---

## Region Codes

Below is a list of region codes supported by the `get_cheapest_round_trips` function:

| Region                            | Code              |
|-----------------------------------|-------------------|
| North America                     | `NOA`             |
| Latin America and Caribbean       | `SOA`             |
| Europe, UK, and Ireland           | `EUK`             |
| South and Central Asia            | `SAS`             |
| Middle East and Africa            | `MDE+OR+AFR`      |
| Far East and Australia            | `FEA`             |

---

## Dependencies

The package relies on the following libraries:
- `requests` for making HTTP requests.
- `urllib.parse` for URL encoding.

Install dependencies using:
```bash
pip install -r requirements.txt
```

---

## Contributing

We welcome contributions! Feel free to fork the repository and submit a pull request. For significant changes, please open an issue first to discuss what you would like to change.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Happy coding! 🎉