import classes.py

fileName = "CONFIG.CSV"

file = open(fileName, "r")
line = file.readline()
components = []

while line != "":
	sepLine = line.split(",")
	compID = sepLine[0]
	name = sepLine[1]	
	dist = sepLine[4]
	qualities = sepLine[5].split("-")

	comp = Component(qualities, name, compID, tDate, dist)

	