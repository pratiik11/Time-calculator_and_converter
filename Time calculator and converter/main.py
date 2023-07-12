class TimeDuration:

    def __init__(self, time_str):
        self.hours, self.minutes, self.seconds = map(int, time_str.split(":"))
        self.total_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds

    def add(self, other):
        total_seconds = self.total_seconds + other.total_seconds
        return TimeDuration.from_seconds(total_seconds)

    def subtract(self, other):
        total_seconds = self.total_seconds - other.total_seconds
        if total_seconds < 0:
            raise ValueError("Resulting time cannot be negative")
        return TimeDuration.from_seconds(total_seconds)

    @staticmethod
    def from_seconds(seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return TimeDuration(f"{hours}:{minutes}:{seconds}")

    def to_hours(self):
        return self.total_seconds / 3600

    def to_minutes(self):
        return self.total_seconds / 60

    def to_seconds(self):
        return self.total_seconds

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

#  the user interactive function
def interactive_time_calculator():
    print("Welcome to the Time Calculator!")

    # These lines would normally take user input in a live Python environment
    time1_str = "4:57:00"  # input("Enter the first time duration (H:MM:SS): ")
    time1 = TimeDuration(time1_str)

    time2_str = "1:45:30"  # input("Enter the second time duration (H:MM:SS): ")
    time2 = TimeDuration(time2_str)

    time3 = time1.add(time2)
    print(f"The sum of {time1} and {time2} is {time3}")

    #  user choice for unit conversion
    choice = "seconds"  # input("Do you want to convert the result to 'hours', 'minutes', or 'seconds'? ")

    if choice == 'hours':
        print(f"The result is {time3.to_hours():.2f} hours")
    elif choice == 'minutes':
        print(f"The result is {time3.to_minutes():.2f} minutes")
    elif choice == 'seconds':
        print(f"The result is {time3.to_seconds():.2f} seconds")
    else:
        print(
            "Invalid choice. Please choose from 'hours', 'minutes', or 'seconds'.")


# Running the interactive function
interactive_time_calculator()
