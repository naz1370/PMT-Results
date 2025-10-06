import streamlit as st
import matplotlib.pyplot as plt

def plot_pmt_data(data, selected_pmts):
    plt.figure(figsize=(10, 6))
    
    for serial_number in selected_pmts:
        pmt_data = data[serial_number]
        plt.plot(pmt_data['Wavelength'], pmt_data['LightResponse'], label=f'PMT {serial_number}')
    
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Light Response')
    plt.legend()
    st.pyplot(plt)
