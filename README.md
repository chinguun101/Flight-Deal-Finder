# Flight Deal Finder

The Flight Deal Finder is a Python application that uses the Amadeus API to search for flight deals and notify users of the best prices. It retrieves destination data, updates IATA codes, searches for flights, and sends notifications via email, SMS, or WhatsApp.

## Features

- Retrieve and update destination data from a Google Sheet.
- Search for flights using the Amadeus API.
- Find the cheapest flight for each destination.
- Send notifications via email, SMS, or WhatsApp when a cheaper flight is found.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/chinguun101/flight-deal-finder.git
   cd flight-deal-finder
   ```

2. **Install the required packages:**

   Make sure you have Python installed, then run:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**

   Create a `.env` file in the root directory and add the following environment variables:

   ```plaintext
   AMADEUS_API_KEY=your_amadeus_api_key
   AMADEUS_SECRET=your_amadeus_secret
   SHEET_ENDPOINT=your_google_sheet_endpoint
   SHEET_ENDPOINT_USERS=your_google_sheet_users_endpoint
   SHEET_TOKEN=your_sheety_api_token
   TWILIO_SID=your_twilio_sid
   TWILIO_AUTH_TOKEN=your_twilio_auth_token
   TWILIO_VIRTUAL_NUMBER=your_twilio_virtual_number
   TWILIO_WHATSAPP_NUMBER=your_twilio_whatsapp_number
   TWILIO_VERIFIED_NUMBER=your_verified_number
   EMAIL=your_email_address
   PASSWORD=your_email_password
   ```

## Usage

1. **Run the main script:**

   Execute the main script to start the flight deal finder:

   ```bash
   python flight_deal_finder/main.py
   ```

2. **Check the console output:**

   The script will print the status of flight searches and any notifications sent.

## Project Structure

- `flight_deal_finder/main.py`: The main script that orchestrates the flight search and notification process.
- `flight_deal_finder/flight_search.py`: Handles flight search operations using the Amadeus API.
- `flight_deal_finder/data_manager.py`: Manages data operations, such as retrieving and updating destination data.
- `flight_deal_finder/notification_manager.py`: Manages sending notifications via email, SMS, and WhatsApp.
- `flight_deal_finder/flight_data.py`: Contains the `FlightData` class and logic to find the cheapest flight.
- `requirements.txt`: Lists the Python packages required for the project.

## Acknowledgments

- [Amadeus API](https://developers.amadeus.com/) for flight data.
- [Twilio](https://www.twilio.com/) for SMS and WhatsApp notifications.
- [Sheety](https://sheety.co/) for Google Sheets integration.