---
title: Connect to Warehouse
---

## Recce OSS
If you use the open source setup, you can connect to your warehouse the same way as dbt. No additional settings need to be configured. Recce uses the dbt library with your profiles to connect to your warehouse.


## Recce Cloud
If you use Recce Cloud, here are the warehouse connection settings. We currently support:

- Snowflake
- Databricks


### Snowflake
We only support password-based authentication.

Field | Description | Examples
----|------|----
`account` | The Snowflake account to connect to | `xxxxxx.us-central1.gcp`
`database` | The default database to connect to | `MYDB`
`schema` | The default schema to connect to | `PUBLIC`
`warehouse` | The warehouse to use when running queries | `WH_LOAD`
`user` | The user to log in as | `MYUSER`
`password` | The password for the user | `MYPASS`


### Databricks

We only support token-based authentication.

Field | Description | Examples
----|------|----
`host` | The hostname of your cluster | `YOURORG.databrickshost.com`
`http_path` | The HTTP path to your SQL Warehouse or all-purpose cluster | `/SQL/YOUR/HTTP/PATH`
`catalog` | The catalog used to connect to the warehouse. This is optional if you are using Unity Catalog | `MY_CATALOG`
`schema` | The default schema to connect to | `MY_SCHEMA`
`token` | The Personal Access Token (PAT) to connect to Databricks | `dapiXXXXXXXXXXXXXXXXXXXXXXX`
