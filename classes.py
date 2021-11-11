#TODO write translate function

# qualities => Description of what is being recorded 
# reading => main disctionary where data is saved
# date => date where data was recorded (todays date as default)
# times => times data was recorded
# dist => distribution 

class Component:
	def __init__(self, qualities, name, compID, tDate, dist):
		self.qualities = qualities.split("-")
		self.reading = {}
		#self.ID = compID + self.fileName
		#self.fileName = ""
		self.compID = compID #int("0x" + compID, 16)
		self.date = tDate
		self.name = name
		self.times = []
		self.dist = dist

	def addFileName(self, fileName):
		self.fileName = fileName
		return

	def separate(self, reading, dist):
		sepRead = []
		dists = list(dist)
		current = reading.strip()
		#print(dists)
		for i in dists:
				sepRead.append(current[:(int(i)*2)])
				#print(current)
				if (int(i)*2) != len(current):
					for j in range((int(i)*2)):
						current = current[1:]
		return sepRead

	def translate(self, l):
		temp = (int(l,16))
		#print(l, temp)
		return temp

	def addReading(self, reading):
		values = self.separate(reading, self.dist) 
		#for components that record multiple values in one go, code to separate the readings accordingly
		for i in range(len(self.qualities)):
				nReading = self.translate(values[i]) # as values are recorded as hex digits and may have more modifications these must be undone to get the actual value
				if self.qualities[i] in self.reading.keys() :
					self.reading[self.qualities[i]].append(nReading)		
				else:
					self.reading[self.qualities[i]] = [nReading]
		return			

	def addTime(self, t):
		self.times.append(t) # where times is a list of strings that denote when the readings were taken, index 0 on this list will correspond to index 0 on the readings
		return

