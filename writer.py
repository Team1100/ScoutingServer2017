def write(data):
    print "Starting Write Functon"
    header = "Name,Match Number,Team,Position,High Fuel Auto,Low Fuel Auto,Gears Auto,Line Auto,High Fuel Teleop,Low Fuel Teleop,Gears Teleop,Climb,No Show,Broken,Disabled,Penalty,Bad Pilot"
    matches = [header]+data.splitlines()
    filename = "ScoutData.csv"
    with open(filename) as f:
        storedMatches = f.readlines()
    storedMatches = [x.strip() for x in storedMatches]
    print "Finished Reading: " ,storedMatches
    for match in matches:
        if match in storedMatches:
            matches.remove(match)
        if match=="":
            matches.remove(match)
    datawrite = storedMatches + matches
    cache = []
    for line in datawrite:
        if line == "":
            datawrite.remove(line)
        if line in cache:
            datawrite.remove(line)
        else:
            cache.append(line)
    print "Writing ", datawrite
    f = open(filename,'w')
    for data in datawrite:
        if data!="":
            f.write(data + '\n')
    f.close()
def pitWrite(data):
    print "Starting Pit Write Functon"
    header = "Team,Team Name,CIM Count,Drive Type,Intake Type,Shooter Type,Comments"
    info = [header] + data.splitlines()
    filename = "PitData.csv"
    with open(filename) as f:
        storedInfo = f.readlines()
    storedInfo = [x.strip() for x in storedInfo]
    print "PIT Finished Reading: ", storedInfo
    for match in info:
        if match in storedInfo:
            info.remove(match)
        if match == "":
            info.remove(match)
    infowrite = storedInfo + info
    cache = []
    for line in infowrite:
        if line == "":
            infowrite.remove(line)
        if line in cache:
            infowrite.remove(line)
        else:
            cache.append(line)
    print "Writing ", infowrite
    f = open(filename, 'w')
    for data in infowrite:
        if data != "":
            f.write(data + '\n')
    f.close()