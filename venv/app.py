""" A Python program that asks for a filename and looks for lines of a specific form,
    computes the average of the numbers, rounded to a single decimal place
    and prints out the average and the number of lines used for the computation.

    author: fizgi
    date: 08-Apr-2020
    python: v3.8.2
"""

import os
import re
from typing import List, IO


file_name: str = input("Enter the file name: ")
values: List[float] = []  # container for the values

try:  # to open the file
    path: IO = open(file_name, "r")
except FileNotFoundError:  # e.g. the user types in the wrong file name
    print(f"File '{file_name}' is not found.")
else:
    with path:  # close path after opening
        if os.path.getsize(file_name) == 0:  # check if the file is empty
            print(f"'{file_name}' is empty.")
        for line in path:
            match = re.findall(r"^New Revision: \d+$", line)  # find the match
            if match:
                number = re.findall(r"\d+$", line)[0]  # extract the number
                values.append(number)

    try:
        avg: float = sum(int(value) for value in values) / len(values)  # calculate the average
        print(f"Average: {round(avg, 1)}")
        print(f"Number of lines: {len(values)}")
    except ZeroDivisionError:  # no data, empty file (len == 0) will raise ZeroDivisionError
        print("No readable data to find the average and the number of lines.")  # handle the error
