import os
from crewai.tools import tool
from serpapi.google_search import GoogleSearch


@tool("hotel_search_tool")
def hotel_search_tool(city: str):
    """
    Search hotels in a city.
    """
    print(os.getenv("SERPAPI_API_KEY"))

    params = {
        "engine": "google_hotels",
        "q": f"hotels in {city}",
        "check_in_date": "2026-06-15",
        "check_out_date": "2026-06-18",
        "currency": "INR",
        "gl": "in",
        "hl": "en",
        "api_key": os.getenv("SERPAPI_API_KEY")
    }

    search = GoogleSearch(params)

    results = search.get_dict()

    hotels = results.get("properties", [])

    hotel_list = []

    for hotel in hotels[:5]:
        hotel_list.append({
            "name": hotel.get("name"),
            "rating": hotel.get("overall_rating"),
            "price": hotel.get("rate_per_night", {}).get("lowest")
        })

    return hotel_list


@tool("flight_search_tool")
def flight_search_tool(route: str):
    """
    Search flights.
    Format:
    Pune-BOM
    """

    try:
        departure, arrival = route.split("-")
    except:
        return "Format must be DEP-ARR e.g. ORD-BOM"

    params = {
        "engine": "google_flights",
        "departure_id": departure.strip(),
        "arrival_id": arrival.strip(),
        "outbound_date": "2026-06-15",
        "return_date": "2026-06-20",
        "currency": "USD",
        "hl": "en",
        "api_key": os.getenv("SERPAPI_API_KEY")
    }

    search = GoogleSearch(params)

    results = search.get_dict()

    flights = results.get("best_flights", [])

    flight_list = []

    for flight in flights[:5]:

        airline = ""

        if flight.get("flights"):
            airline = flight["flights"][0].get("airline")

        flight_list.append({
            "airline": airline,
            "price": flight.get("price")
        })

    return flight_list
