import math
import datetime

# metri
dist = 42000
#minute
time = 280
goal = 42000
age = 29

def running_calc(dist, time, goal, age):
    # Preveri parametre
    if not all(isinstance(p, int) and p > 0 for p in [dist, time, goal, age]):
        return "Neveljavni parametri 1"
    dist = dist/1000
    goal = goal/1000
    if age <= 5:
        return "premladi"
    elif age >= 90:
        return "prestari"
    else:
        exhoustion_factor = abs(age - 29) / 130 + 0.07
        exhoustion_factor = min(exhoustion_factor, 0.45)
    pace = time / dist
    if pace <= 2:
        return "Neveljavni parametri 2"
    E = round(0.05 * goal + 0.5*(pace),3)
    adjusted_pace = pace + (exhoustion_factor * pace)
    if goal >= dist:
        extra_time = (goal - dist) * adjusted_pace
        time_goal = extra_time + time
    else:
        time_goal = time - adjusted_pace*(dist - goal)
    try:
        time_goal = time - adjusted_pace*(dist - goal)
        time_goal_hours_A, time_goal_minutes_A = divmod(time_goal-E, 60)
        time_goal_hours_B, time_goal_minutes_B = divmod(time_goal+E, 60)
        time_goal_seconds_A = round((time_goal_minutes_A % 1) * 60)
        time_goal_seconds_B = round((time_goal_minutes_B % 1) * 60)
        time_goal_minutes_A = math.floor(time_goal_minutes_A)
        time_goal_minutes_B = math.floor(time_goal_minutes_B)
        time_string_A = f"{int(time_goal_hours_A):02d}:{int(time_goal_minutes_A):02d}:{int(time_goal_seconds_A):02d}"
        time_string_B = f"{int(time_goal_hours_B):02d}:{int(time_goal_minutes_B)+1:02d}:{int(time_goal_seconds_B):02d}"
        print("Ciljan cas:", [time_string_A, time_string_B])
    except ValueError:
        print("Neveljavni parametri 3")
