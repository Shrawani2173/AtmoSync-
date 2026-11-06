# AtmoSync – Sensor Data Format

## 1. Overview
AtmoSync uses simulated IoT sensor data to monitor the storage conditions of avocado containers.

## 2. Data Format
Sensor readings are generated in JSON format.

## 3. Sample JSON

```json
{
  "container_id": "AVO_001",
  "sensor_id": "SEN_01",
  "timestamp": "2026-11-05T10:30:00Z",
  "temperature": 8.5,
  "humidity": 75.2,
  "vibration": 0.35
}
```

## 4. Field Description

| Field | Description |
|---|---|
| container_id | Unique container identifier |
| sensor_id | Unique sensor identifier |
| timestamp | Date and time of reading in UTC |
| temperature | Temperature in Celsius (°C) |
| humidity | Humidity percentage (%) |
| vibration | Vibration reading |

## 5. Purpose
This common JSON structure ensures that all team members use the same data format throughout the AtmoSync pipeline.

## 6. Data Pipeline
Python Sensor Simulator → Apache Kafka → Snowflake → dbt → Apache Superset
