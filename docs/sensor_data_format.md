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
  "vibration": 0.35,
  "location": "Mumbai Port"
}
```

## 4. Field Description

| Field | Type | Description |
|---|---|---|
| container_id | string | Unique container identifier |
| sensor_id | string | Unique sensor identifier |
| timestamp | string | Date and time of reading in UTC (ISO 8601, ends with Z) |
| temperature | number | Temperature in Celsius (°C) |
| humidity | number | Humidity percentage (%) |
| vibration | number | Vibration reading |
| location | string | Current location of the container (port or city name) |

## 5. Purpose
This common JSON structure ensures that all team members use the same data format throughout the AtmoSync pipeline. The `location` field is used to match a container to nearby secondary markets when calculating Spoilage Arbitrage.

## 6. Data Pipeline
Python Sensor Simulator → Apache Kafka → Snowflake → dbt → Apache Superset
