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
        self.hotel.create_hotel("Hotel California", "Los Angeles", 100)
        reservation_data = self.reservation.create_reservation(
            "H001", "2024-07-01", "2024-07-10"
        )
        self.assertIsInstance(reservation_data, dict)
        self.assertEqual(reservation_data["hotel_id"], "H001")
        self.assertEqual(reservation_data["customer_id"], "C001")

    def test_create_reservation_invalid_dates(self):
        """Test creating a reservation with invalid dates."""
        with self.assertRaises(ValueError):
            self.reservation.create_reservation(
                "H001", "2024-07-10", "2024-07-01"
            )

    def test_create_hotel(self):
        """Test creating a hotel instance."""
        hotel = Hotel("12345")
        self.assertEqual(hotel.hotel_id, "12345")


if __name__ == "__main__":
    unittest.main()
