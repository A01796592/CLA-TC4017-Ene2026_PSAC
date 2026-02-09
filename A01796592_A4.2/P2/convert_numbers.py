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
                elif n < 0:
                    n = abs(n)
                    while n > 0:
                        binary = str(n % 2) + binary
                        n //= 2
                    binary = binary.zfill(10)
                    binary = ''.join('1' if b == '0' else '0' for b in binary)
                    binary = format(int(binary, 2) + 1, f'0{10}b')
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
                n = int(num_to_hex)
                hex_digits = "0123456789ABCDEF"
                hexadecimal = ""
                if n == 0:
                    hexadecimal = "0"
                elif n < 0:
                    n = abs(n)
                    while n > 0:
                        hexadecimal = hex_digits[n % 16] + hexadecimal
                        n //= 16
                    hexadecimal = hexadecimal.zfill(10)
                    hexadecimal = ''.join(hex_digits[15 - hex_digits.index(h)] for h in hexadecimal)
                    hexadecimal = format(int(hexadecimal, 16) + 1, f'0{10}X')
                    hexadecimal = "0x" + hexadecimal
                else:
                    while n > 0:
                        hexadecimal = hex_digits[n % 16] + hexadecimal
                        n //= 16
                    hexadecimal = "0x" + hexadecimal
                hex_numbers.append(hexadecimal)
            except ValueError:
                print(f"Warning: '{num_to_hex}' is not a valid integer and will be skipped.")
        return hex_numbers

if __name__ == "__main__":
    start_time = time.time()
    filenames = sys.argv[1:]
    with open("ConversionResult.txt", "w", encoding="utf-8") as out:
        out.write("ITEM\tFILE\tTC\tBIN\tHEX\n")
        print("ITEM\tFILE\tTC\tBIN\tHEX")
        for fname in filenames:
            item = 1
            numbers = []
            with open(fname, 'r', encoding='utf-8') as file:
                tokens = (
                    file.read()
                    .replace(",", " ")
                    .replace("\n", " ")
                    .replace(";", " ")
                    .split()
                )
                for num in tokens:
                    try:
                        numbers.append(int(num))
                    except ValueError:
                        print(f"Warning: '{num}' in {fname} skipped")
            converter = NumberConverter(numbers)
            bin_nums = converter.to_binary()
            hex_nums = converter.to_hexadecimal()
            for i, num in enumerate(numbers):
                out.write(
                    f"{item}\t{fname}\t{num}\t{bin_nums[i]}\t{hex_nums[i]}\n"
                )
                print(
                    f"{item}\t{fname}\t{num}\t{bin_nums[i]}\t{hex_nums[i]}"
                )
                item += 1
            out.write("\n")
    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.6f} seconds")
