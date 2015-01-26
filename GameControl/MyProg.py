import matplotlib.pyplot as plt
import numpy as np
import pong as p

#plt.ion()
x = np.arange(7)
freqs = []
medians = [[],[],[],[],[],[],[]]
labels = ["Delta","Theta","Alpha","Low Beta","Beta","High Beta","Gamma"]
labels2 = ['2-4','4-8','8-13','11-14','13-18','18-21','30-50']
concVal = 0
concState = 0



print "Justin's Program ready!"
def getUpdate(object):
	freqs.append(object)
	visualize(object)

def visualize(object):
	plt.clf()
	sums = [[],[],[],[],[],[],[]]
	ranges = np.arange(7)
	if len(freqs) > 4:	
		trials = [len(freqs)-4,len(freqs)-3,len(freqs)-2,len(freqs)-1] #median der letzten 4
	else:
		trials = np.arange(len(freqs))
	for trial in trials:
		current = freqs[trial]
		for i in ranges:
			sums[i].append(current[i])
	
	for i in ranges:
		medians[i]= np.median(sums[i])
	
	plt.plot(medians)
	plt.plot(object,'rx')
	plt.xticks(ranges,labels)
	plt.xlim(-1,7)
	plt.legend()
	
	
	#define if concentrated
	relaxation = (object[0]-medians[0])+(object[1]-medians[1])+(object[2]-medians[2])
	concentration = (object[3]-medians[3])+(object[4]-medians[4])+(object[5]-medians[5])
	concVal =  concentration - relaxation#concentration value
	if relaxation > 0 and concentration < 0:
		plt.title("Surely Not Concentrated")
		concState = 0
	elif relaxation < 0 and concentration > 0:
		plt.title("Surely Concentrated")
		concState = 3
	elif concVal < 0:
		plt.title("Not Concentrated ?")
		concState = 1
	elif concVal >= 0:
		plt.title("Concentrated ?")
		concState = 2
	else:
		print "Fail!"
	p.update(concState) #update conc val
	#plt.draw()


	
