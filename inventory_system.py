"""
Inventory Management System

This module defines a class-based inventory system for adding,
removing, and managing stock items with proper logging, error
handling, and secure file storage.
"""

import json
import logging


class InventorySystem:
    """Manages inventory operations and storage."""

    def __init__(self, file_name="inventory.json"):
        """Initialize the system with a data file."""
        self.stock_data = {}
        self.file_name = file_name
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )

    def add_item(self, item, qty):
        """Add an item and quantity to the inventory."""
        if not isinstance(item, str) or not isinstance(qty, int):
            logging.warning("Invalid input types for item or qty.")
            return
        self.stock_data[item] = self.stock_data.get(item, 0) + qty
        logging.info("Added %s of %s", qty, item)

    def remove_item(self, item, qty):
        """Remove a given quantity of an item from the inventory."""
        try:
            if item not in self.stock_data:
                raise KeyError(f"{item} not found in stock")
            self.stock_data[item] -= qty
            if self.stock_data[item] <= 0:
                del self.stock_data[item]
            logging.info("Removed %s of %s", qty, item)
        except KeyError as error:
            logging.error("KeyError: %s", error)
        except (ValueError, TypeError) as error:
            logging.error("Invalid input: %s", error)

    def get_qty(self, item):
        """Return the current quantity of a given item."""
        return self.stock_data.get(item, 0)

    def load_data(self):
        """Load inventory data from JSON file."""
        try:
            with open(self.file_name, "r", encoding="utf-8") as file:
                self.stock_data = json.load(file)
            logging.info("Data loaded successfully.")
        except FileNotFoundError:
            logging.warning("File not found. Starting with empty inventory.")
            self.stock_data = {}

    def save_data(self):
        """Save inventory data to JSON file."""
        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump(self.stock_data, file, indent=4)
        logging.info("Data saved successfully.")

    def print_data(self):
        """Print all inventory items and their quantities."""
        print("Items Report:")
        for item, qty in self.stock_data.items():
            print(f"{item} -> {qty}")

    def check_low_items(self, threshold=5):
        """Return items below the given threshold quantity."""
        return [item for item, qty in self.stock_data.items()
                if qty < threshold]


def main():
    """Main entry point of the program."""
    system = InventorySystem()
    system.add_item("apple", 10)
    system.add_item("banana", 3)
    system.remove_item("apple", 2)
    print(
        "Apple stock:", system.get_qty("apple"),
        "Low items:", system.check_low_items()
    )
    system.save_data()
    system.load_data()
    system.print_data()
    logging.info(
        "Program executed successfully."
    )


if __name__ == "__main__":
    main()
