import math
from poberi_utezi import fetch_utezi

# metri
dist = 42000
# sekunde
time = 130 * 60
goal = 84000
age = 29

utezi = fetch_utezi()


def find_closest_value(goal_value, values_list):
    closest = min(values_list, key=lambda x: abs(x[3] - goal_value))
    return closest

closest_utezi = find_closest_value(goal / 1000, utezi)

def running_calc(dist, time, goal, age, closest_utezi):
    opt_leta = 2023 - closest_utezi[1]
    # Preveri parametre
    if not all(isinstance(p, int) and p > 0 for p in [dist, time, goal, age]):
        return "Neveljavni parametri 1"
    dist = dist / 1000
    goal = goal / 1000
    if age <= 5:
        return "premladi"
    elif age >= 90:
        return "prestari"
    else:
        exhoustion_factor = abs(age/opt_leta-1)
        exhoustion_factor = min(exhoustion_factor, 0.05)
        exhoustion_factor_second = goal/10000000
    pace = (time/60)  / dist
    if pace <= 2:
        return "Neveljavni parametri 2"
    E = round(0.5 * goal + 0.5 * (pace), 3)
    utez = closest_utezi[2]/(60*1000)
    # dodana utez proporcionalno na tek, ki ga imajo
    adjusted_pace = (1-exhoustion_factor) * pace + (exhoustion_factor)*utez + exhoustion_factor_second*pace
    if goal >= dist:
        extra_time = (goal - dist) * adjusted_pace
        time_goal = extra_time + (time / 60)
    else:
        time_goal = (time / 60) - adjusted_pace * (dist - goal)
    try:
        time_goal_hours_A, time_goal_minutes_A = divmod(time_goal - E / 20, 60)  
        time_goal_hours_B, time_goal_minutes_B = divmod(time_goal + E / 2, 60)
        time_goal_seconds_A = round((time_goal_minutes_A % 1) * 60)
        time_goal_seconds_B = round((time_goal_minutes_B % 1) * 60)
        time_goal_minutes_A = math.floor(time_goal_minutes_A)
        time_goal_minutes_B = math.floor(time_goal_minutes_B)
        time_string_A = f"{int(time_goal_hours_A):02d}:{int(time_goal_minutes_A):02d}:{int(time_goal_seconds_A):02d}"
        time_string_B = f"{int(time_goal_hours_B):02d}:{int(time_goal_minutes_B) + 1:02d}:{int(time_goal_seconds_B):02d}"
        return f"Ciljan cas od {time_string_A} do {time_string_B}"
    except ValueError:
        return "Neveljavni parametri 3"

#result = running_calc(dist, time, goal, age, closest_utezi)
#print(result)

