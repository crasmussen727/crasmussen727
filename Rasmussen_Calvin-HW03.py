#Name: Calvin Rasmussen 
#Lab Section: 13
#Submission Date: 11/05/24
#Sources, help given to/received from: Notes from class, and notes from designing with devices
def is_leap_year(year):
    # Check if a given year is a leap year
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year):
    # Define days in each month, taking leap years into account
    month_days = {
        1: 31, 2: 29 if is_leap_year(year) else 28, 3: 31, 4: 30,
        5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    return month_days.get(month, 0)

def is_valid_date(month, day, year):
    # Check if month is between 1 and 12, day is within month bounds
    if month < 1 or month > 12:
        return False
    if day < 1 or day > days_in_month(month, year):
        return False
    return True

def calculate_jan_first_day(year):
    # Calculate the weekday of January 1st for a given year
    y = year - 1
    jan_first_day = (36 + y + (y // 4) - (y // 100) + (y // 400)) % 7
    return jan_first_day

def calculate_day_of_week(month, day, year, jan_first_day):
    # Calculate the day of the week for the specified date
    day_counts = [31, 29 if is_leap_year(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_of_year = sum(day_counts[:month-1]) + day - 1
    return (jan_first_day + day_of_year) % 7

def main():
    # Dictionary to map day numbers to names
    days_of_week = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 
                    4: "Thursday", 5: "Friday", 6: "Saturday"}
    
    # Input date and split into components
    date_input = input("Enter a date (MM/DD/YYYY): ")
    try:
        month, day, year = map(int, date_input.split("/"))
    except ValueError:
        print(f"{date_input} Invalid Date")
        return

    # Check if the date is valid
    if not is_valid_date(month, day, year):
        print(f"{date_input} Invalid Date")
        return

    # Calculate the weekday for January 1st of the given year
    jan_first_day = calculate_jan_first_day(year)
    
    # Calculate the day of the week for the given date
    day_of_week = calculate_day_of_week(month, day, year, jan_first_day)
    
    # Output the result
    print(f"{date_input} {days_of_week[day_of_week]}")

# Run the program
if __name__ == "__main__":
    main()