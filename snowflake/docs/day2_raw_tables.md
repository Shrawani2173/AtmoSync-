# Day 2: RAW Tables (Ashraf)

## Task
Create RAW tables in Snowflake.

## Database details
- Warehouse: ATMOSYNC_WH
- Database: ATMOSYNC_DB
- Schema: RAW

## Tables created

| Table | Purpose |
|---|---|
| IOT_SENSOR_RAW | Kafka connector loads the full JSON here (RECORD_CONTENT, RECORD_METADATA) |
| IOT_SENSOR_READINGS | One column per sensor field, used for checking data |
| COMMODITY_PRICES_RAW | Commodity price data (loaded on Day 5) |

## IOT_SENSOR_READINGS columns

| Column | Type | JSON field |
|---|---|---|
| CONTAINER_ID | VARCHAR | container_id |
| SENSOR_ID | VARCHAR | sensor_id |
| EVENT_TIMESTAMP | TIMESTAMP_TZ | timestamp (UTC) |
| TEMPERATURE | FLOAT | temperature (°C) |
| HUMIDITY | FLOAT | humidity (%) |
| VIBRATION | FLOAT | vibration |
| LOCATION | VARCHAR | location |
| LOADED_AT | TIMESTAMP_NTZ | added by Snowflake |

## Files
- SQL script: snowflake/setup/02_create_raw_tables.sql

## Next (Day 3)
- Check table schema
- Kafka connector loads data into IOT_SENSOR_RAW
