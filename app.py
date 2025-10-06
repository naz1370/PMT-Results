import streamlit as st
from data_loader import load_data
from plot_utils import plot_pmt_data

# Load the data once
data = load_data()

st.title("PMT Data Visualization")

# Select up to 10 PMTs
selected_pmts = st.multiselect("Choose PMTs", options=list(data.keys()), default=list(data.keys())[:10])

# Plot button
if st.button("Plot Data"):
    if selected_pmts:
        plot_pmt_data(data, selected_pmts)
    else:
        st.write("Please select at least one PMT.")
