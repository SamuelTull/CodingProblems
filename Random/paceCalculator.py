def parseTime(time):
    """
    takes a time in seconds and returns a string in the format hh:mm:ss or mm:ss or ss.sss
    """
    hours = int(time // 3600)
    minutes = int((time // 60) % 60)
    seconds = int(time % 60)
    if hours > 0:
        return f"{hours}:{minutes:02d}:{seconds:02d}"
    if minutes > 0:
        return f"{minutes}:{seconds:02d}"
    milliseconds = int((time % 1) * 100)
    return f"{seconds}.{milliseconds:02d}s"


def parsePace(pace):
    """
    Converts a time in seconds per kilometer to mm:ss per km and per mile, and returns both.
    """
    return f"{parseTime(pace)}/km | {parseTime(pace * 1.60934)}/mile"


def get_time():
    """
    if time == None: Asks the user to input a time in hours, minutes, and seconds
    returns the time in seconds and as string
    """
    print("\nTime?")
    hours = input("Hours? ")
    hours = float(hours) * 3600 if hours else 0.0
    minutes = input("Minutes? ")
    minutes = float(minutes) * 60 if minutes else 0.0
    seconds = input("Seconds? ")
    seconds = float(seconds) if seconds else 0.0
    time = hours + minutes + seconds
    return time, parseTime(time)


def get_distance():
    """
    Asks the user to input a distance and returns the distance in kilometers.
    """
    print("\nDistance?")
    print("Options: Kilometers, Miles, Marathon")
    option = input("Option? (1-3) ")
    if option not in ["1", "2", "3"]:
        return get_distance()
    distance = float(input("Distance? "))
    if option == "1":
        return distance, f"{distance} km"
    elif option == "2":
        return distance * 1.60934, f"{distance} miles"
    elif option == "3":
        return distance * 42.195, f"{distance} marathon"


def get_pace():
    """
    Asks the user to input a pace in minutes and seconds per kilometer/mile and returns the pace in seconds per kilometer.
    """
    print("\nPace ")
    print("Options: per km, per mile")
    option = input("Option? (1-2) ")
    if option not in ["1", "2"]:
        return get_pace()

    minutes = input("Minutes? ")
    minutes = float(minutes) * 60 if minutes else 0.0
    seconds = input("Seconds? ")
    seconds = float(seconds) if seconds else 0.0

    if option == "1":
        return minutes + seconds
    elif option == "2":
        return (minutes + seconds) / 1.60934


def printKeyTimes(pace):
    print("100m:", parseTime(pace * 0.1))
    print("200m:", parseTime(pace * 0.2))
    print("400m:", parseTime(pace * 0.4))
    print("800m:", parseTime(pace * 0.8))
    print("1k:", parseTime(pace * 1))
    print("1 mile:", parseTime(pace * 1.60934))
    print("5k:", parseTime(pace * 5))
    print("10k:", parseTime(pace * 10))
    print("Half marathon:", parseTime(pace * 21.0975))
    print("Marathon:", parseTime(pace * 42.195))


def printKeyMarathonTimes():
    for time in range(120, 301, 15):
        pace = time * 60 / 42.195
        print(parsePace(pace), "|", parseTime(pace * 42.195) + " marathon")


option = input("Have pace? (Y/N) ")

if option == "Y" or option == "y":
    pace = get_pace()
else:
    distance, distance_str = get_distance()
    time, time_str = get_time()
    print("------------------")
    print("Distance:", distance_str)
    print("Time:", time_str)
    pace = time / distance


print("------------------")
print("Pace:", parsePace(pace))
print("------------------")
printKeyTimes(pace)
print("------------------")
printKeyMarathonTimes()
