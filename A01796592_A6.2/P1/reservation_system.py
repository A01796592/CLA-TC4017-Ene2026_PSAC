"""Reservation System Module
CLA-T-1201 - A01796592 - Assignment 6.2 - Problem 1
This module contains the ReservationSystem class which manages reservations.
"""

import json
import os


class Hotel:
    """Hotel class to represent a hotel with its name and location."""
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id

    def create_hotel(self, name, location, rooms, reservations=None):
        """Creates a hotel instance and returns it."""
        hotel_data = {
            "hotel_id": self.hotel_id,
            "name": name,
            "location": location,
            "rooms": rooms,
            "reservations": reservations if reservations is not None else []
        }
        with open("hotels.json", "w", encoding="utf-8") as f:
            json.dump(hotel_data, f, indent=4)
        return hotel_data

    def delete_hotel(self):
        """Deletes the hotel instance from the hotels.json file."""
        if os.path.exists("hotels.json"):
            os.remove("hotels.json")
            print("Hotel deleted successfully.")
        else:
            print("Hotel file does not exist.")

    def display_hotel_information(self):
        """Displays the hotel information."""
        if os.path.exists("hotels.json"):
            with open("hotels.json", "r", encoding="utf-8") as f:
                hotel_data = json.load(f)
                print(f"Hotel Name: {hotel_data['name']}")
                print(f"Location: {hotel_data['location']}")
                print(f"Rooms: {hotel_data['rooms']}")
                print(f"Reservations: {hotel_data['reservations']}")
        else:
            print("Hotel file does not exist.")

    def modify_hotel_information(self, name=None, location=None, rooms=None):
        """Modifies the hotel information and updates the hotels.json file."""
        if os.path.exists("hotels.json"):
            with open("hotels.json", "r", encoding="utf-8") as f:
                hotel_data = json.load(f)
            if name:
                hotel_data["name"] = name
            if location:
                hotel_data["location"] = location
            if rooms:
                hotel_data["rooms"] = rooms
            with open("hotels.json", "w", encoding="utf-8") as f:
                json.dump(hotel_data, f, indent=4)
        else:
            print("Hotel file does not exist.")

    def reserve_room(self, customer_id, check_in_date, check_out_date):
        """Reserves a room for a customer if available."""
        if os.path.exists("hotels.json"):
            with open("hotels.json", "r", encoding="utf-8") as f:
                hotel_data = json.load(f)
            reservations = hotel_data.get("reservations", [])
            rooms = hotel_data.get("rooms", 0)
            if len(reservations) < rooms:
                reservation_id = len(reservations) + 1
                reservation = {
                    "reservation_id": reservation_id,
                    "customer_id": customer_id,
                    "check_in_date": check_in_date,
                    "check_out_date": check_out_date
                }
                reservations.append(reservation)
                hotel_data["reservations"] = reservations
                with open("hotels.json", "w", encoding="utf-8") as f:
                    json.dump(hotel_data, f, indent=4)
                print(f"Room reserved successfully for customer {customer_id}")
            else:
                print("No rooms available for the selected dates.")
        else:
            print("Hotel file does not exist.")

    def cancel_reservation(self, reservation_id):
        """Cancels a reservation based on the reservation ID."""
        if os.path.exists("hotels.json"):
            with open("hotels.json", "r", encoding="utf-8") as f:
                hotel_data = json.load(f)
            reservations = hotel_data.get("reservations", [])
            reservations = [res for res in reservations
                            if res["reservation_id"] != reservation_id]
            hotel_data["reservations"] = reservations
            with open("hotels.json", "w", encoding="utf-8") as f:
                json.dump(hotel_data, f, indent=4)
            print(f"Reservation {reservation_id} cancelled successfully.")
        else:
            print("Hotel file does not exist.")


class Customer:
    """Customer class to represent a customer with their ID and name."""
    def __init__(self, customer_id):
        self.customer_id = customer_id

    def create_customer(self, name, age=None):
        """Creates a customer instance and returns it."""
        customer_data = {
            "customer_id": self.customer_id,
            "name": name,
            "age": age
        }
        with open("customers.json", "w", encoding="utf-8") as f:
            json.dump(customer_data, f, indent=4)
        return customer_data

    def delete_customer(self):
        """Deletes the customer instance from the customers.json file."""
        if os.path.exists("customers.json"):
            os.remove("customers.json")
        else:
            print("Customer file does not exist.")

    def display_customer_information(self):
        """Displays the customer information."""
        if os.path.exists("customers.json"):
            with open("customers.json", "r", encoding="utf-8") as f:
                customer_data = json.load(f)
                print(f"Customer ID: {customer_data['customer_id']}")
                print(f"Name: {customer_data['name']}")
                print(f"Age: {customer_data.get('age', 'Not specified')}")
        else:
            print("Customer file does not exist.")

    def modify_customer_information(self, name=None, age=None):
        """Modifies the customer information and updates
        the customers.json file."""
        if os.path.exists("customers.json"):
            with open("customers.json", "r", encoding="utf-8") as f:
                customer_data = json.load(f)
            if name:
                customer_data["name"] = name
            if age is not None:
                customer_data["age"] = age
            with open("customers.json", "w", encoding="utf-8") as f:
                json.dump(customer_data, f, indent=4)
        else:
            print("Customer file does not exist.")


class Reservation:
    """Reservation class to represent a reservation with its details."""
    def __init__(self, reservation_id, hotel_id, customer_id):
        self.reservation_id = reservation_id
        self.hotel_id = Hotel(hotel_id).hotel_id
        self.customer_id = Customer(customer_id).customer_id

    def create_reservation(self, hotel_name, check_in_date,
                           check_out_date):
        """Creates a reservation instance and returns it."""
        reservation_data = {
            "reservation_id": self.reservation_id,
            "hotel_name": hotel_name,
            "Hotel ID": self.hotel_id,
            "Customer ID": self.customer_id,
            "check_in_date": check_in_date,
            "check_out_date": check_out_date
        }
        with open("reservations.json", "w", encoding="utf-8") as f:
            json.dump(reservation_data, f, indent=4)
        return reservation_data

    def cancel_reservation(self):
        """Cancels the reservation instance from the reservations.json file."""
        if os.path.exists("reservations.json"):
            os.remove("reservations.json")
        else:
            print("Reservation file does not exist.")


if __name__ == "__main__":
    try:
        arg = input("Enter 'Hotel' to create a hotel, "
                    "'Customer' to create a customer, "
                    "'Reservation' to create a reservation, "
                    "or 'exit' to quit: ").strip().lower()
        if arg == "hotel":
            hotel_id_arg = input("Enter hotel ID: ")
            hotel_name_arg = input("Enter hotel name: ")
            location_arg = input("Enter hotel location: ")
            rooms_arg = int(input("Enter number of rooms: "))
            hotel_arg = Hotel(hotel_id_arg)
            hotel_arg.create_hotel(hotel_name_arg, location_arg, rooms_arg)
        elif arg == "customer":
            customer_id_arg = input("Enter customer ID: ")
            customer_name_arg = input("Enter customer name: ")
            age_arg = input("Enter customer age (optional): ")
            customer_arg = Customer(customer_id_arg)
            customer_arg.create_customer(customer_name_arg,
                                         age_arg if age_arg else None)
        elif arg == "reservation":
            reservation_id_arg = input("Enter reservation ID: ")
            hotel_id_arg = input("Enter hotel ID: ")
            customer_id_arg = input("Enter customer ID: ")
            check_in_date_arg = input("Enter check-in date (YYYY-MM-DD): ")
            check_out_date_arg = input("Enter check-out date (YYYY-MM-DD): ")
            reservation_arg = Reservation(reservation_id_arg,
                                          hotel_id_arg,
                                          customer_id_arg)
            reservation_arg.create_reservation(hotel_id_arg,
                                               check_in_date_arg,
                                               check_out_date_arg)
        elif arg == "exit":
            print("Exiting the system.")
        else:
            print("Invalid option. Please try again.")
    except (ValueError, FileNotFoundError, json.JSONDecodeError) as e:
        print(f"An error occurred: {e}")
