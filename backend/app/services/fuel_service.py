from app.services.gas_api import get_gas_prices


def calculate_recommendation(mpg, gallons, start, destination):
    stations = get_gas_prices(start, destination)

    results = []

    for station in stations:
        total_cost = station["price"] * gallons + (station["detour_miles"] * 0.1)

        results.append({
            "name": station["name"],
            "price": station["price"],
            "detour_miles": station["detour_miles"],
            "total_cost": round(total_cost, 2)
        })

    best_value = min(results, key=lambda x: x["total_cost"])
    cheapest = min(results, key=lambda x: x["price"])
    most_convenient = min(results, key=lambda x: x["detour_miles"])

    return {
        "route": {
            "start": start,
            "destination": destination
        },
        "inputs": {
            "mpg": mpg,
            "gallons": gallons
        },
        "best_value": best_value,
        "cheapest": cheapest,
        "most_convenient": most_convenient,
        "all_options": results
    }