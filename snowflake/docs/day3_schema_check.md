# Day 3: Table Schema Check (Ashraf)

## Task
Check table schema.

## Checked tables
- ATMOSYNC_DB.RAW.IOT_SENSOR_RAW: RECORD_CONTENT (VARIANT), RECORD_METADATA (VARIANT)
- ATMOSYNC_DB.RAW.IOT_SENSOR_READINGS: container_id, sensor_id, event_timestamp, temperature, humidity, vibration, location, loaded_at
- ATMOSYNC_DB.RAW.COMMODITY_PRICES_RAW: commodity, market, price, price_date, loaded_at

## Result
- Schema matches the sensor data format JSON
- Ready for the Kafka connector (Day 3) and the end-to-end test (Day 4)

## Next (Day 4)
- Fix load and schema bugs found in the end-to-end test
