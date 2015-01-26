
from ZeoRawData.BaseLink import BaseLink
from ZeoRawData.Parser import Parser
import matplotlib.pyplot as plt

 
f = []

def eventCallback(self, timestamp, version, event):
        # For debugging
	print event
 
def sliceCallback(slice):
    
	# Bad Signal
	if slice['BadSignal'] == True:
		print 'Empty waveform... Bad signal'
	
	elif slice['Waveform'] is not []:
		msg = [];	
		for w in slice['Waveform']:
	
			# message  
			msg.append(w)
		data(msg)

def data(fq):
	f=fq
 

# Initialize
port= "/dev/ttyUSB0"
link = BaseLink(port)
parser = Parser()
print "Zeo Connected..." 
 
# Add the Parser to the BaseLink's callback
link.addCallback(parser.update)
print "Raw data input initialized..."
 

 
# Add your callback functions
parser.addEventCallback(eventCallback)
parser.addSliceCallback(sliceCallback)
print 'Enabled callbacks'
 
# Start link
print "Start reading data:" 
link.run()
plt.figure()
plt.plot(f)
	
