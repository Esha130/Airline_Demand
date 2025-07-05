import pandas as pd

def get_top_origin_countries(df, top_n=10):
    """Returns top N countries with most flights"""
    return (
        df['origin_country']
        .value_counts()
        .head(top_n)
        .reset_index()
        .rename(columns={'index': 'country', 'origin_country': 'flight_count'})
    )


def get_ground_vs_air(df):
    """Returns count of flights on ground vs airborne"""
    if df.empty or "on_ground" not in df.columns:
        # Return an empty DataFrame with the correct columns
        return pd.DataFrame({"status": [], "count": []})

    # Count True/False values
    counts = df["on_ground"].value_counts()

    # Convert to DataFrame manually to ensure proper format
    status_labels = {True: "On Ground", False: "Airborne"}
    status_list = [status_labels.get(key, str(key)) for key in counts.index]
    result_df = pd.DataFrame({
        "status": status_list,
        "count": counts.values
    })

    return result_df


def get_average_velocity_altitude(df):
    """Returns average velocity and altitude of flights"""
    return {
        "avg_velocity": df["velocity"].mean() if not df.empty else 0,
        "avg_altitude": df["baro_altitude"].mean() if not df.empty else 0
    }
