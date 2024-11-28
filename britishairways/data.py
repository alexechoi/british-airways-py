# data.py

# Supported regions and their codes
REGIONS = {
    "Europe": "EUR",
    "Asia": "AS",
    "North America": "NA",
    "South America": "SA",
    "Australia": "AU",
    "Africa": "AF"
}

# Example airports for each region (expand as needed)
DESTINATIONS = {
    "EUR": ["LHR", "CDG", "FRA"],
    "AS": ["HKG", "SIN", "NRT"],
    "NA": ["JFK", "LAX", "ORD"],
    "SA": ["GRU", "EZE"],
    "AU": ["SYD", "MEL"],
    "AF": ["CPT", "JNB"]
}

# Supported cabin classes
CABINS = ["Economy", "Premium Economy", "Business", "First"]