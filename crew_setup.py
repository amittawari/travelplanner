from crewai import Task, Crew, Process
from agents import flight_agent, hotel_agent

def create_travel_crew(city, departure_airport, arrival_airport):

    flight_task = Task(
        description=f"""
        Search best flights from
        {departure_airport}
        to
        {arrival_airport}
        """,
        expected_output="""
        Top flight options with airline and price.
        """,
        agent=flight_agent
    )

    hotel_task = Task(
        description=f"""
        Find top hotels in {city}
        """,
        expected_output="""
        Top hotels with price and rating.
        """,
        agent=hotel_agent
    )

    crew = Crew(
        agents=[
            flight_agent,
            hotel_agent
        ],
        tasks=[
            flight_task,
            hotel_task
        ],
        process=Process.sequential,
        verbose=True
    )

    return crew