# Azure Data Factory REST API Ingestion Pipeline

## Project Overview

This project demonstrates how to build a cloud-based data ingestion pipeline using **Azure Data Factory (ADF)**.

The pipeline extracts user information from a REST API (**ReqRes API**) using an Azure Data Factory **Copy Activity** and stores the extracted data in **Azure Blob Storage** as a delimited text file.

This project focuses on the **data ingestion layer** of an ETL pipeline and demonstrates how Azure Data Factory can connect to external APIs and store data in Azure cloud storage.

---

# Architecture

## Current Implementation

```text
             REST API
          (ReqRes Users API)
                  |
                  |
                  ▼
        Azure Data Factory
          Copy Activity
                  |
                  |
                  ▼
        Azure Blob Storage
       (Delimited Text File)
```

---

# Source

**REST API**

```
https://reqres.in/api/users?page=2
```

The API provides sample user data in JSON format.

---

# Destination

**Azure Blob Storage**

* File Format: Delimited Text
* Storage Layer: Raw Data Storage

---

# Data Fields Extracted

The pipeline extracts the following fields from the API response:

| Field      | Description            |
| ---------- | ---------------------- |
| id         | User identifier        |
| email      | User email address     |
| first_name | User first name        |
| avatar     | User profile image URL |

---

# Tools & Technologies Used

* Azure Data Factory
* Azure Blob Storage
* REST API
* JSON
* Copy Activity
* Linked Services
* Datasets

---

# How the Pipeline Works

1. Azure Data Factory connects to the REST API using an HTTP connection.
2. A GET request is sent to the ReqRes API endpoint.
3. The API returns user information in JSON format.
4. ADF Copy Activity extracts the required fields:

   * id
   * email
   * first_name
   * avatar
5. The extracted data is converted into a delimited text format.
6. The output file is stored in Azure Blob Storage.

---

# Pipeline Components

## Linked Services

The pipeline uses:

* REST API Linked Service
* Azure Blob Storage Linked Service

## Datasets

Configured datasets for:

* REST API JSON source
* Blob Storage text file destination

## Copy Activity

The Copy Activity performs:

* Data extraction
* Field mapping
* Data movement from API to cloud storage

---

# Sample Data Flow

### Source JSON

```json
{
    "id": 1,
    "email": "george.bluth@reqres.in",
    "first_name": "George",
    "avatar": "https://reqres.in/img/faces/1-image.jpg"
}
```

### Stored Output

```text
1,george.bluth@reqres.in,George,https://reqres.in/img/faces/1-image.jpg
```

---

# Future Enhancements (Production Pipeline Design)

The current project implements the ingestion layer. The following enhancements can extend it into a complete end-to-end data engineering solution.

## 1. Data Transformation Layer

Add Azure Data Factory Mapping Data Flow to clean and transform the raw data.

Planned transformations:

| Transformation    | Description                               |
| ----------------- | ----------------------------------------- |
| Remove duplicates | Keep unique user records                  |
| Trim spaces       | Clean unwanted whitespace                 |
| Standardize email | Convert emails to lowercase               |
| Format names      | Convert names to proper case              |
| Data validation   | Check missing or invalid values           |
| Add audit columns | Add load timestamp and source information |

Example:

Before:

| id | email                                       | first_name |
| -- | ------------------------------------------- | ---------- |
| 1  | [GEORGE@REQRES.IN](mailto:GEORGE@REQRES.IN) | george     |

After:

| user_id | email                                       | first_name | source_system | load_date  |
| ------- | ------------------------------------------- | ---------- | ------------- | ---------- |
| 1       | [george@reqres.in](mailto:george@reqres.in) | George     | ReqRes API    | 2026-07-11 |

---

# Future Production Architecture

```text
                    REST API
                       |
                       ▼
              Azure Data Factory
                 Copy Activity
                       |
                       ▼
             Azure Blob Storage
                  Raw Layer
                       |
                       ▼
          Azure Data Factory Data Flow
              Transformation Layer
                       |
                       ▼
             Azure Data Lake Storage
                Curated Layer
                       |
                       ▼
            Azure Synapse Analytics
                Data Warehouse
                       |
                       ▼
                  Power BI
             Analytics & Reporting
```

---

# Future Scheduling & Monitoring

Planned improvements:

* Configure Azure Data Factory Triggers for scheduled execution.
* Add pipeline monitoring and logging.
* Implement error handling and retry policies.
* Add data quality checks.

---

# Security

Sensitive information is not stored in this repository.

The following items are excluded:

* API credentials
* Azure connection strings
* Access keys
* Authentication details

---

# Project Outcome

This project demonstrates:

✅ REST API data ingestion using Azure Data Factory
✅ Cloud data storage using Azure Blob Storage
✅ Data pipeline development using Copy Activity
✅ Azure service integration
✅ Foundation for building a complete ETL/ELT data platform

---

# Author

**Rafiya Ahmed**

Azure Data Engineering Project
