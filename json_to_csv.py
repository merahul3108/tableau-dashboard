import json
import csv

# Load JSON file
with open("daikibo-telemetry-data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Create CSV file
with open("daikibo_telemetry.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)

    # Header
    writer.writerow([
        "deviceID",
        "deviceType",
        "timestamp",
        "factory",
        "status",
        "unhealthy"
    ])

    # Rows
    for record in data:
        status = record["data"]["status"].lower()
        unhealthy = 10 if status == "unhealthy" else 0

        writer.writerow([
            record["deviceID"],
            record["deviceType"],
            record["timestamp"],
            record["location"]["factory"],
            status,
            unhealthy
        ])

print("CSV file created successfully!")
