from crewai import Agent
from tools import hotel_search_tool, flight_search_tool


flight_agent = Agent(
    role="Flight Expert",
    goal="Find best flights",
    backstory="""
    A master of air travel who understands layovers, airline quality, and pricing trends.
    """,
    tools=[flight_search_tool],
    verbose=True
)

hotel_agent = Agent(
    role="Hotel Expert",
    goal="Find best hotels",
    backstory="""
    A specialist in finding the perfect accommodation, whether it's a luxury resort or a budget-friendly option.
    """,
    tools=[hotel_search_tool],
    verbose=True
)