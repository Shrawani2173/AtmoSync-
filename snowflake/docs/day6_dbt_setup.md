# Day 6: dbt Setup (Ashraf)

## Task
Install dbt Core and connect it to Snowflake.

## Done
- Installed dbt-core and dbt-snowflake (pip)
- Created dbt project in snowflake_dbt/
- Created DBT_ROLE with access to ATMOSYNC_DB (read RAW, write STAGING and ANALYTICS)
- Configured profiles.yml locally (not committed)
- `dbt debug` passed: all checks passed

## Connection settings (no secrets)
- Account: TJBRGSZ-RX49654
- Warehouse: ATMOSYNC_WH
- Database: ATMOSYNC_DB
- Role: DBT_ROLE
- Target schema: STAGING

## Next (Day 7)
- Write staging models to parse raw JSON from IOT_SENSOR_RAW
