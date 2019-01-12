pi@pitestenv ~ $cu -l /dev/ttyAMA0

##### When plugged into USB with the header "A" pins enabled
##### (USB to SIM863) the device will be /dev/USB0

Type "AT" and hit Enter. You should see "OK" in response.
Type "AT+CMGF=1" and hit Enter. Same thing.

All looks good so far.

Type 
AT+CMGS="<phone number>"r
> Text message <ctrl+z>

Set the local SMSC：AT+CSCA="+14348082616" then Enter, get response “OK”.
Note: The SMSC will be different on different area. In this part, it is Shenzhen China as examples.
AT+CMGF=1: Set SMS to TEXT mode；
AT+CMGS="xxxxxxxxxxx” then Enter, set the number of receiver, then you will get response: 
>, edit the content of message (needn’t Enter at the end). After editing, send 1A in HEX format to 
send the message (0x1A is key value of “CTRL+Z”, it will tell the module to send). If the message is 
sent successfully, module will get the reply +CNGS: 174 as below figures.

AT+CMGS="14348082616"
> Test
>
+CMGS: 0

OK
~.

==================================================================================
SLEEP MODE

# Enable slow clock automatically after 5 second of inactivity
AT+CSCLK=2

# Wake with AT command, wait 100ms, then send AT command to disable slow clock

# Disable slow clock
AT+CSCLK=0

===================================================================================
LOCATION SERVICES

pi@pitestenv:~/dv/test $ cu -l /dev/ttyAMA0
Connected.
AT
OK
# Set the connection type to GPRS
AT+SAPBR=3,1,"Contype","GPRS"
OK

# Set APN to www - this will get you an IP
AT+SAPBR=3,1,"APN","www"
OK

# Enable GPRS
AT+SAPBR =1,1
OK

# Check the connection - if you have an IP, it's good
AT+SAPBR=2,1
+SAPBR: 1,1,"100.206.112.168"

OK

#CIPGSMLOC is used to retrieve network date/time/location
#Check date/time
AT+CIPGSMLOC=2,1
+CIPGSMLOC: 0,2018/04/21,18:53:41

OK

# Check the network location
AT+CIPGSMLOC=1,1
+CIPGSMLOC: 0,-78.483948,38.012264,2018/04/21,18:54:08

OK
### It's important to flip these since they come back long/lat
### and google maps prefers lat/long

===================================================================================


Find your IMEI (International Mobile station Equipment Identity) (Serial number identification)
AT+CGSN
867010032334642

OK
AT+GSN
867010032334642

OK

Find your IMSI (International Mobile Subscriber Identity)
AT+CIMI
204043922313966
OK

===================================================================================

Read some phone book entries

AT+CPBS?
+CPBS: "SM",2,50

OK
AT+CPBR=1,5
+CPBR: 1,"4348082616",129,""

+CPBR: 2,"4346073932",129,""

OK


~. hangup
