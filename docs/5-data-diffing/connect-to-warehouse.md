---
title: Connect to Warehouse
---

## Recce OSS
Recce OSS supports all warehouses that dbt supports. It uses the same configuration as dbt, simply use your existing dbt profiles to connect to your warehouse. No additional setup required.

## Recce Cloud
If you use Recce Cloud, here are the warehouse connection settings. We currently support:

- [Snowflake](#snowflake)
- [Databricks](#databricks)
- [BigQuery](#bigquery)
- [Redshift](#redshift)

Others are coming in future releases

### Security

Recce Cloud protects all warehouse connection config (such as passwords, tokens, and private keys) using envelope encryption with AWS KMS. Credentials are encrypted at rest using AES-256, with encryption keys managed by AWS KMS. Decrypted credentials exist only in memory during connection establishment and are never written to disk. AWS KMS keys rotate automatically every 365 days to maintain security best practices.

### Snowflake
We support two authentication methods for Snowflake:

- **User & Password**: Traditional username and password authentication
- **Key Pair**: More secure authentication using RSA key pairs

#### Common Fields

| Field       | Description                               | Examples                 |
| ----------- | ----------------------------------------- | ------------------------ |
| `account`   | The Snowflake account to connect to       | `xxxxxx.us-central1.gcp` |
| `database`  | The default database to connect to        | `MY_DB`                   |
| `schema`    | The default schema to connect to          | `PUBLIC`                 |
| `warehouse` | The warehouse to use when running queries | `WH_LOAD`                |

#### User & Password Authentication

| Field      | Description               | Examples |
| ---------- | ------------------------- | -------- |
| `user`     | The user to log in as     | `MY_USER` |
| `password` | The password for the user | `MY_PASS` |

#### Key Pair Authentication

| Field                    | Description                                                                     | Required |
| ------------------------ | ------------------------------------------------------------------------------- | -------- |
| `user`                   | The user to log in as                                                           | Yes      |
| `private_key`            | Your RSA private key in PEM format or Base64-encoded DER format                 | Yes      |
| `private_key_passphrase` | Passphrase for the private key (only required if your private key is encrypted) | No       |

For more information on setting up key pair authentication, refer to [Snowflake's key pair authentication documentation](https://docs.snowflake.com/en/user-guide/key-pair-auth).


### Databricks
We support two authentication methods for Databricks:

- **Token-based**: Require Personal Access Token (PAT)
- **OAuth Client-based (M2M)**: Auto-enabled in every account with expected settings
More details [here](https://docs.getdbt.com/docs/core/connect-data-platform/databricks-setup#examples)).

#### Common Fields

| Field       | Description                                                                                   | Examples                      |
| ----------- | --------------------------------------------------------------------------------------------- | ----------------------------- |
| `host`      | The hostname of your cluster                                                                  | `YOURORG.databrickshost.com`  |
| `http_path` | The HTTP path to your SQL Warehouse or all-purpose cluster                                    | `/SQL/YOUR/HTTP/PATH`         |
| `catalog`   | The catalog used to connect to the warehouse. This is optional if you are using Unity Catalog | `MY_CATALOG`                  |
| `schema`    | The default schema to connect to                                                              | `MY_SCHEMA`                   |

#### Token-based Authentication

| Field      | Description                                              | Examples                      |
| ---------- | -------------------------------------------------------- | ----------------------------- |
| `token`    | The Personal Access Token (PAT) to connect to Databricks | `dapiXXXXXXXXXXXXXXXXXXXXXXX` |

#### OAuth Client-based Authentication (M2M)

| Field                 | Description                                                                     | Required |
| ----------------------| ------------------------------------------------------------------------------- | -------- |
| `auth_type`           | The type of authorization needed to connect to Databricks. Default as `oauth`   | Yes      |
| `client_id`           | The client ID for your Databricks OAuth application                             | Yes      |
| `client_secret`       | The client secret for your Databricks OAuth application                         | Yes      |

For more information on setting up OAuth Client-based authentication, refer to [Databricks's Oauth Client-based authentication documentation]((https://docs.getdbt.com/docs/core/connect-data-platform/databricks-setup?tokenoauth=oauth#examples)).


### BigQuery

!!!info "Important"
    For authentication, we currently provide support for service account JSON only. More details [here](https://docs.getdbt.com/docs/core/connect-data-platform/bigquery-setup#service-account-json).

| Field          | Description                                                                                | Examples                      |
| -------------- | ------------------------------------------------------------------------------------------ | ----------------------------- |
| `project`      | The GCP project to connect to                                                              | `GCP_PROJECT_ID`              |
| `dataset`      | The default BigQuery dataset to connect to                                                         | `DBT_DATASET_NAME`            |
| `keyfile_json` | The [keyfile](https://docs.getdbt.com/guides/bigquery?step=7#generate-bigquery-credentials) generated from your GCP service account to connect to BigQuery               | `keyfile_json: type: xxx project_id: xxx private_key_id: xxx ...` |


### Redshift

!!!info "Important"
    We currently support Database (Password-based authentication) only. More details [here](https://docs.getdbt.com/docs/core/connect-data-platform/redshift-setup#authentication-parameters).

| Field       | Description                                                                                   | Examples                      |
| ----------- | --------------------------------------------------------------------------------------------- | ----------------------------- |
| `host`      | Host of your cluster                                                                  | `hostname.region.redshift.amazonaws.com`  |
| `user` | Account username to log into your cluster                                    | `MY_USER`         |
| `password`   | Password for authentication | `MY_PASS`                  |
| `dbname`    | The default database to connect to                                                              | `MY_DB`                   |
| `schema`     | The default schema to connect to                                      | `MY_SCHEMA` |
| `port`          | Port for your Redshift environment | `5439`|

