# XportSpyder

## Overview

XportSpyder is an automation crawler designed to collect badminton court availability data from the TeamXports booking platform.
It simulates human login, retrieves the next 14 days of availability data, and saves the results in a structured CSV file for analysis or alert purposes.

## Features

- 14-Day Availability Scraper
Automatically retrieves booking data for the next 14 days, including morning, afternoon, and evening time slots.
- Login Flow Automation
Simulates human login behavior and handles cookie validation to ensure session availability.
-  Structured Availability Output
Scraped data is cleaned and exported to a structured CSV file, focusing on available and reserved slots across all venues and time periods..

## Usage Steps
🔐 Login Simulation Phase

1. Use `location.py` to record mouse click coordinates (for buttons and input fields on the login page)

2. Input the recorded coordinates into the corresponding positions in `simulate_login_save_cookie.py`

3. Create a `credentials.json` file containing your login username and password

4. Run `simulate_login_save_cookie.py` to simulate login and generate the `cookies_teamxports.json` file

🕸 Data Crawling Phase

5. Run `crawler.py` to automatically fetch badminton court availability for the next 14 days and export it as `teamxports_booking_14days.csv`

