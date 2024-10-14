from flask import Flask
from prometheus_client import Gauge, generate_latest
import pandas as pd
import time

app = Flask(__name__)

# Create a Gauge metric for CPU utilization
cpu_utilization_gauge = Gauge('cpu_utilization', 'CPU Utilization', ['index'])
# Create a Gauge metric for upper threshold
upper_threshold_gauge = Gauge('cpu_upper_threshold', 'Upper Threshold for CPU Utilization', ['index'])
# Create a Gauge metric for EWMA of CPU utilization
ewma_gauge = Gauge('cpu_ewma_utilization', 'EWMA of CPU Utilization', ['index'])

def load_data(file_path):
    data = pd.read_csv(file_path)
    print("Available columns in data:", data.columns.tolist())
    
    if 'Date' not in data.columns or 'Timestamp' not in data.columns:
        raise KeyError("The 'Date' or 'Timestamp' column is missing from the data.")
    
    data['DateTime'] = pd.to_datetime(data['Date'] + ' ' + data['Timestamp'], errors='coerce')
    
    if data['DateTime'].isna().any():
        print("Warning: Some 'DateTime' values could not be converted. They will be removed.")
    
    data = data.dropna(subset=['DateTime'])
    data = data.set_index('DateTime')
    data['CPU_Utilization'] = pd.to_numeric(data['CPU_Utilization'], errors='coerce')
    
    print(f"Data range: {data.index.min()} to {data.index.max()}")
    return data

def calculate_anomalies(data):
    data['CPU_Utilization'] = pd.to_numeric(data['CPU_Utilization'], errors='coerce')
    data = data.dropna(subset=['CPU_Utilization'])
    
    # Calculate rolling window for EWMA
    data['EWMA'] = data['CPU_Utilization'].ewm(span=10, adjust=False).mean()  # Adjust span as needed
    
    # Calculate upper threshold
    std_dev = data['CPU_Utilization'].std()
    data['Upper_Threshold'] = data['EWMA'] + 1 * std_dev
    
    # Identify anomalies
    data['Anomaly'] = data['CPU_Utilization'] > data['Upper_Threshold']
    
    return data

def update_metrics():
    file_path = 'synthetic_data.csv'  # Update this path if necessary
    data = load_data(file_path)
    data = calculate_anomalies(data)

    while True:
        for index, row in data.iterrows():
            cpu_util = row['CPU_Utilization']
            upper_threshold = row['Upper_Threshold']
            ewma_value = row['EWMA']

            # Set metrics
            cpu_utilization_gauge.labels(index=str(index)).set(cpu_util)
            upper_threshold_gauge.labels(index=str(index)).set(upper_threshold)
            ewma_gauge.labels(index=str(index)).set(ewma_value)

            print(f'Sent CPU Utilization: {cpu_util}, EWMA: {ewma_value}, Upper Threshold: {upper_threshold} for index: {index}')
            time.sleep(30)

@app.route('/metrics')
def metrics():
    return generate_latest()

if __name__ == '__main__':
    # Start updating metrics in a separate thread
    import threading
    threading.Thread(target=update_metrics, daemon=True).start()
    
    app.run(host='0.0.0.0', port=8001)
