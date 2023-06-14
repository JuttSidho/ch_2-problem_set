"""
implement a program that prompts the user for a time and outputs whether it’s breakfast time, 
lunch time, or dinner time. If it’s not time for a meal, don’t output anything at all. 
Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. And assume that 
each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime 
in between, it’s time for breakfast.
"""
def main():
    time = input('enter the time in formate hh:mm : ')
    hours = convert(time)

    # Check if it's breakfast time
    if 7.0 <= hours < 8.0:
        print("It's breakfast time!")

    # Check if it's lunch time
    elif 12.0 <= hours < 15.0:
        print("It's lunch time!")

    # Check if it's dinner time
    elif 18.0 <= hours < 22.0:
        print("It's dinner time!")


def convert(time):
    hours, minutes = map(int, time.split(':'))
    hours_float = hours + (minutes / 60)
    return hours_float


if __name__ == "__main__":
    main()