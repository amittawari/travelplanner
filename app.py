import streamlit as st
from dotenv import load_dotenv
from crew_setup import create_travel_crew

# Load environment variables
load_dotenv()

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="🌍",
    layout="wide"
)

# -----------------------------
# Header
# -----------------------------
st.title("🌍 AI Travel Planner")
st.markdown("Plan Flights and Hotels using AI Agents")

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.header("Travel Details")

    city = st.text_input(
        "Destination City",
        value="Mumbai"
    )

    departure_airport = st.text_input(
        "Departure Airport Code",
        value="ORD"
    )

    arrival_airport = st.text_input(
        "Arrival Airport Code",
        value="BOM"
    )

    generate_btn = st.button(
        "🚀 Generate Travel Plan",
        use_container_width=True
    )

# -----------------------------
# Generate Plan
# -----------------------------
if generate_btn:

    with st.spinner("AI Agents are planning your trip..."):

        try:

            crew = create_travel_crew(
                city=city,
                departure_airport=departure_airport,
                arrival_airport=arrival_airport
            )

            result = crew.kickoff()

            st.success("✅ Travel Plan Generated Successfully")

            # ----------------------------------
            # Flights
            # ----------------------------------
            if len(result.tasks_output) > 0:

                st.markdown("---")
                st.subheader("✈️ Flight Recommendations")

                with st.container(border=True):
                    st.markdown(result.tasks_output[0].raw)

            # ----------------------------------
            # Hotels
            # ----------------------------------
            if len(result.tasks_output) > 1:

                st.markdown("---")
                st.subheader("🏨 Hotel Recommendations")

                with st.container(border=True):
                    st.markdown(result.tasks_output[1].raw)

        except Exception as ex:

            st.error("Error generating travel plan")
            st.exception(ex)

# -----------------------------
# Initial Page
# -----------------------------
else:

    st.info(
        """
        Enter travel details in the sidebar and click
        **Generate Travel Plan**.
        """
    )
