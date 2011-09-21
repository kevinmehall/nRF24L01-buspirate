This is a Python library for using Nordic Semiconductor's nRF24L01+ radios
using the DangerousPrototypes [BusPirate][buspirate] as a SPI adaptor.

It works nicely with the [$4 breakout boards from Itead Studio][itead]. 

Caveat: USB and the FTDI chip introduce a very high latency compared to the
low latency SPI controllers on a microcontroller. This will limit your data rate,
and specifically means that you will lose received packets if they come just
after sending a packet, before the computer has to put the radio back into receive
mode. So if you're doing a request/reply protocol, add a delay before the remote
device replies to give the BusPirate some time. This works for testing, but you
probably want to connect the radio to a microcontroller for more serious use.

For the other side of the radio link, see the following:

  - https://github.com/aaronds/arduino-nrf24l01
  - http://www.arduino.cc/playground/InterfacingWithHardware/Nrf24L01

### Pinout for the Itead module

	GND  -> GND
	3.3V -> VCC
	AUX  -> CE
	CS   -> CSN
	CLK  -> CLK
	MOSI -> MOSI
	MISO -> MISO


![Pinout diagram](http://kevinmehall.net/static/2011/buspirate_nordic_pinout.png)

[buspirate]: http://dangerousprototypes.com/bus-pirate-manual/
[itead]: http://iteadstudio.com/store/index.php?main_page=product_info&cPath=7&products_id=53&zenid=n3fhe16udvtbrhvqnepeg4pg65
