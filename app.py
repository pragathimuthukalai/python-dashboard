import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title("📊 Sales Dashboard")

# Load data
df = pd.read_csv("sales_data.csv")

# Sidebar filter
region = st.sidebar.selectbox("Select Region", df["Region"].unique())
filtered_df = df[df["Region"] == region]

# Show data
st.subheader("Filtered Data")
st.dataframe(filtered_df)

# Total sales
total_sales = filtered_df["Sales"].sum()
st.metric("Total Sales", total_sales)

# Sales by product
fig1 = px.bar(filtered_df, x="Product", y="Sales", color="Product",
              title="Sales by Product")
st.plotly_chart(fig1)

# Profit trend
fig2 = px.line(filtered_df, x="Date", y="Profit",
               title="Profit Over Time")
st.plotly_chart(fig2)

# Quantity pie chart
fig3 = px.pie(filtered_df, names="Product", values="Quantity",
              title="Product Quantity Share")
st.plotly_chart(fig3)