# Company Domain Verification API

## Project Overview

The Company Domain Verification API is a backend application designed to manage and document relationships between companies and web domains.

The purpose of the application is to support company-to-domain verification by storing a company, a domain, the determination of whether the domain belongs to the company, a confidence level, justification for the determination, and supporting sources.

For example, the application could record a relationship between a company and a domain with the following information:

* Company: Example Corporation
* Domain: example.com
* Match Status: Confirmed
* Confidence Level: High
* Justification: The company's official website identifies the domain as its primary website.
* Supporting Sources: Official website, business registry, or other publicly available sources

## Technology Stack

* Python
* Flask
* PostgreSQL
* Docker
* Docker Compose

The API will initially be tested using Insomnia or Postman.

## Architecture

The project uses a two-tier architecture consisting of a Flask web application and a PostgreSQL database.

```text
API Client (Insomnia / Postman)
              |
              | HTTP Requests
              v
        Flask API
              |
              | SQL
              v
       PostgreSQL Database
```

Docker Compose is used to define and manage both application services.

## Planned Features

The application will eventually support:

* Creating and managing companies
* Creating and managing domains
* Associating companies with domains
* Recording match status
* Recording confidence levels
* Adding justification for match decisions
* Adding supporting sources
* Searching and filtering company-domain matches

## Project Status

This project is currently under development.

The initial implementation focuses on establishing a Dockerized two-tier architecture consisting of a Flask web application and PostgreSQL database. Additional API endpoints and database functionality will be implemented in future development stages.
