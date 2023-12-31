def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    day = day_of_week
    weekdays = ["none", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    
    if day < 1 or day > 7:
        return "None"

    return weekdays[day]

print(weekday_name(-1))
print(weekday_name(0))
print(weekday_name(1))
print(weekday_name(2))
print(weekday_name(3))
print(weekday_name(4))
print(weekday_name(5))
print(weekday_name(6))
print(weekday_name(7))
print(weekday_name(8))
print(weekday_name(9))
    