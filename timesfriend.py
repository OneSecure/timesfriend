#!/usr/bin/python
# -*- coding: utf-8 -*-

#---------------------------------import---------------------------------------
import urllib2;
import urllib;
from urlparse import urlparse;
import re;
import os;
from io import BytesIO
import datetime, time

APP_KEY = u'APP_KEY'
APP_SECRET = u'APP_SECRET'
REDIRECT_URL = 'REDIRECT_URL'
USERNAME = u'username'
PASSWORD = u'password'

#------------------------------------------------------------------------------
def postWeibo():
	#respHtml = unicode(respHtml, "utf-8")

	from weibo_tiny import Client
	client = Client(APP_KEY, APP_SECRET, REDIRECT_URL, username=USERNAME, password=PASSWORD)

	gmt = datetime.datetime.now()
	chinaTime = gmt + datetime.timedelta(hours=8)
	chinaTime.ctime()

	out = chinaTime.strftime("%H:%M")

	options = { 23:u"子时", 00:u"子时", 01:u"丑时", 02:u"丑时", 03:u"寅时", 04:u"寅时", 05:u"卯时", 06:u"卯时", 
				07:u"辰时",  8:u"辰时",  9:u"巳时", 10:u"巳时", 11:u"午时", 12:u"午时", 13:u"未时", 14:u"未时", 
				15:u"申时", 16:u"申时", 17:u"酉时", 18:u"酉时", 19:u"戍时", 20:u"戍时", 21:u"亥时", 22:u"亥时",  }

	info = u'======== 【' + options[chinaTime.hour] + u'】 =  ' + out + u'  ========' 
	client.post('statuses/update', status=info)

###############################################################################
if __name__=="__main__":
	postWeibo()
