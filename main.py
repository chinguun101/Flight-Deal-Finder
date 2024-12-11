import time
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

# ==================== Set up the Flight Search ====================

# Initialize the data manager to handle destination data
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

# Initialize the flight search and notification manager
flight_search = FlightSearch()
notification_manager = NotificationManager()

# Set your origin airport
ORIGIN_CITY_IATA = "LON"

# ==================== Update the Airport Codes in Google Sheet ====================

# Update IATA codes for destinations if missing
for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        # Slowing down requests to avoid rate limit
        time.sleep(2)
print(f"sheet_data:\n {sheet_data}")

# Update the destination data in the data manager
data_manager.destination_data = sheet_data
# data_manager.update_destination_codes()

# ==================== Search for Flights and Send Notifications ====================

# Define the search period for flights
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

# Search for flights for each destination
for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today,
        is_direct="false",
    )
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: £{cheapest_flight.price} with {cheapest_flight.nr_stops} layovers")
    # Slowing down requests to avoid rate limit
    time.sleep(2)

    # Retry if no flight price is available
    if cheapest_flight.price == "N/A":
        flights = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today,
            is_direct="false",
        )
        cheapest_flight = find_cheapest_flight(flights)
        print(f"{destination['city']}: £{cheapest_flight.price} with {cheapest_flight.nr_stops} layovers")
    time.sleep(2)

    # Send notifications if a cheaper flight is found
    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        print(f"Lower price flight found to {destination['city']}!")
        # notification_manager.send_sms(
        #     message_body=f"Low price alert! Only £{cheapest_flight.price} to fly "
        #                  f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
        #                  f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        # )
        # SMS not working? Try WhatsApp instead.
        notification_manager.send_whatsapp(
            message_body=f"Low price alert! Only £{cheapest_flight.price} to fly "
                         f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                         f"on {cheapest_flight.out_date} until {cheapest_flight.return_date} with {cheapest_flight.nr_stops} layovers."
        )

        notification_manager.send_emails(
            mail_list=data_manager.get_emails(),
            message_body=f"Subject:Low price alert!\n\nOnly {cheapest_flight.price}GBP to fly "
                         f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                         f"on {cheapest_flight.out_date} until {cheapest_flight.return_date} with {cheapest_flight.nr_stops} layovers."
        )


