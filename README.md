# Database Migration: MySQL to PostgreSQL

## Overview
This project automates the migration of a relational database (Formula 1 dataset) from MySQL to PostgreSQL. The migration is performed using a custom Python script running within a Dockerized environment. It handles both Data Definition Language (DDL) generation and Data Manipulation Language (DML) batch insertion dynamically.

## Implementation Details
To make the migration work seamlessly, several architectural decisions and implementations were necessary:
*   **Dynamic DDL Generation:** The script uses `SHOW TABLES` and `DESCRIBE` queries on the MySQL database to fetch the schema structure dynamically, rather than hardcoding queries.
*   **Custom Type Mapping:** A Python dictionary was created to translate MySQL-specific data types to PostgreSQL equivalents (e.g., converting `tinyint` to `SMALLINT`).
*   **Batch Data Transfer:** Data was extracted from MySQL using `fetchall()` and inserted into PostgreSQL using `executemany()` to ensure performance and avoid memory overloads.
*   **Volume Mounting:** The Python script was mounted as a Docker volume (`./script:/app/script`), allowing real-time code edits without the need to rebuild the Docker image on every change.

## Challenges Faced
During the development of the migration script, several technical hurdles were resolved:
1.  **PostgreSQL SERIAL Syntax:** Unlike MySQL, which uses `AUTO_INCREMENT` as a column modifier, PostgreSQL uses `SERIAL` as a distinct pseudo-type. The script logic had to be adjusted to replace the integer type entirely when an auto-increment flag was detected.
2.  **Composite Primary Keys:** MySQL's `DESCRIBE` command flags all columns involved in a composite primary key. Attempting to define `PRIMARY KEY` on multiple individual columns caused PostgreSQL syntax errors. The solution was to collect all primary key column names in a list and define them as a single table constraint at the end of the `CREATE TABLE` statement.
3.  **Default Dictionary Values:** Using `.get()` for type mapping required returning the original uppercase type as a default (e.g., `VARCHAR(50)`) to prevent standard types from being incorrectly overwritten.
4.  **Cursor and Transaction Lifecycle:** Executing commands outside the Python `with` statement caused "cursor already closed" errors. Additionally, PostgreSQL required an explicit `connection.commit()` to persist the schema and data changes.

## Docker Guide and Commands
The entire infrastructure, including databases and administration tools, is containerized. All image mirrors and versions used in the `docker-compose.yml` file (such as `mysql`, `postgres`, `python`, `phpmyadmin`, and `dpage/pgadmin4`) were sourced directly from the official Docker Hub registry.

### Prerequisites
Make sure Docker and Docker Compose are installed on your system.

### Common Docker Commands Used

*   **Start the Infrastructure:**
    Starts the databases and management interfaces (pgAdmin, phpMyAdmin) in the background.
    `docker compose up -d`

*   **Run the Migration Script:**
    Executes the Python migration script interactively. The `--rm` flag ensures the temporary Python container is deleted immediately after the script finishes, keeping the environment clean.
    `docker compose run --rm python_migrator`

*   **Check Container Logs:**
    Useful for debugging if a container stops unexpectedly.
    `docker compose logs python_migrator`
    *(You can replace `python_migrator` with any other service name).*

*   **Stop and Remove the Environment:**
    Stops all running containers and removes the network.
    `docker compose down`