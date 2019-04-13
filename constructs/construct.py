import os

csv_path = os.path.join("C:\\Users\\chenx\\Desktop\\sql\\constructs","teaches.csv")

mask = [1,1,1,1,1]

vals = []

# Read csv into vals list
with open(csv_path, 'r') as csv:
    for line in csv.read().split("\n"):
        val = line.split(",")
        if(len(val) != len(mask)):
            continue
        vals.append(val)

# Builds format line
fmt="("
for i in range(len(mask)):
    if(i>0):
        fmt += ","
    if(mask[i]):
        fmt+="\""
    fmt += "{}"
    if(mask[i]):
        fmt+="\""
fmt += ")"

# Prints output with vals list
for val in vals:
    print(fmt.format(*val)+",")
