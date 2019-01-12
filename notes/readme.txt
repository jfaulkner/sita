Point the gps daemon to the GPS device on UART
sudo gpsd /dev/ttyAMA0 -F /var/run/gpsd.sock

Then run cgps to check the GPS data
cgps -s


Note to self:
If there's no data, double check that everything's plugged in.
Then run this:
pi@pitestenv:~/dv/test $ sudo nano /etc/default/gpsd
pi@pitestenv:~/dv/test $ sudo ln -s /lib/systemd/system/gpsd.service /etc/systemd/system/multi-user.target.wants/
pi@pitestenv:~/dv/test $ sudo gpsd /dev/ttyAMA0 -F /var/run/gpsd.sock
pi@pitestenv:~/dv/test $ gpsmon
pi@pitestenv:~/dv/test $ cgps

gpsmon and cgps -s should show data

####If they show NOFIX, run these, wait a few minutes and try again
pi@pitestenv:~/dv/test $ sudo killall gpsd
pi@pitestenv:~/dv/test $ sudo gpsd /dev/ttyAMA0 -F /var/run/gpsd.sock


Once data is being retrieved, python can get the GPS data
pi@pitestenv:~/dv/test $ python ~/dv/test/gpsdData.py
