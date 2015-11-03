
import alsaaudio
import audioop
import time
import numpy as np
from matplotlib.pyplot import plot, draw, show, figure

x = np.array
f1 = figure()
af1 = f1.add_subplot(111)

#aplay -D hw:sndrpiwsp -r 44100 -c 2 -f S32_LE
card = 'hw:sndrpiwsp'

RATE = 44100
#RATE = str(RATE)

CHANNELS = 1
#CHANNELS = str(CHANNELS)

FORMAT = 'S32_LE'
DURATION = 5
#DURATION = str(DURATION) 

CHUNK = 1024

inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK, card)

inp.setchannels(CHANNELS)
inp.setrate(RATE)
inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)

inp.setperiodsize(CHUNK)

loops = 3000
Sample = np.zeros(1)
numbers = np.zeros(1)


while loops > 0:
    #print loops
    loops -=1
    l,data = inp.read()
    try: 
        if l:
            numbers = np.fromstring(data, dtype=np.int16)
            #print numbers.size
            
        if 'Sample' not in vars():
            Sample = numbers
        else:
            Sample = np.append(Sample, numbers)
    except:
        pass
        #need to figure out the error that happens here when it replys with non-int16 values. 

#	if Sample.size > 20000:
#		HalfPoint = len(Sample/2)#
#		Sample = Sample[HalfPoint-20000:HalfPoint+20000]

print "finished"
print Sample


plot(Sample)
show()







