#! /usr/bin/python
 
import os
from gps import *
from time import *
import time
import threading
 
gpsd = None #seting the global variable
gpsp = None
 
class GpsPoller(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    global gpsd #bring it in scope
    gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
    self.current_value = None
    self.running = True #setting the thread running to true
 
  def run(self):
    global gpsd
    global gpsp
    while gpsp.running:
      gpsd.next()

def getCoords():
  global gpsp 
  gpsp = GpsPoller() # create the thread
  coords = {'lat':0.0,'lon':0.0,'utc':''}
  try:
    gpsp.start() # start it up
    while coords['lat']==0.0 or coords['lon']==0.0 or coords['utc']=='':
      # gps connection could take some time
      #print gpsd.fix.latitude,', ',gpsd.fix.longitude,'  Time: ',gpsd.utc
 
      #os.system('clear')
 
      #print
      #print ' GPS reading'
      #print '----------------------------------------'
      #print 'latitude    ' , gpsd.fix.latitude
      #print 'longitude   ' , gpsd.fix.longitude
      #print 'time utc    ' , gpsd.utc,' + ', gpsd.fix.time
      #print 'altitude (m)' , gpsd.fix.altitude
      #print 'eps         ' , gpsd.fix.eps
      #print 'epx         ' , gpsd.fix.epx
      #print 'epv         ' , gpsd.fix.epv
      #print 'ept         ' , gpsd.fix.ept
      #print 'speed (m/s) ' , gpsd.fix.speed
      #print 'climb       ' , gpsd.fix.climb
      #print 'track       ' , gpsd.fix.track
      #print 'mode        ' , gpsd.fix.mode
      #print
      #print 'sats        ' , gpsd.satellites
      coords['lat'] = gpsd.fix.latitude
      coords['lon'] = gpsd.fix.longitude
      coords['utc'] = gpsd.utc
      time.sleep(2) #set to a reasonable retry delay
    #print "\nKilling Thread..."
    gpsp.running = False
    gpsp.join() # wait for the thread to finish what it's doing 
  except (SystemExit):
    #print "\nKilling Thread..."
    gpsp.running = False
    gpsp.join() # wait for the thread to finish what it's doing
  #print "latitude: "+str(coords['lat'])
  #print "longitude: "+str(coords['lon'])
  #print "time: "+str(coords['utc'])
  #print "Done.\nExiting."
  return coords
 
if __name__ == '__main__':
  getCoords()
