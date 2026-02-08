""" Convert numbers
CLA-T-1201 - A01796592 - Assignment 4.2 - Problem 2
This script reads a file containing numbers separated by commas, spaces, semicolons, or new lines,
and converts them to binary, and hexadecimal formats, saving the results to separate files.
"""

import sys
import time

class NumberConverter:
    """Class to convert numbers to different formats."""
    def __init__(self, arg_numbers):
        self.numbers = arg_numbers

    def to_binary(self):
        """Convert numbers to binary format."""
        binary_numbers = []
        for num_to_bin in self.numbers:
            try:
                n = int(num_to_bin)
                binary = ""
                if n == 0:
                    binary = "0"
                else:
                    while n > 0:
                        binary = str(n % 2) + binary
                        n //= 2
                binary_numbers.append(binary)
            except ValueError:
                print(f"Warning: '{num_to_bin}' is not a valid integer and will be skipped.")
        return binary_numbers

    def to_hexadecimal(self):
        """Convert numbers to hexadecimal format."""
        hex_numbers = []
        for num_to_hex in self.numbers:
            try:
                hex_numbers.append(hex(int(num_to_hex)))
            except ValueError:
                print(f"Warning: '{num_to_hex}' is not a valid integer and will be skipped.")
        return hex_numbers

    def save_to_file(self, data1, data2, filen):
        """Save converted data to a file."""
        with open(filen, 'w', encoding='utf-8') as f:
            f.write("ITEM \tTC \t \tBIN \t \t \tHEX \n")
            print("ITEM \tTC \t \tBIN \t \t \tHEX \n")
            for i, item in enumerate(data1):
                f.write(f"{i+1}\t{self.numbers[i]}\t{item}\t{data2[i]}\n")
                print(f"{i+1}\t{self.numbers[i]}\t{item}\t{data2[i]}\n")

if __name__ == "__main__":
    time_execution = 0
    start_time = time.time()
    if len(sys.argv) != 2:
        print("Usage: python convert_numbers.py <input_file>")
        sys.exit(1)
    filename = sys.argv[1]
    numbers = []
    with open(filename, 'r', encoding='utf-8') as file:
        strname = file.read().replace(",", " ").replace("\n", " ").replace(";", " ").split()
        for num in strname:
            try:
                numbers.append(float(num))
            except ValueError:
                print(f"Warning: '{num}' is not a valid number and will be skipped.")
    converter = NumberConverter(numbers)
    binary_nums = converter.to_binary()
    hex_nums = converter.to_hexadecimal()
    converter.save_to_file(binary_nums, hex_nums, "ConversionResult.txt")
    end_time = time.time()
    time_execution = end_time - start_time
    print(f"\nExecution time: {time_execution:.6f} seconds")
