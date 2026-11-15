
import random
import json
from datetime import datetime, timezone

sensor_readings = []

for i in range(5):

    data = {
        "container_id": "AVO_001",
        "sensor_id": "SEN_01",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "temperature": round(random.uniform(5, 15), 2),
        "humidity": round(random.uniform(60, 90), 2),
        "vibration": round(random.uniform(0.1, 1.0), 2)
    }

    sensor_readings.append(data)

# Display readings in JSON format
print(json.dumps(sensor_readings, indent=4))

# Save readings into a JSON file
with open("sample_output.json", "w") as file:
    json.dump(sensor_readings, file, indent=4)

print("\n5 sensor readings generated successfully!")
