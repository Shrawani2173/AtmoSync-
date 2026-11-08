# Apache Kafka Basics

## 1. What is Apache Kafka?
Apache Kafka is a distributed event streaming platform used to transfer data between different applications in real time.

## 2. Important Kafka Components

- **Producer:** Sends data to Kafka.
- **Broker:** Receives and manages messages.
- **Topic:** A category where messages are stored.
- **Consumer:** Reads messages from a topic.

## 3. Kafka Workflow in AtmoSync

1. Python generates simulated sensor readings.
2. Kafka Producer sends sensor data.
3. Kafka Broker receives the data.
4. Data is stored in the `sensor_readings` topic.
5. Kafka Consumer reads the messages.
6. Data is forwarded to Snowflake for storage and analysis.

## 4. Role of Kafka in AtmoSync

Kafka helps transfer sensor readings from the Python simulator to the data storage system. It supports continuous data streaming and connects different parts of our project.

## 5. Project Data Fields

- container_id
- sensor_id
- timestamp
- temperature
- humidity
- vibration
