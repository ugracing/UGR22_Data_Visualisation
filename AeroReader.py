import matplotlib.pyplot as plt


fileName = "AeroData.csv"
sampling = 5


file = open(fileName)
line = file.readline()
lines = file.readlines()
lenFile = len(lines)
vals = {"1":[],"2":[],"3":[],"4":[],"5":[],"6":[],"7":[],"8":[]}
times = {"123":[],"456":[],"78":[]}


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
			times["123"].append(int(data[0].split(".")[3]))
		elif (multSensor == 1):
			vals["4"].append(int(data[4]))
			vals["5"].append(int(data[5]))
			vals["6"].append(int(data[6]))
			times["456"].append(int(data[0].split(".")[3]))
		elif (multSensor == 2):
			vals["7"].append(int(data[4]))
			vals["8"].append(int(data[5]))
			times["78"].append(int(data[0].split(".")[3]))

	except Exception as e:
		continue
		print(e)
		#print(data)



#print(times)
print(vals["6"])

plt.scatter(times["456"],vals["6"])
plt.show()
