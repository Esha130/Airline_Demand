import streamlit as st
import pandas as pd
from scraper import fetch_flight_data
import plotly.express as px
from insights import (
    get_top_origin_countries,
    get_ground_vs_air,
    get_average_velocity_altitude,
)

# App Configuration
st.set_page_config(page_title="Airline Demand Trends", layout="wide")
st.title("✈️ Airline Booking Market Demand Tracker")

# Fetch Data
st.subheader("Real-time Flight Data (via OpenSky API)")
with st.spinner("Fetching data..."):
    df = fetch_flight_data()

if not df.empty:
    st.success(f"Fetched {len(df)} flights.")
    
    # -------------------------
    # Filter Section
    # -------------------------
    st.subheader("🔍 Filter Options")

    countries = df["origin_country"].dropna().unique()
    selected_country = st.selectbox("Select Origin Country", sorted(countries))
    filtered_df = df[df["origin_country"] == selected_country]

    status_option = st.radio("Flight Status", ["All", "Airborne", "On Ground"])
    if status_option == "Airborne":
        filtered_df = filtered_df[filtered_df["on_ground"] == False]
    elif status_option == "On Ground":
        filtered_df = filtered_df[filtered_df["on_ground"] == True]

    # -------------------------
    # Show Data Table
    # -------------------------
    st.write(f"📍 Flights from {selected_country}")
    st.dataframe(filtered_df)

    # -------------------------
    # Visualization
    # -------------------------
    st.subheader("📊 Flight Velocity vs Altitude")
    if not filtered_df.empty:
        fig = px.scatter(
            filtered_df,
            x="velocity",
            y="baro_altitude",
            color="on_ground",
            hover_data=["callsign", "origin_country"]
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No flight data available for selected filters.")

    # -------------------------
    # Insights Section
    # -------------------------
    st.subheader("📈 Flight Insights")

    # Ground vs Air
    status_df = get_ground_vs_air(filtered_df)
    st.write("🧭 Ground vs Airborne")
    st.bar_chart(status_df.set_index("status"))

    # Average Velocity and Altitude
    stats = get_average_velocity_altitude(filtered_df)
    col1, col2 = st.columns(2)
    col1.metric("Avg Velocity (m/s)", f"{stats['avg_velocity']:.2f}")
    col2.metric("Avg Altitude (m)", f"{stats['avg_altitude']:.2f}")

    # Top Origin Countries (from whole dataset, not just filtered)
    st.subheader("🌍 Top Origin Countries (Global)")
    top_countries = get_top_origin_countries(df)
    st.dataframe(top_countries)

else:
    st.warning("Could not fetch flight data. Please try again later.")
