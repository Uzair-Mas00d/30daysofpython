# Day 17: 30 Days of python programming

# Exercises: Level 1

# Question 1
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
try:
    *nordic_countries ,es,ru = names
    print(f"{nordic_countries} {es} {ru}")

except Exception as e:
    print(e)