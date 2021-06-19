# Calculate cost of a multi day trip with flinkster and compare cost of different car categories
# taken from https://anmeldung.flinkster.de/de/fahrzeuge-und-tarife
car_rates = {
    "klein": {
        "hourly_day": 5.0,
        "hourly_nightly": 1.5,
        "first_day": 50.0,
        "more_days": 29.0,
        "per_km": 0.25,
    },
    "kompakt": {
        "hourly_day": 6.0,
        "hourly_nightly": 1.9,
        "first_day": 60.0,
        "more_days": 39.0,
        "per_km": 0.26,
    }
}

def calculateTimePriceDays(rates, duration):
    return rates["first_day"] + (rates["more_days"] * (duration - 1))

def calculateDistancePrice(rates, distanceInKilometers):
    return distanceInKilometers * rates["per_km"]

def calculateTripCost(car_category, days, distanceInKilometers):
    print(f'Trip cost for rate {car_category}, for {days} days and {distanceInKilometers} kilometers')
    rates = car_rates[car_category]
    print(calculateTimePriceDays(rates, days) + calculateDistancePrice(rates, distanceInKilometers))

calculateTripCost("klein", 3, 300)
calculateTripCost("kompakt", 3, 300)
