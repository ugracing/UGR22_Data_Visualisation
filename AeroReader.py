import matplotlib.pyplot as plt


fileName = "AeroData.csv"
sampling = 5


file = open(fileName)
line = file.readline()
lines = file.readlines()
lenFile = len(lines)
vals = {"1":[],"2":[],"3":[],"4":[]}
times = []

for i in range(lenFile):
	if (i % 100/sampling != 0):
		continue
	try:
		line = lines[i]
		data = line.strip().split(",")
		#print(data)
		times.append(int(data[0].split(".")[3]))
		vals["1"].append(int(data[3]))
		vals["2"].append(int(data[4]))
		vals["3"].append(int(data[5]))
		vals["4"].append(int(data[6]))

	except Exception as e:
		continue
		print(e)
		#print(data)



print(max(times))

plt.scatter(times,vals["3"])
plt.show()
