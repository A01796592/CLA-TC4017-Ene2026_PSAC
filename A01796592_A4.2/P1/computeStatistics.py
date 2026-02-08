""" Compute Statistics
CLA-T-1201 - A01796592 - Assignment 4.2 - Problem 1
This script computes the mean, median, mode, standard deviation , and variance of a list of numbers.
"""

import sys

class Statistics:
    """Class to compute statistical measures of a list of numbers."""
    def __init__(self, numbers):
        self.numbers = numbers

    def mean_calc(self):
        """Calculate the mean of the numbers."""
        mean = 0
        try:
            self.validate_numbers()
            for num in self.numbers:
                mean += num
            mean /= len(self.numbers)
        except ZeroDivisionError:
            raise ValueError("The list of numbers is empty.")
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
                        sorted_numbers[j] = sorted_numbers[j+1]
                        sorted_numbers[j+1] = sorted_numbers[j]
            if n % 2 == 0:
                median = (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
            else:
                median = sorted_numbers[n//2]
        except ZeroDivisionError:
            raise ValueError("The list of numbers is empty.")
        return median

    def mode(self):
        """Calculate the mode of the numbers."""
        frequency = {}
        mode = None
        max_freq = 0
        try:
            self.validate_numbers()
            for num in self.numbers:
                for i in range(len(self.numbers)):
                    if num == self.numbers[i]:
                        frequency[num] = frequency[num] + 1
            for i in range(len(self.numbers)):
                if frequency[self.numbers[i]] > max_freq:
                    max_freq = frequency[self.numbers[i]]
                    mode = self.numbers[i]
        except ZeroDivisionError:
            raise ValueError("The list of numbers is empty.")
        return mode

    def variance(self):
        """Calculate the variance of the numbers."""
        mean = self.mean_calc()
        variance = 0
        try:
            self.validate_numbers()
            for num in self.numbers:
                variance += (num - mean) ** 2
            variance /= len(self.numbers)
        except ZeroDivisionError:
            raise ValueError("The list of numbers is empty.")
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
        with open(file_name, "w") as f:
            f.write(f"Numbers: {self.numbers}\n")
            f.write(f"Mean: {self.mean_calc()}\n")
            f.write(f"Median: {self.median()}\n")
            f.write(f"Mode: {self.mode()}\n")
            f.write(f"Variance: {self.variance()}\n")
            f.write(f"Standard Deviation: {self.standard_deviation()}\n")
        print(f"Numbers: {self.numbers}")
        print(f"Mean: {self.mean_calc()}")
        print(f"Median: {self.median()}")
        print(f"Mode: {self.mode()}")
        print(f"Variance: {self.variance()}")
        print(f"Standard Deviation: {self.standard_deviation()}")

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename, 'r') as file:
        strname = file.read().strip().split(',')
        numbers = [float(num) for num in strname]
    stats = Statistics(numbers)
    stats.print_statistics()
