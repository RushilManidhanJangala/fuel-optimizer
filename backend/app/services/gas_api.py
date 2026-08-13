def get_gas_prices(start: str, destination: str):
    # Simulating stations along route
    return [
        {"name": "Shell - Phoenix Exit", "price": 4.29, "detour_miles": 0.2},
        {"name": "Chevron - Highway 10", "price": 4.49, "detour_miles": 0.5},
        {"name": "Arco - Midway Stop", "price": 4.09, "detour_miles": 0.3},
        {"name": "Costco - Near LA", "price": 3.95, "detour_miles": 1.5},
        {"name": "Circle K - Border AZ/CA", "price": 4.15, "detour_miles": 0.4},
    ]