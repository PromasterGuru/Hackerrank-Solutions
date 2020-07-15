def timeConversion(s):
    meridiem = s[-2:]
    hours = int(s[:2])
    time = ''
    value = 0
    if(meridiem == 'PM'):
        value = 12 + hours
        if(value >= 24):
            value = 12
    elif(meridiem == 'AM'):
        value = hours
        if(hours >= 12):
            value = 0
    time += "{:02d}".format(value) + s[2:-2]
    return time
    
if __name__ == "__main__":
    time = '07:05:45PM'
    print(timeConversion(time))