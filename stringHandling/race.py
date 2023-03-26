gender = "Boys"
distance = "400"
event = "Relay"
age_group = "Under 13"

length = len(age_group)
race = gender[0] + distance + event[0:1] + age_group[0] + age_group[length-2:length-1]

print(race)