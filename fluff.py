import random
from writer import write
random.seed("TURTWIG")
lines = ["Name,Match Number,Team,Position,High Fuel Auto,Low Fuel Auto,Gears Auto,Line Auto,High Fuel Teleop,Low Fuel Teleop,Gears Teleop,Climb,No Show,Broken,Disabled,Penalty,Bad Pilot"]
teams = "1100,195,190,125,4048,467,69,78,254,2648,839,3930,5400,1735,1768,1519".split(",")
for team in teams:
    for i in range(12):
        data = ["Auto Scouter"]
        data.append(str(i+random.randint(1,61)))
        data.append(str(team))
        data.append(str(random.randint(0,6)))
        data.append(str(random.randint(0,random.randint(1,10))))
        data.append(str(random.randint(0,random.randint(1,10))))
        data.append(str(random.randint(0,1)))
        data.append(str(random.randint(0,1)==1))
        data.append(str(random.randint(0, random.randint(50,150))))
        data.append(str(random.randint(0, random.randint(50,150))))
        data.append(str(random.randint(0, 12)))
        data.append(str(random.randint(0,1) == 1))
        data.append(str(random.randint(0, 30) == 1))
        data.append(str(random.randint(0, 30) == 1))
        data.append(str(random.randint(0, 30) == 1))
        data.append(str(random.randint(0, 30) == 1))
        data.append(str(random.randint(0, 30) == 1))
        l = ""
        for d in data:
            l+=d+","
        lines.append(l[0:-1])
packet = ""
for line in lines:
    print line
    packet+=line+"\n"
print "Auto Scouter is done for the day!"

        #josh is less hunk than zach hunk.
        #Zach is approx. 1.333333333333333333 (4/3) hunk
        #Josh averages a daily value of 0.36787944117 (e^-1) hunk.
