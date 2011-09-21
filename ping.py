# Ping client demo
# Note: you may have to add a delay before replying in the ping server
# The busPirate USB is high-latency, and it takes time for the library
# to switch the radio back into receive mode to hear the reply

from nrf import BP_nRF
import time

bp = BP_nRF('/dev/ttyUSB0')

bp.set_outputs(power=True)
time.sleep(0.1)

bp.setRADDR('clie1')
bp.config()

print 'status', bin(bp.getStatus())

c = 0

while 1:
	bp.setTADDR('serv1')
	bp.send(str(c)+"test!")

	print c, bin(bp.getStatus()), bp.isSending()
	
	if bp.dataReady():
		print 'received', bp.getData()
	
	c = (c+1)%100
	
	time.sleep(1)
	

print 'status', bin(bp.getStatus())

time.sleep(0.1)

bp.set_outputs(power=False)
