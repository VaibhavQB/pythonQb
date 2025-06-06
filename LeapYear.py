# Function to check whether the year is a leap year
def is_leap_year(year):

    leap = False  # Initialize leap year flag
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):  # Leap year condition
        leap = True  
        
    return f"{year} is a leap year." if leap else f"{year} is not a leap year."  

# Input from the user
year = int(input("Enter a year: "))
print(is_leap_year(year))