#Part 2: Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight). If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm). Write a Python program to solve the general version of the above problem. Ask the user for the time now (in hours) and then ask for the number of hours to wait for the alarm. Your program should output what the time will be on a 24-hour clock when the alarm goes off.
def main():
    #Get the current time in hours
    currentTime = int(input('Enter the current time in hours using 24-hour format: '))
    #Get the number of hours to wait until the alarm goes off
    alarmWait = int(input('Enter the number of hours until the alarm goes off: '))
    #Calculate the time it will be when the alarm goes off
    alarmTime = (currentTime + alarmWait) % 24

    #Print the time it will be when the alarm goes off
    print('The alarm will go off at ',alarmTime)
if __name__ == '__main__': main()
