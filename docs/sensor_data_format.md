# AtmoSync – Sensor Data Format Documentation

## 1. Introduction

AtmoSync uses a standardized JSON data format to represent environmental readings collected from IoT sensors installed in avocado storage containers.

The common data structure ensures consistency and smooth communication between the Python sensor simulator, Apache Kafka, Snowflake, and other components of the system.

## 2. Sensor Data Structure

Each sensor reading is represented as a JSON object containing container identification, sensor identification, timestamp, and environmental measurements.

### Sample JSON Record

```json
{
    "container_id": "AVO_001",
    "sensor_id": "SEN_01",
    "timestamp": "2026-11-15T10:30:00Z",
    "temperature": 8.5,
    "humidity": 75.2,
    "vibration": 0.35
}
```

## 3. Field Description

| Field Name | Data Type | Description |
|---|---|---|
| container_id | String | Unique identifier of the storage container |
| sensor_id | String | Unique identifier of the sensor |
| timestamp | String (UTC) | Date and time when the reading is generated |
| temperature | Float | Temperature measurement in Celsius |
| humidity | Float | Humidity measurement in percentage |
| vibration | Float | Vibration measurement |

## 4. Sensor Identification

The system uses unique sensor IDs to distinguish readings from different sensors.

Example:
- SEN_01
- SEN_02
- SEN_03

Each reading is associated with the container in which the sensor is installed.

## 5. Data Generation

The Python sensor simulator generates sensor readings with the following parameters:

| Parameter | Generation Range |
|---|---|
| Temperature | 5°C – 15°C |
| Humidity | 60% – 90% |
| Vibration | 0.1 – 1.0 |

These are simulated project values used for development and testing.

## 6. Data Flow

1. Python generates sensor readings.
2. Each reading is structured as a JSON record.
3. The Kafka Producer publishes records to the `sensor_data` topic.
4. The Kafka Consumer retrieves the messages.
5. Sensor records are forwarded to Snowflake.
6. dbt transforms the stored data.
7. Apache Superset visualizes the processed information.

## 7. Importance of Standardized Data

- Maintains consistency across project components.
- Simplifies data exchange between producer and consumer.
- Makes data ingestion into Snowflake easier.
- Supports structured data transformation.
- Helps create reliable analytical dashboards.

## 8. Conclusion

The standardized JSON sensor data format provides a common structure for all AtmoSync components. It supports smooth integration between sensor data generation, Kafka streaming, cloud storage, data transformation, and visualization.
