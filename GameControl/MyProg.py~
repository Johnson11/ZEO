import matplotlib.pyplot as plt
import numpy as np

plt.ion()
x = np.arange(7)
freqs = []
medians = [[],[],[],[],[],[],[]]

print "Justin's Program ready!"
def getUpdate(object):
	print "Got update"
	freqs.append(object)
	visualize(object)

def visualize(object):
	sums = [[],[],[],[],[],[],[]]
	ranges = np.arange(7)
	trials = np.arange(len(freqs))
	for trial in trials:
		current = freqs[trial]
		for i in ranges:
			sums[i].append(current[i])
	
	for i in ranges:
		medians[i]= np.median(sums[i])

	plt.plot(medians)
	plt.draw()
