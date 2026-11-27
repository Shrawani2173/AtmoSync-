
import random
import json
import os
import time
from datetime import datetime, timezone

def generate_sensor_reading(sensor_id):
    return {
        "container_id": "AVO_001",
        "sensor_id": sensor_id,
        "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "temperature": round(random.uniform(5, 15), 2),
        "humidity": round(random.uniform(60, 90), 2),
        "vibration": round(random.uniform(0.1, 1.0), 2)
    }

def generate_readings(total_readings):
    sensor_ids = ["SEN_01", "SEN_02", "SEN_03"]
    readings = []

    for i in range(total_readings):
        sensor_id = sensor_ids[i % len(sensor_ids)]
        reading = generate_sensor_reading(sensor_id)
        readings.append(reading)

        print(f"Reading {i + 1} generated")

        if i < total_readings - 1:
            time.sleep(2)

    return readings

def save_readings(readings, filename):
    folder = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(folder, filename)

    with open(file_path, "w") as file:
        json.dump(readings, file, indent=4)

    print("File saved at:", file_path)

def main():
    readings = generate_readings(10)

    print(json.dumps(readings, indent=4))
    save_readings(readings, "sample_output.json")

    print("\n10 sensor readings generated successfully!")

if __name__ == "__main__":
    main()
