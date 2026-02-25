import streamlit as st
from datetime import datetime
import requests
import pandas as pd

API_URL = "http://127.0.0.1:9000"


def analytics_months_tab():

    st.title("Monthly Expense Analysis")

    # 🔹 Year Dropdown (2000–2050)
    year = st.selectbox(
        "Select Year",
        options=list(range(2000, 2051)),
        index=list(range(2000, 2051)).index(datetime.today().year)
    )

    # 🔹 Multi-select Month Dropdown
    months_dict = {
        1: "January", 2: "February", 3: "March", 4: "April",
        5: "May", 6: "June", 7: "July", 8: "August",
        9: "September", 10: "October", 11: "November", 12: "December"
    }

    selected_months = st.multiselect(
        "Select Month(s)",
        options=list(months_dict.keys()),
        format_func=lambda x: months_dict[x]
    )

    # 🔹 View Analysis Button
    if st.button("View Analysis"):

        if not selected_months:
            st.warning("Please select at least one month.")
            return

        payload = {
            "year": year,
            "months": selected_months
        }

        response = requests.post(f"{API_URL}/monthly_summary/", json=payload)

        if response.status_code != 200:
            st.error("Failed to retrieve monthly summary.")
            return

        monthly_summary = response.json()

        if not monthly_summary:
            st.info("No data found for selected filters.")
            return

        # 🔹 Convert to DataFrame
        df = pd.DataFrame(monthly_summary)

        df.rename(columns={
            "expense_month": "Month Number",
            "month_name": "Month Name",
            "total": "Total"
        }, inplace=True)

        df_sorted = df.sort_values(by="Month Number")
        df_sorted.set_index("Month Name", inplace=True)

        # 🔹 Bar Chart
        st.bar_chart(df_sorted["Total"], use_container_width=True)

        # 🔹 Format Total column
        df_sorted["Total"] = df_sorted["Total"].map("{:.2f}".format)

        st.table(df_sorted)
