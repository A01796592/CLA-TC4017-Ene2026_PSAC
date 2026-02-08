""" Compute Statistics
CLA-T-1201 - A01796592 - Assignment 4.2 - Problem 1
This script computes the mean, median, mode, standard deviation , and variance of a list of numbers.
"""

import sys
import time

class Statistics:
    """Class to compute statistical measures of a list of numbers."""
    def __init__(self, arg_numbers):
        self.numbers = arg_numbers

    def mean_calc(self):
        """Calculate the mean of the numbers."""
        mean = 0
        try:
            self.validate_numbers()
            for num in self.numbers:
                mean += num
            mean /= len(self.numbers)
        except ZeroDivisionError as exc:
            raise ValueError('The list of numbers is empty.') from exc
        return mean

    def median(self):
        """Calculate the median of the numbers."""
        median = 0
        sorted_numbers = self.numbers.copy()
        n = len(sorted_numbers)
        try:
            self.validate_numbers()
            for i in range(n):
                for j in range(0, n-i-1):
                    if sorted_numbers[j] > sorted_numbers[j+1]:
                        temp = sorted_numbers[j]
                        sorted_numbers[j] = sorted_numbers[j+1]
                        sorted_numbers[j+1] = temp
            if n % 2 == 0:
                index = int (n/2)
                median = (sorted_numbers[index - 1] + sorted_numbers[index]) / 2
            else:
                median = sorted_numbers[int(n/2)]
        except ZeroDivisionError as exc:
            raise ValueError('The list of numbers is empty.') from exc
        return median

    def mode(self):
        """Calculate the mode of the numbers."""
        frequency = {}
        mode = None
        max_freq = 0
        try:
            self.validate_numbers()
            for num in self.numbers:
                for i, val in enumerate(self.numbers):
                    if num == val:
                        frequency[num] = frequency.get(num, 0) + 1
            for i, num in enumerate(self.numbers):
                if frequency[self.numbers[i]] > max_freq:
                    max_freq = frequency[self.numbers[i]]
                    mode = self.numbers[i]
        except ZeroDivisionError as exc:
            raise ValueError('The list of numbers is empty.') from exc
        return mode

    def variance(self):
        """Calculate the variance of the numbers."""
        mean = self.mean_calc()
        variance = 0
        try:
            self.validate_numbers()
            for num in self.numbers:
                variance += (abs(num - mean) ** 2)
            variance /= len(self.numbers)
        except ZeroDivisionError as exc:
            raise ValueError('The list of numbers is empty.') from exc
        return variance

    def standard_deviation(self):
        """Calculate the standard deviation of the numbers."""
        variance = self.variance()
        std_dev = variance ** 0.5
        return std_dev

    def validate_numbers(self):
        """Validate that all elements in the list are numbers."""
        for num in self.numbers:
            if not isinstance(num, (int, float)):
                raise ValueError("All elements must be numbers.")

    def print_statistics(self):
        """Print and save the statistical measures to a file."""
        file_name = "StatisticsResults.txt"
        with open(file_name, "w", encoding='utf-8') as f:
            f.write(f"Count:\t{len(self.numbers)}\n")
            f.write(f"Mean:\t{self.mean_calc()} \n")
            f.write(f"Median:\t{self.median()} \n")
            f.write(f"Mode:\t{self.mode()} \n")
            f.write(f"Standard Deviation:\t{self.standard_deviation()} \n")
            f.write(f"Variance:\t{self.variance()}\n")
        print(f"Count:\t{len(self.numbers)}")
        print(f"Mean:\t{self.mean_calc()}")
        print(f"Median:\t{self.median()}")
        print(f"Mode:\t{self.mode()}")
        print(f"Standard Deviation:\t{self.standard_deviation()}")
        print(f"Variance:\t{self.variance()}")

if __name__ == "__main__":
    time_execution = 0
    start_time = time.time()
    filename = sys.argv[1]
    numbers = []
    with open(filename, 'r', encoding='utf-8') as file:
        strname = file.read().replace(",", " ").replace("\n", " ").replace(";", " ").split()
        for str_v in strname:
            try:
                numbers.append(float(str_v))
            except ValueError:
                print(f"Warning: '{str_v}' is not a valid number and will be skipped.")
    stats = Statistics(numbers)
    stats.print_statistics()
    end_time = time.time()
    time_execution = end_time - start_time
    print(f"\nExecution time: {time_execution:.6f} seconds")
