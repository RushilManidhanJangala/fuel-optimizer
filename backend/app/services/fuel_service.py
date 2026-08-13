from app.services.gas_api import get_gas_prices


def calculate_recommendation(mpg: float, gallons: float, start: str, destination: str):
    stations = get_gas_prices(start, destination)

    results = []

    for station in stations:
        fuel_cost = station["price"] * gallons
        extra_gallons = station["detour_miles"] / mpg
        extra_cost = extra_gallons * station["price"]
        total_cost = fuel_cost + extra_cost

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
        "best_value": best_value,
        "cheapest": cheapest,
        "most_convenient": most_convenient,
        "all_options": sorted(results, key=lambda x: x["total_cost"])
    }