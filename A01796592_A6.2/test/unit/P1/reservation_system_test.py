"""Test file for the Reservation System module.
CLA-T-1201 - A01796592 - Assignment 6.2 - Problem 1
This module contains test cases for the ReservationSystem class.
"""

import unittest
import os
from P1.reservation_system import Hotel, Customer, Reservation


class TestReservationSystem(unittest.TestCase):
    """Test cases for the ReservationSystem class."""
    def setUp(self):
        """Set up test environment."""
        self.hotel = Hotel("H001")
        self.customer = Customer("C001")
        self.reservation = Reservation("R001", "H001", "C001")

    def tearDown(self):
        """Clean up test environment."""
        for file in ["hotels.json", "customers.json", "reservations.json"]:
            if os.path.exists(file):
                os.remove(file)

    def test_create_hotel_class_attributes(self):
        """Test that hotel class attributes are set correctly."""
        self.assertEqual(self.hotel.hotel_id, "H001")

    def test_create_hotel_success(self):
        """Test creating a hotel."""
        hotel_data = self.hotel.create_hotel(
            "Hotel California", "Los Angeles", 100
        )
        self.assertIsInstance(hotel_data, dict)
        self.assertEqual(hotel_data["name"], "Hotel California")
        self.assertEqual(hotel_data["location"], "Los Angeles")
        self.assertEqual(hotel_data["rooms"], 100)

    def test_create_hotel_invalid_rooms(self):
        """Test creating a hotel with invalid number of rooms."""
        with self.assertRaises(ValueError):
            self.hotel.create_hotel("Bad Hotel", "Nowhere", -5)

    def test_delete_hotel(self):
        """Test deleting a hotel."""
        self.hotel.create_hotel("Hotel California", "Los Angeles", 100)
        self.hotel.delete_hotel()
        self.hotel.delete_hotel()

    def test_display_hotel_info(self):
        """Test displaying hotel information."""
        hotel_info = Hotel("H002")
        hotel_info.create_hotel("Grand Hotel", "New York", 200)
        hotel_info.display_hotel_information()
        hotel_info.delete_hotel()
        hotel_info.display_hotel_information()

    def test_modify_hotel_info(self):
        """Test modifying hotel information."""
        self.hotel.create_hotel("Hotel California", "Los Angeles", 100)
        modified_info = self.hotel.modify_hotel_information(
            name="Hotel New California", location="San Francisco", rooms=150
        )
        self.assertEqual(modified_info["name"], "Hotel New California")
        self.assertEqual(modified_info["location"], "San Francisco")
        self.assertEqual(modified_info["rooms"], 150)
        self.hotel.delete_hotel()
        self.hotel.modify_hotel_information(name="Should Fail")

    def test_create_customer_success(self):
        """Test creating a customer."""
        customer_data = self.customer.create_customer("John Doe", 30)
        self.assertIsInstance(customer_data, dict)
        self.assertEqual(customer_data["name"], "John Doe")
        self.assertEqual(customer_data["age"], 30)

    def test_create_customer_invalid_age(self):
        """Test creating a customer with invalid age."""
        with self.assertRaises(ValueError):
            self.customer.create_customer("Jane", -1)

    def test_create_reservation_success(self):
        """Test creating a reservation."""
        hotel_reservation = Hotel("H001")
        hotel_reservation.create_hotel("Hotel California", "Los Angeles", 100)
        hotel_reservation.reserve_room("H001", "2024-07-01", "2024-07-10")
        hotel_reservation.delete_hotel()
        hotel_reservation.reserve_room("H001", "2024-07-01", "2024-07-10")

    def test_cancel_reservation_hotel(self):
        """Test canceling a reservation."""
        hotel_reservation = Hotel("H001")
        hotel_reservation.create_hotel("Hotel California", "Los Angeles", 100)
        hotel_reservation.reserve_room("H001", "2024-07-01", "2024-07-10")
        hotel_reservation.cancel_reservation("R001")
        hotel_reservation.delete_hotel()
        hotel_reservation.cancel_reservation("R001")

    def test_create_reservation_invalid_dates(self):
        """Test creating a reservation with invalid dates."""
        with self.assertRaises(ValueError):
            self.reservation.create_reservation(
                "H001", "2024-07-10", "2024-07-01"
            )

    def test_cancel_reservation(self):
        """Test canceling a reservation."""
        self.reservation.create_reservation(
            "H001", "2024-07-01", "2024-07-10"
        )
        self.reservation.cancel_reservation()

    def test_delete_customer(self):
        """Test deleting a customer."""
        self.customer.create_customer("John Doe", 30)
        self.customer.delete_customer()
        self.customer.delete_customer()

    def test_display_customer_info(self):
        """Test displaying customer information."""
        customer_info = Customer("C002")
        customer_info.create_customer("Jane Doe", 25)
        customer_info.display_customer_information()
        customer_info.delete_customer()
        customer_info.display_customer_information()

    def test_modify_customer_info(self):
        """Test modifying customer information."""
        self.customer.create_customer("John Doe", 30)
        modified_info = self.customer.modify_customer_information(
            name="John Smith", age=35
        )
        self.assertEqual(modified_info["name"], "John Smith")
        self.assertEqual(modified_info["age"], 35)
        self.customer.delete_customer()
        self.customer.modify_customer_information(name="Should Fail")

    def test_create_reservation_nonexistent_hotel(self):
        """Test creating a reservation for a non-existent hotel."""
        self.reservation.create_reservation(
                "H999", "2024-07-01", "2024-07-10"
            )

    def test_cancel_reservation_nonexistent(self):
        """Test canceling a non-existent reservation."""
        self.reservation.cancel_reservation()


if __name__ == "__main__":
    unittest.main(verbosity=2)
