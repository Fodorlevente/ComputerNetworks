import sys
from subprocess import PIPE, Popen
import datetime
import csv
import json
import platform

system = platform.system()
tracerouteName = "traceroute" if system == "linux" else "tracert"

mostFamousWebsites = []
pings = []
traces = []

with open('C:/Users/Levi/Desktop/top-1m.csv') as csvFile:
    spamReader = csv.reader(csvFile, delimiter=',')
    for row in spamReader:
        mostFamousWebsites.append(row[1])

for i in mostFamousWebsites[0:100]:
    p1 = Popen(["ping", '-n', '20', i], stdout=PIPE)
    pings.append({"target": i,
            "output":p1.communicate()}) 

    p2 = Popen([tracerouteName, i], stdout=PIPE)
    traces.append({"target": i,
            "output":p2.communicate()})

for i in mostFamousWebsites[-1:-1:100]:
    p1 = Popen(["ping", '-n', '10', i], stdout=PIPE)
    pings.append({"target": i,
            "output":p1.communicate()})
    
    p2 = Popen([tracerouteName, i], stdout=PIPE)
    traces.append({"target": i,
            "output":p2.communicate()})

date = datetime.datetime.now().strftime("%Y%m%d")

pingData = {"date": date,
        "system": system,
        "pings": pings }

tracerouteData = {"date": date,
                "system": system,
                "traces": traces}


with open("traceroute.json", "w") as write_file:
    json.dump(tracerouteData, write_file)

with open("ping.json", "w") as write_file:
    json.dump(pingData, write_file)