import sys
import gpsData as GpsData
import sms as Sms
from time import gmtime, strftime, sleep
#from email.mime.text import MIMEText

def main():
  #print "Starting.... %s"%(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
  # use GPS data for message
  coords = GpsData.getCoords()
  lat=str(coords['lat'])
  lon=str(coords['lon'])
  utc=str(coords['utc'])
  url = 'http://maps.google.com/maps?f=q&q=%s,%s' % (lat,lon)
  #msg = MIMEText(u'SITA Notification -- my location: '+url+' ('+utc+')')
  msg = 'SITA Notification -- my location: '+url+' ('+utc+')'
  #msg = 'SITA Notification -- my location: '+url+' ('+strftime("%Y-%m-%d %H:%M:%S", gmtime())+')'
  # set up recipients
  # get recipients from SIM card or props file from /boot/phonebook.properties
  phonebook = []
  phonebook = Sms.phonebook()
  if phonebook == []:
    # if no numbers on SIM card, check properties file
    filepath = '/boot/phonebook.properties'
    with open(filepath) as fp:
      line = fp.readline().replace('\r', '').replace('\n', '')
      if line != '':
        phonebook.append(line)
      while line:
        line = fp.readline().replace('\r', '').replace('\n', '')
        if line != '':
          phonebook.append(line)

  # broadcast location twice
  for addr in phonebook:
    Sms.sendsms(addr,msg)
    sleep(2)
  sleep(30)
  for addr in phonebook:
    Sms.sendsms(addr,msg)
    sleep(2)
  #print "Done... %s"%(strftime("%Y-%m-%d %H:%M:%S", gmtime()))

if __name__ == '__main__':
    main()

