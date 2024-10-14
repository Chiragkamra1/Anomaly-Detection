# CPU Utilization Anomaly Detection System

## Overview

This project implements a CPU utilization anomaly detection system using a Flask application and integrates with Prometheus for monitoring and alerting. The application leverages Exponentially Weighted Moving Average (EWMA) to dynamically calculate thresholds based on historical CPU utilization data. When CPU utilization exceeds these thresholds, alerts are triggered, which are then sent to Microsoft Teams via Power Automate.

## Project Structure

```
/YourProjectDirectory
│
 /flask_app
        app.py                      # Your Flask application code
        synthetic_data.csv          # Your CSV data file
        Dockerfile                   # Dockerfile for your Flask application
        requirements.txt             # Python package dependencies
    /prometheus_config
        prometheus.yml              # Prometheus configuration file
        alerts.rules.yml             # Prometheus alert rules file
        alertmanager.yml             # Alertmanager configuration file
        docker-compose.yml            # Docker Compose configuration file
```

## Features

- **Anomaly Detection:** Utilizes the EWMA method to calculate dynamic thresholds based on historical data for CPU utilization.
- **Metrics Exposure:** The application exposes CPU utilization, upper thresholds, and EWMA metrics to Prometheus.
- **Alerting System:** Integrates with Prometheus Alertmanager to send alerts to Microsoft Teams when CPU utilization exceeds defined thresholds.
- **Data Handling:** Loads CPU utilization data from a CSV file, processes it, and updates Prometheus metrics accordingly.

##Project Description

This project implements an anomaly detection system for monitoring CPU utilization in real-time 
using a Flask application, Prometheus, and Alertmanager. It dynamically calculates 
adaptive thresholds based on historical CPU usage patterns using the Exponentially Weighted Moving 
Average (EWMA) method. By scraping metrics through Prometheus, the application identifies
 anomalies when CPU utilization exceeds calculated thresholds.

The system is integrated with Microsoft Teams via Power Automate for alert notifications, 
enabling quick responses to critical CPU utilization events. The architecture employs Docker
 for containerization, ensuring portability and ease of deployment across different environments.

Key features of the project include:

Dynamic Thresholding: Utilizes historical data to adjust alert thresholds without manual intervention.
Real-time Monitoring: Continuously scrapes and updates CPU utilization metrics.
Alerting System: Sends alerts to Microsoft Teams based on CPU utilization anomalies.
Graphical Visualization: Provides insights into CPU utilization trends using Grafana.

## Getting Started

### Prerequisites

- **Docker:** Ensure that Docker and Docker Compose are installed on your machine.
- **Python:** The Flask application requires Python 3.x and the necessary packages listed in `requirements.txt`.

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Chiragkamra1/Anomaly-Detection.git
   cd YourProjectDirectory
   ```

2. **Build the Docker Image:**
   ```bash
   docker-compose build
   ```

3. **Run the Application:**
   ```bash
   docker-compose up
   ```

4. **Access the Application:**
   The Flask application will be accessible at `http://localhost:8001/metrics`.

### Configuration

- **Prometheus Configuration:** Update `prometheus.yml` to set the scrape targets, including the Flask application metrics endpoint.
- **Alert Rules:** Modify `alerts.rules.yml` to configure alerting rules based on the EWMA thresholds and CPU utilization metrics.

## Conclusion

This project demonstrates the integration of machine learning concepts with real-time monitoring and alerting using Prometheus and Microsoft Teams. The dynamic nature of the threshold calculation ensures that alerts are relevant and timely, providing effective monitoring for CPU utilization anomalies.

Feel free to explore the code and modify it to suit your requirements!
