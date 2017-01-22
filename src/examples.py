# Reading a CSV file.
# -------------------
# ... first let's inspect a file (assume we don't have Excel)

f = open("/path/to/data.csv")
data = f.readlines()
print(data[0])
print(data[0].split(','))


# Analyzing a Traffice Violations (truncated at 1000 lines of data)
# -----------------------------------------------------------------

from collections import Counter
reader = csv.reader(open("data/Traffic_Violations.csv"))

# ^ let's read the traffic violations and see which color vehicle gets the most
COLOR = 23
MAKE = 21
DL_STATE = -3

color_counter = Counter()
make_counter = Counter()
for row in reader:
    counter.update(row[COLOR])
    make_counter.update(row[MAKE])
counter.most_common(10)

# most common states?
states = [row[-3] for row in reader]
Counter(states).most_common(10)


# Analyzing Utility rates. (see data/iouzipcodes2011.csv)
# --------------------------------------------------------
# Google says the average US home usage is ~ 901 kWh per month.
# last column is `res_rate`
# `state` is index 3

from collections import defaultdict
from statistics import mean

# Build a dict of the utility costs per state
states = defaultdict(list)
reader = csv.reader(open('data/iouzipcodes2011.csv'))
for row in reader:
    states[row[3]].append(row[-1])

# figure out the mean cost in each state
for state, costs in states.items():
    try:
        averages[state] = mean([float(value) for value in costs])
    except (ValueError, TypeError):
        pass
print(averages)

# But what's the monthly cost in each state?
monthly = []
for state, rate in averages.items():
    monthly.append((state, rate * 901))  # 901 is the average usage in the US

print(monthly)
print(sorted(monthly))  # sort by state?
sorted(monthly, key=lambda t: t[1])


# Fetching things from an API (iTunes)
# ---------------------------------------------
# Fetching with urllib (python 3)
import json
from urllib import request
resp = urllib.request.urlopen("https://itunes.apple.com/search?term=beyonce")
print(resp.status)

data = resp.read()
data = json.loads(data.decode('utf-8'))
for entry in data['results']:
    print(entry['trackPrice'], entry['artistName'], entry['trackName'])


# Fetching with requests
import requests
resp = requests.get("https://itunes.apple.com/search?term=beyonce")
print(resp.status_code)

data = resp.json()
for entry in data['results']:
    print(entry['trackPrice'], entry['artistName'], entry['trackName'])
