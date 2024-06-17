# Simple WebScraper

This project scrapes upcoming tour information from a specified URL, stores it in a SQLite database, and sends an email notification if a new tour is found.

## Table of Contents
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)
- [Functions](#functions)
- [License](#license)

## Project Structure


- `data.db`: SQLite database to store tour information.
- `extract.yaml`: YAML file used by `selectorlib` to extract tour information from the webpage.
- `send_email.py`: Contains the `my_send_email` function to send email notifications.
- `scraper.py`: Main script to scrape, extract, store, and send notifications.
- `README.md`: Project documentation.

## Requirements

- Python 3.x
- `requests` library
- `selectorlib` library
- `sqlite3` library (part of Python standard library)

## Setup

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/tour-scraper.git
    cd tour-scraper
    ```

2. **Install dependencies:**
    ```sh
    pip install requests selectorlib
    ```

3. **Create `data.db` database:**
    ```sh
    sqlite3 data.db
    ```
    Inside the SQLite shell, create the `events` table:
    ```sql
    CREATE TABLE events (
        band TEXT,
        city TEXT,
        date TEXT
    );
    ```
    Exit the SQLite shell by typing `.exit`.

4. **Prepare `extract.yaml` file:**
    Ensure your `extract.yaml` file is properly configured to extract the tour information from the webpage.

5. **Configure email sending:**
    Ensure `send_email.py` contains the `my_send_email` function to send email notifications. This function should be implemented to send an email when called.

