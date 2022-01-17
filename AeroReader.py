import matplotlib.pyplot as plt


fileName = "aerodataMult.csv"
sampling = 5


file = open(fileName)
line = file.readline()
lines = file.readlines()
lenFile = len(lines)
vals = {"1":[],"2":[],"3":[],"4":[],"5":[],"6":[],"7":[],"8":[],"Range":[],"Temp":[],"SensorNo":[],"firmVer":[]}
times = {"123":[],"456":[],"78":[]}

#convert shit yea?????


for i in range(lenFile):
	if (i % 100/sampling != 0):
		continue
	try:
		line = lines[i]
		data = line.strip().split(",")
		#print(data)
		multSensor = int(data[3])
		if (multSensor == 0):
			vals["1"].append(int(data[4]))
			vals["2"].append(int(data[5]))
			vals["3"].append(int(data[6]))
			vals["Range"].append(int(data[7]))
			times["123"].append(int(data[0].split(".")[3]))
		elif (multSensor == 1):
			vals["4"].append(int(data[4]))
			vals["5"].append(int(data[5]))
			vals["6"].append(int(data[6]))
			vals["Temp"].append(int(data[7]))
			times["456"].append(int(data[0].split(".")[3]))
		elif (multSensor == 2):
			vals["7"].append(int(data[4]))
			vals["8"].append(int(data[5]))
			vals["SensorNo"].append(int(data[6]))
			vals["firmVer"].append(int(data[7]))
			times["78"].append(int(data[0].split(".")[3]))

	except Exception as e:
		continue
		print(e)
		#print(data)

select = 5

if select < 4:
	pVal = str(select)
	tVal = "123"
elif select < 7:
	pVal = str(select)
	tVal = "456"
elif select < 7:
	pVal = str(select)
	tVal = "456"

#print(times)
print(vals[pVal])

plt.scatter(times[tVal],vals[pVal])
plt.show()
