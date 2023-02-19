# Implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. If it’s not time for a meal, 
# don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. And assume that each meal’s time range is inclusive.
# For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

def main():
    time = input("What time is it? ")
    convert(time)

def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours) * 60
    minutes = int(minutes)
    t = hours + minutes
    if t >= 420 and t <= 480:
        print("breakfast time")
    elif t >= 720 and t <= 790:
        print("lunch time")
    elif t >= 1080 and t <= 1140:
        print("dinner time")

if __name__ == "__main__":
    main()
