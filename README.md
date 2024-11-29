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

This package is available on [PyPI](https://pypi.org/project/britishairways/). Install it directly using pip:

```bash
pip install britishairways
```

Or, clone the repository and install it locally:

```bash
git clone https://github.com/alexechoi/british-airways-py.git
cd british-airways-py
pip install .
```

---

## Usage

### Initialize the Client

Before using the package, initialize the `BritishAirways` client:

```python
from britishairways.api import BritishAirways

# Initialize the client
ba = BritishAirways()
```

---

### Functions

#### 1. **`get_one_way_price`**

Fetch the price for a one-way flight on a specific date.

**Parameters**:
- `origin` (str): The origin airport code (e.g., "LHR").
- `destination` (str): The destination airport code (e.g., "JFK").
- `departure_date` (str): The departure date in `YYYY-MM-DD` format.

**Example**:
```python
one_way_flight = ba.get_one_way_price(
    origin="LON",
    destination="NYC",
    departure_date="2024-12-15"
)
print(one_way_flight)
```

---

#### 2. **`get_specific_round_trip`**

Fetch details for a specific round trip, given a departure and return date.

**Parameters**:
- `origin` (str): The origin airport code (e.g., "LHR").
- `destination` (str): The destination airport code (e.g., "JFK").
- `departure_date` (str): The departure date in `YYYY-MM-DD` format.
- `return_date` (str): The return date in `YYYY-MM-DD` format.

**Example**:
```python
flights = ba.get_specific_round_trip(
    origin="LON",
    destination="NYC",
    departure_date="2024-12-15",
    return_date="2024-12-22"
)
print(flights)
```

---

#### 3. **`get_cheapest_round_trips`**

Fetch the cheapest round-trip flights for a given region and origin.

**Parameters**:
- `region` (str): The region code (e.g., "FEA").
- `origin` (str): The origin airport code (e.g., "LON").

**Example**:
```python
cheapest_flights = ba.get_cheapest_round_trips(region="FEA", origin="LON")
print(cheapest_flights)
```

---

#### 4. **`get_monthly_graphs`**

Retrieve monthly pricing data for a specific origin and destination.

**Parameters**:
- `origin` (str): The origin airport code (e.g., "LHR").
- `destination` (str): The destination airport code (e.g., "ATL").
- `trip_length` (int): The length of the trip in days (e.g., 7).

**Example**:
```python
monthly_graphs = ba.get_monthly_graphs(origin="LHR", destination="ATL", trip_length=7)
print(monthly_graphs)
```

---

#### 5. **`get_calendar_prices`**

Retrieve calendar-based pricing data for specific months, displaying daily flight prices.

**Parameters**:
- `origin` (str): The origin airport code (e.g., "LHR").
- `destination` (str): The destination airport code (e.g., "NYC").
- `trip_length` (int): The number of nights for the trip (e.g., 7).
- `months` (list): A list of months in `YYYYMM` format (e.g., `["202412", "202501"]`).

**Example**:
```python
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