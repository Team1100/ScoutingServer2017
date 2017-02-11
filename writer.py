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
    print "Writing ", datawrite
    f = open(filename,'w')
    for data in datawrite:
        if data!="":
            f.write(data + '\n')
    f.close()
    with open(filename) as f:
        lines = f.readlines()
    lines = [x.strip() for x in storedMatches]
    for line in lines:
        if line == "":
            lines.remove(line)
    f = open(filename, 'w')
    for data in datawrite:
        if data != "":
            f.write(data + '\n')
    f.close()