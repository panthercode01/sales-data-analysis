
import streamlit as st
import pandas as pd

# Page settings
st.set_page_config(
    page_title="Gourav's Sales Data Analyst",
    page_icon="📊",
    layout="wide"
)

# Dashboard title
st.title("📊 Gourav's Sales Data Analyst")
st.write("Analyze your sales, revenue, and profit.")

# Load data
df = pd.read_csv("sales.csv")

# Calculate revenue and profit
df["revenue"] = df["quantity"] * df["unit_price"]

df["profit"] = df["quantity"] * (
    df["unit_price"] - df["unit_cost"]
)

# Sidebar filter
st.sidebar.header("Dashboard Filters")

products = st.sidebar.multiselect(
    "Select Products",
    options=df["product"].unique(),
    default=df["product"].unique()
)

# Filter data
filtered_df = df[df["product"].isin(products)]

# Calculate metrics
total_revenue = filtered_df["revenue"].sum()
total_profit = filtered_df["profit"].sum()
total_units = filtered_df["quantity"].sum()

profit_margin = (
    (total_profit / total_revenue) * 100
    if total_revenue > 0 else 0
)

# KPI cards
col1, col2, col3, col4 = st.columns(4)

col1.metric("💰 Total Revenue", f"₹{total_revenue:,.0f}")
col2.metric("📈 Total Profit", f"₹{total_profit:,.0f}")
col3.metric("📦 Units Sold", f"{total_units}")
col4.metric("📊 Profit Margin", f"{profit_margin:.2f}%")

st.divider()

# Product-wise analysis
st.subheader("📋 Product-wise Sales Analysis")

product_sales = filtered_df.groupby("product").agg(
    quantity=("quantity", "sum"),
    revenue=("revenue", "sum"),
    profit=("profit", "sum")
).reset_index()

st.dataframe(product_sales, use_container_width=True)

# Charts
left, right = st.columns(2)

with left:
    st.subheader("💰 Revenue by Product")
    st.bar_chart(
        product_sales.set_index("product")["revenue"]
    )

with right:
    st.subheader("📈 Profit by Product")
    st.bar_chart(
        product_sales.set_index("product")["profit"]
    )

# Business insights
st.divider()
st.subheader("💡 Automatic Business Insights")

if not product_sales.empty:
    best_revenue = product_sales.loc[
        product_sales["revenue"].idxmax(), "product"
    ]

    best_profit = product_sales.loc[
        product_sales["profit"].idxmax(), "product"
    ]

    best_selling = product_sales.loc[
        product_sales["quantity"].idxmax(), "product"
    ]

    st.write(f"🏆 **Highest Revenue:** {best_revenue}")
    st.write(f"💵 **Most Profitable:** {best_profit}")
    st.write(f"📦 **Most Units Sold:** {best_selling}")
else:
    st.info("Select at least one product to see insights.")

# Raw data
with st.expander("View Original Sales Data"):
    st.dataframe(filtered_df, use_container_width=True)

st.caption("Sales Data Analyst Project | Built with Python, Pandas & Streamlit")
