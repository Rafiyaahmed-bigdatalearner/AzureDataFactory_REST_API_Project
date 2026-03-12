# Azure Data Factory REST API Project

## Project Overview

This project demonstrates how to extract data from a REST API using **Azure Data Factory (ADF)** and store the data in **Azure Blob Storage**.

The pipeline uses a **Copy Activity** to fetch user data from the ReqRes API and write it to a text file in Blob Storage.

---

## Source

REST API
https://reqres.in/api/users?page=2

---

## Sink

Azure Blob Storage (Delimited Text file)

---

## Pipeline Architecture

![ADF Pipeline](pipeline.png)

---

## Fields Extracted

* id
* email
* first_name
* avatar

---

## Tools Used

* Azure Data Factory
* Azure Blob Storage
* REST API

---

## How it Works

1. Azure Data Factory sends a **GET request** to the REST API.
2. The API returns user data in JSON format.
3. Copy Activity maps the required fields.
4. The data is stored in Azure Blob Storage as a delimited text file.

---

## Note

API keys or credentials are not included in this repository for security reasons.
