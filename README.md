# IoT Cloud Monitoring Dashboard using ESP32, MQTT, FastAPI & Supabase

## Overview

This project is a complete cloud-based IoT monitoring system built using ESP32 (Wokwi simulation), MQTT communication, Python FastAPI backend, Supabase cloud database, and a web dashboard deployed on Render.

The system collects temperature and humidity data from a DHT22 sensor connected to ESP32, sends the data through MQTT, stores it in a cloud PostgreSQL database, and visualizes it through a live dashboard accessible from any device.

---

## Project Architecture

ESP32 (Wokwi + DHT22)
↓ MQTT Publish
HiveMQ Public Broker
↓ MQTT Subscriber (Python)
FastAPI Backend + MQTT Bridge
↓
Supabase PostgreSQL Cloud Database
↓
FastAPI API + Dashboard
↓
Render Cloud Deployment
↓
Live Web Dashboard

---

## Features

* ESP32 IoT device simulation using Wokwi
* DHT22 temperature and humidity sensing
* MQTT publish-subscribe communication
* JSON sensor payload transmission
* Python MQTT subscriber using Paho MQTT
* Cloud PostgreSQL database using Supabase
* FastAPI backend APIs
* Historical sensor data storage
* Interactive dashboard UI
* Cloud deployment using Render
* Accessible from desktop and mobile devices

---

## Tech Stack

### Embedded / IoT

* ESP32
* DHT22
* Wokwi Simulator
* MQTT Protocol
* HiveMQ Broker

### Backend

* Python
* FastAPI
* Paho MQTT
* Psycopg2

### Database

* Supabase PostgreSQL

### Frontend

* HTML
* CSS
* JavaScript
* Chart.js

### Deployment

* Render Cloud Platform
* GitHub

---

## Folder Structure

```text
iot_backend/
│
├── main.py
├── mqtt_to_supabase.py
├── mqtt_subscriber.py
├── requirements.txt
├── Procfile
├── templates/
│   └── dashboard.html
└── README.md
```

## MQTT Topic

```text
dillip/home/sensor
```

Example MQTT JSON payload:

```json
{
  "temperature": 24.00,
  "humidity": 40.00
}
```

---

## API Endpoints

### Home

```text
/
```

Returns API status.

---

### Latest Sensor Data

```text
/latest
```

Returns latest temperature and humidity values.

---

### Sensor History

```text
/history
```

Returns recent sensor data records.

---

### Dashboard

```text
/dashboard
```

Displays web-based monitoring dashboard.

---

## Local Setup

### Clone Repository

```bash
git clone https://github.com/dillip-dev606/iot-dashboard.git
cd iot-dashboard
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run FastAPI

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000/dashboard
```

---

## Cloud Deployment

This project is deployed using Render and connected to Supabase PostgreSQL cloud database.

Live Deployment:

(Add Render URL here)

---

## Learning Outcomes

This project helped in understanding:

* MQTT publish-subscribe architecture
* IoT cloud communication
* ESP32 data acquisition
* JSON payload handling
* Python backend development
* REST API creation
* Cloud database integration
* Full-stack IoT deployment
* GitHub and cloud hosting workflow

---

## Future Improvements

* Real-time WebSocket dashboard
* Telegram / Email alerts
* Multi-device monitoring
* Device online/offline detection
* Authentication and login system
* Mobile application integration

---

## Author

**Dillip Prasad**
Electronics and Communication Engineering
IoT | Embedded Systems | Cloud Integration
