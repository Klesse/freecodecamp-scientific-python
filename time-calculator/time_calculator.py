def add_time(start, duration, day=None):
  week = [
    'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday',
    'saturday'
  ]
  start_hour = start.split(':')[0]
  duration_hour, duration_minute = duration.split(':')
  start_minute, period = start.split(':')[1].split(' ')
  hours, minutes, next_day = 0, 0, 0
  minutes = int(start_minute) + int(duration_minute)
  if minutes >= 60:
    hours += 1
    minutes -= 60
  print(minutes)
  hours = hours + int(start_hour) + int(duration_hour)
  while hours > 12:
    hours -= 12
    if period[0] == "P":
      next_day += 1
      period = period.replace("P", "A")
    else:
      period = period.replace("A", "P")
  if hours == 12 and minutes > 0:
    if period[0] == "P":
      next_day += 1
      period = period.replace("P", "A")
    else:
      period = period.replace("A", "P")

  if len(str(minutes)) == 1:
    minutes = f'0{minutes}'
  if day != None:
    index = (next_day + week.index(day.lower())) % (len(week))
    #index = week.index(day.lower()) + next_day
    week_day = week[index]
    week_day = week_day[0].upper() + week_day[1:]
    if next_day == 1:
      new_time = f"{hours}:{minutes} {period}, {week_day} (next day)"
    elif next_day > 1:
      new_time = f"{hours}:{minutes} {period}, {week_day} ({next_day} days later)"
    else:
      new_time = f"{hours}:{minutes} {period}, {week_day}"
  else:
    if next_day == 1:
      new_time = f"{hours}:{minutes} {period} (next day)"
    elif next_day > 1:
      new_time = f"{hours}:{minutes} {period} ({next_day} days later)"
    else:
      new_time = f"{hours}:{minutes} {period}"
  return new_time
