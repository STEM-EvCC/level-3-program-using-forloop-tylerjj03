mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]
print("Total number of missions: " + str(len(mission_names)))

print("Number of successful missions: " + str(sum(mission_success)))

missionSuccessRate = ((sum(mission_success)) / (len(mission_names))) * 100

print("Success rate: " + str(round(missionSuccessRate, 2)) + "%")

print("Missions launched before the year 2000: ") 

for i, j in zip(mission_names, mission_years):
    if (j < 2000):
        print(i)

