
def separate(reading, dist):
	sepRead = []
	rLen = len(reading)
	dists = list(dist)
	current = reading.copy()
	for i in dists:
			sepRead.append(list(current)[:(int(i)*2)-1])
			current.pop(:(int(i)*2)-1)
	return sepRead

#TODO write translate function

class Component:
  def __init__(self, qualities, name, compID, tDate, dist):

		self.qualities = qualities.split("-")
    self.reading = {}
    self.ID = compID + tDate
    self.compID = compID
    self.date = tDate
		self.name = name
		self.times = []

	def addReading(reading):
		values = separate(reading, dist) #for components that record multiple values in one go, code to separate the readings accordingly
		for i in range(len(self.qualities)):
				nReading = translate(values[i]) # as values are recorded as hex digits and may have more modifications these must be undone to get the actual value
				if self.reading[self.qualities[i]] != None:
					self.reading[self.qualities[i]].append(nReading)		
				else:
					self.reading[self.qualities[i]] = [nReading]

	def addTime(t):
				self.times.append(t) # where times is a list of strings that denote when the readings were taken, index 0 on this list will correspond to index 0 on the readings

