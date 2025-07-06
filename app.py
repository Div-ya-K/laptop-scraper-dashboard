import streamlit as st
import pandas as pd

# Load CSV
df = pd.read_csv("laptops_combined.csv")

st.title("🛍️ Laptop Scraper Dashboard")
st.markdown("""
This dashboard displays laptop data scraped from the test e-commerce site  
[**webscraper.io**](https://webscraper.io/test-sites/e-commerce/static/computers/laptops), which is publicly available for learning and practicing web scraping.

Data includes laptop title, price, description, and rating across multiple pages.
""")
csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="⬇️ Download CSV",
    data=csv,
    file_name='laptops_combined.csv',
    mime='text/csv',
)

# Price Filter
max_price = st.slider("Select Maximum Price", 
                      int(df['Price'].min()), 
                      int(df['Price'].max()), 
                      int(df['Price'].max()))

# Rating Filter
min_rating = st.slider("Minimum Rating (Stars)", 0, 5, 0)

# Apply Filters
filtered_df = df[(df['Price'] <= max_price) & (df['Rating'] >= min_rating)]

# Show Data
st.subheader(f"Showing {len(filtered_df)} Laptops")
st.dataframe(filtered_df)


st.subheader("📊 Average Price by Rating")
avg_price_by_rating = df.groupby("Rating")["Price"].mean().reset_index()
st.bar_chart(avg_price_by_rating.set_index("Rating"))
