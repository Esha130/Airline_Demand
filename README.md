# ✈️ Airline Booking Market Demand Tracker

A real-time interactive web app built using Python and Streamlit to visualize airline market demand trends using publicly available flight data. The app helps identify popular routes, monitor flight activity, and extract insights from real-time air traffic data.

---

## 📌 Project Objective

This app was built as part of a technical evaluation to demonstrate skills in:

- Python programming
- API integration and data scraping
- Data analysis and processing
- Interactive web development (Streamlit)
- Data visualization and dashboarding

---

## 🔍 Features

- ✅ Fetches **live flight data** from the OpenSky Network API
- ✅ Allows users to:
  - Filter by **origin country**
  - Filter by **flight status** (Airborne / On Ground / All)
- ✅ Generates insights:
  - Top flight-originating countries
  - Count of airborne vs grounded flights
  - Average flight velocity and altitude
- ✅ Visualizes:
  - Real-time flight data table
  - Scatter plot (Velocity vs Altitude)
  - Bar chart for flight status breakdown

---

## 🖥️ Tech Stack

| Layer            | Tools Used                 |
|------------------|----------------------------|
| Language         | Python 3                   |
| Web Framework    | Streamlit                  |
| API Source       | OpenSky Network API        |
| Data Processing  | Pandas, Requests           |
| Visualization    | Plotly, Streamlit Charts   |
| Deployment       | Streamlit Cloud / Local    |

---

## 📂 Project Structure

```

airline-demand-tracker/
├── app.py             # Main Streamlit app
├── scraper.py         # Fetches real-time flight data from OpenSky API
├── insights.py        # Functions for insights and analytics
├── requirements.txt   # List of required Python packages
└── README.md          # Project documentation

````

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/airline-demand-tracker.git
cd airline-demand-tracker
````

### 2. Create Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate     # For macOS/Linux
# OR
venv\Scripts\activate        # For Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
streamlit run app.py
```

---

## 📊 Sample Output

### 🔹 Filter Options

* Select origin country from dropdown
* Choose flight status: All / Airborne / On Ground

### 🔹 Visuals & Insights

* Bar chart of Ground vs Airborne flights
* Scatter plot: Velocity vs Altitude
* Metrics: Average velocity and altitude
* Top countries with most flights (global)

---

## 🌐 Live Demo

> Once deployed on Streamlit Cloud, add your link here:

**🔗 [Open Live App][(https://airlinedemand.streamlit.app/)]**


## 🧠 About the Developer

**Esha Gowani**
📫 \[eshagowani@gmail.com]
🔗 \[LinkedIn Profile (optional)]
🌍 [Portfolio / GitHub](https://github.com/Esha130)

---

## 📝 License

This project is intended for evaluation and educational use.

````


### ✅ What You Should Do Now

1. Create a new file in your project:  
   `airline-demand-tracker/README.md`

2. Paste the above content in full.

3. Replace the placeholders:
   - `https://github.com/your-username/...`
   - `https://your-streamlit-app-url.streamlit.app`
   - `[Your Email]`, `[LinkedIn]`

4. Add and push:
```bash
git add README.md
git commit -m "Added professional README"
git push origin main
