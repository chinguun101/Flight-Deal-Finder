import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class DataManager:
    """
    A class to manage data operations, such as retrieving and updating destination data.
    """

    def __init__(self):
        # self._user = os.environ["SHEET_USERNAME"]
        # self._password = os.environ["SHEET_PASSWORD"]
        self.SHEET_ENDPOINT= os.getenv("SHEET_ENDPOINT")
        self.SHEET_ENDPOINT_USERS= os.getenv("SHEET_ENDPOINT_USERS")
        self.SHEET_TOKEN=os.getenv("SHEET_TOKEN")
        self.headers={'Authorization':self.SHEET_TOKEN}
        #self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}
        self.email_data=[]

    def get_emails(self):
        """
        Retrieves a list of email addresses for sending notifications.

        Returns:
            list: A list of email addresses.
        """
        # Placeholder for actual email retrieval logic
        return []

    def get_destination_data(self):
        """
        Retrieves destination data from a data source, such as a Google Sheet or a database.

        Returns:
            list: A list of dictionaries containing destination data.
        """
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response=requests.get(f"{self.SHEET_ENDPOINT}",headers=self.headers)# ,json=body)
        data = response.json()
        self.destination_data = data["prices"]
        # Try importing pretty print and printing the data out again using pprint() to see it formatted.
        #pprint(data)
        return self.destination_data

    # In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        """
        Updates the IATA codes for destinations in the data source.

        This method iterates over the destination data and sends a PUT request to update
        each destination's IATA code in the data source.
        """
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.SHEET_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=self.headers
            )
            print(response.text)

DataManager()