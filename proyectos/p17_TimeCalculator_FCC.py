# Proyecto 'Arithmetic Formatter' perteneciente al curso 'Scientific Computing with Python' de FCC

def add_time(start_time, duration, start_day=None):
    '''
    Función que recibe una hora de inicio y una duración y devuelve
    una hora de finalización y el tiempo transcurrido + el día de la semana 
    '''
    # diccionario para mapear los nombres de los días de la semana a valores numéricos,
    # para facilitar el cálculo del día de la semana cuando se proporciona un día de inicio.
    days = {
        'monday': 0,
        'tuesday': 1,
        'wednesday': 2,
        'thursday': 3,
        'friday': 4,
        'saturday': 5,
        'sunday': 6
    }

    start_time, period = start_time.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    start_hour = start_hour % 12

    if period.lower() == 'pm':
        start_hour += 12

    dur_hour, dur_minute = map(int, duration.split(':'))

    total_start_minutes = start_hour * 60 + start_minute
    total_dur_minutes = dur_hour * 60 + dur_minute
    total_minutes = total_start_minutes + total_dur_minutes

    new_hour = total_minutes // 60
    new_minute = total_minutes % 60

    period = 'PM' if new_hour < 12 else 'AM'
    if new_hour >= 12:
        period = 'AM' if new_hour >= 24 else 'PM'
        new_hour = new_hour % 12

    if new_hour == 0:
        new_hour = 12

    new_time = f"{new_hour}:{new_minute:02d} {period}"

    if start_day:
        start_day = start_day.lower()
        start_day_index = days[start_day]
        days_passed = (start_day_index + new_hour // 24) % 7
        new_day = list(days.keys())[list(days.values()).index(days_passed)]
        new_time += f", {new_day.capitalize()}"

    if total_minutes >= 24 * 60:
        days_passed = total_minutes // (24 * 60)
        if days_passed == 1:
            new_time += " (next day)"
        else:
            new_time += f" ({days_passed} days later)"

    return new_time

# TEST CASES:
print(add_time("3:00 PM", "3:10"))
print('6:10 PM - Test Case 1')
print('---------------------------------------------')

print(add_time("11:30 AM", "2:32", "Monday"))
print('2:02 PM, Monday - Test Case 2')
print('---------------------------------------------')

print((add_time("11:43 AM", "00:20")))
print('12:03 PM - Test Case 3')
print('---------------------------------------------')

print(add_time("10:10 PM", "3:30"))
print('1:40 AM (next day) - Test Case 4')
print('---------------------------------------------')

print(add_time("11:43 PM", "24:20", "thursday"))
print('12:03 AM, Thursday (2 days later) - Test Case 5')
print('---------------------------------------------')

print(add_time("6:30 PM", "205:12"))
print('7:42 AM (9 days later) - Test Case 6')
print('---------------------------------------------')
