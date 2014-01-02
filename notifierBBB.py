

/*********************************************************************
 * notifier.py -- code which creates an emailnotifier on Beaglebone Black
 * Usage: Runs the program and turns ON the one of your LED whenever you are receiving email and 
  other LED goes ON when you are not having any new mails.        
 *********************************************************************/

#!/usr/bin/env python

import Adafruit_BBIO.GPIO as GPIO, feedparser, time
DEBUG = 1

USERNAME = "raspberrypitenet" #gmail username
PASSWORD = ":)" #enter your password within double quotes "

NEWMAIL_OFFSET = 0 # your unread message status 
MAIL_CHECK_FREQ = 1 # check your mail for every seconds

GPIO.setup("P9_12", GPIO.OUT) #set the pin as output 
GPIO.setup("P9_14", GPIO.OUT) #set the pin as output

while True:

newmails = int(feedparser.parse("https://" + USERNAME + ":" + PASSWORD +"@mail.google.com/gmail/feed/atom")["feed"]["fullcount"])

if DEBUG:
print "hi Praveen You have", newmails, "new email :)" # status message printing in your console

if newmails > NEWMAIL_OFFSET:
GPIO.output("P9_12",GPIO.HIGH) #led goes ON when mail drop to your inbox
GPIO.output("P9_14",GPIO.LOW) 
else:
GPIO.output("P9_12",GPIO.LOW) 
GPIO.output("P9_14",GPIO.HIGH) #led goes ON when no new mail in your inbox

time.sleep(MAIL_CHECK_FREQ)
