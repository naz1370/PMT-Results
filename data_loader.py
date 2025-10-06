import pandas as pd

def load_data():
    df = pd.read_excel('pmt_data.xlsx')

    data = {}
    for serial_number in df['SerialNumber'].unique():
        data[serial_number] = df[df['SerialNumber'] == serial_number]
    
    return data
