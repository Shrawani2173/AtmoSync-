# AtmoSync - Sensor Data Format

## Project Overview
This document defines the common JSON format used for simulated IoT sensor readings.

## Sensor Parameters
- Temperature: Temperature inside the avocado container (°C).
- Humidity: Humidity inside the container (%).
- Vibration: Vibration level detected by the sensor.

## JSON Data Structure

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

## Field Description

| Field | Data Type | Description |
|---|---|---|
| container_id | String | Unique container ID |
| sensor_id | String | Unique sensor ID |
| timestamp | String | Date and time of reading in UTC |
| temperature | Float | Temperature in °C |
| humidity | Float | Humidity percentage |
| vibration | Float | Vibration reading |

## Data Flow
Python Simulator → Kafka → Snowflake → dbt → Apache Superset
