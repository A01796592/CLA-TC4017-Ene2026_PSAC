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

if __name__ == "__main__":
    start_time = time.time()
    filenames = sys.argv[1:]
    with open("StatisticsResults.txt", "w", encoding="utf-8") as out:
        out.write(
            "File\t\tCount\tMean\t\tMedian\t\tMode\tStdDev\t\tVariance\n"
        )
        print("File\t\tCount\tMean\t\tMedian\t\tMode\tStdDev\t\tVariance")
        for fname in filenames:
            numbers = []
            with open(fname, "r", encoding="utf-8") as file:
                content = file.read().replace(",", " ").replace("\n", " ").replace(";", " ").split()
                for value in content:
                    try:
                        numbers.append(float(value))
                    except ValueError:
                        print(f"Warning: '{value}' in {fname} ignored")
            stats = Statistics(numbers)
            out.write(
                f"{fname}\t"
                f"{len(numbers)}\t"
                f"{stats.mean_calc():.4f}\t"
                f"{stats.median():.4f}\t"
                f"{stats.mode()}\t"
                f"{stats.standard_deviation():.4f}\t"
                f"{stats.variance():.4f}\n"
            )
            print(
                f"{fname}\t"
                f"{len(numbers)}\t"
                f"{stats.mean_calc():.4f}\t"
                f"{stats.median():.4f}\t"
                f"{stats.mode()}\t"
                f"{stats.standard_deviation():.4f}\t"
                f"{stats.variance():.4f}"
            )
    print("StatisticsResults.txt generated successfully")
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.6f} seconds")
