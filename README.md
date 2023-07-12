# Time Calculator

Time Calculator is an interactive Python program that adds time durations and converts the result into different units. This tool is designed to handle time inputs in the format "H:MM:SS" and outputs the sum of these durations.

![Time Calculator Code](IMAGE_URL_1)

## How it Works

The program uses a `TimeDuration` class to represent a time duration. This class contains methods to add time durations, subtract them, and convert them into different units (hours, minutes, and seconds). Here's a brief overview of its methods:

- `__init__(self, time_str)`: Constructor that takes a time string and converts it into total seconds.
- `add(self, other)`: Adds another `TimeDuration` object to the current one.
- `subtract(self, other)`: Subtracts another `TimeDuration` object from the current one.
- `to_hours(self)`: Converts the time duration into hours.
- `to_minutes(self)`: Converts the time duration into minutes.
- `to_seconds(self)`: Converts the time duration into seconds.

The `interactive_time_calculator` function simulates an interactive session with the user, prompting for two time durations, adding them, and offering the option to convert the result into different units.

![Time Calculator Result](IMAGE_URL_2)

## Financial Implications

The Time Calculator program can serve as a foundation for financial applications, particularly in the area of time-value of money (TVM). The TVM concept is a fundamental concept in finance that money available now is worth more than the same amount in the future due to its potential earning capacity.

This tool can be integrated with other financial tools and formulas to calculate future and present values, taking into account interest rates and periods, which are often measured in terms of years, but with our tool can be measured with any time unit (hours, minutes, seconds).

For instance, it can be used with the compound interest formula, `A = P (1 + r/n)^(nt)`, where:
- `A` is the amount of money accumulated after n years, including interest.
- `P` is the principal amount (the initial amount of money).
- `r` is the annual interest rate (in decimal form).
- `n` is the number of times that interest is compounded per year.
- `t` is the time the money is invested for, in years.

In this context, our Time Calculator can help adjust the 't' value in the formula according to the specific time unit the user is interested in.

## Usage

To use the Time Calculator, simply run the `main.py` file in a Python environment and follow the prompts in the terminal. The program will ask you to enter two time durations and whether you want to convert the result into hours, minutes, or seconds.

## Contributing

This project is open for collaboration. If you're interested in improving the code or adding new features, please feel free to clone the repository, make your changes, and create a pull request.
