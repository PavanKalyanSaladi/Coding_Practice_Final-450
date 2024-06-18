'''
Find Number of days Above Average Temperature

Input:-
How many day's temperature?  2
Day 1's high temp: 1
Day 2's high temp: 2

Ouptut:-
Average = 1.5
1 day(s) above average
'''

def days_above_average(days):
    temperature = []
    total = 0
    count = 0
    for day in range(1, days + 1):
        nextDay = int(input("Day " +  str(day) + "'s high temp: "))
        total += nextDay
        temperature.append(nextDay)
    
    for day in range(days):
        if temperature[day] > round(total / days, 2):
            count += 1
    
    print("Average = ", round(total / days, 2))
    print(f"{count} day(s) above average")

days_above_average(int(input("How many day's temperature? ")))