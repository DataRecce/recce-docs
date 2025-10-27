---
title: Connect to Warehouse
---

## Recce OSS
Recce OSS supports all warehouses that dbt supports. It uses the same configuration as dbt, simply use your existing dbt profiles to connect to your warehouse. No additional setup required.

## Recce Cloud
If you use Recce Cloud, here are the warehouse connection settings. We currently support:

- [Snowflake](#snowflake)
- [Databricks](#databricks)

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
| `database`  | The default database to connect to        | `MYDB`                   |
| `schema`    | The default schema to connect to          | `PUBLIC`                 |
| `warehouse` | The warehouse to use when running queries | `WH_LOAD`                |

#### User & Password Authentication

| Field      | Description               | Examples |
| ---------- | ------------------------- | -------- |
| `user`     | The user to log in as     | `MYUSER` |
| `password` | The password for the user | `MYPASS` |

#### Key Pair Authentication

| Field                    | Description                                                                     | Required |
| ------------------------ | ------------------------------------------------------------------------------- | -------- |
| `user`                   | The user to log in as                                                           | Yes      |
| `private_key`            | Your RSA private key in PEM format or Base64-encoded DER format                 | Yes      |
| `private_key_passphrase` | Passphrase for the private key (only required if your private key is encrypted) | No       |

For more information on setting up key pair authentication, refer to [Snowflake's key pair authentication documentation](https://docs.snowflake.com/en/user-guide/key-pair-auth).


### Databricks

We only support token-based authentication.

| Field       | Description                                                                                   | Examples                      |
| ----------- | --------------------------------------------------------------------------------------------- | ----------------------------- |
| `host`      | The hostname of your cluster                                                                  | `YOURORG.databrickshost.com`  |
| `http_path` | The HTTP path to your SQL Warehouse or all-purpose cluster                                    | `/SQL/YOUR/HTTP/PATH`         |
| `catalog`   | The catalog used to connect to the warehouse. This is optional if you are using Unity Catalog | `MY_CATALOG`                  |
| `schema`    | The default schema to connect to                                                              | `MY_SCHEMA`                   |
| `token`     | The Personal Access Token (PAT) to connect to Databricks                                      | `dapiXXXXXXXXXXXXXXXXXXXXXXX` |
