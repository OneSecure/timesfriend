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

	info = u'【 #时间# 的 #朋友# #整点# #报时# 】' + u'＝＝＝＝＝  ' + out + u'  ＝＝＝＝＝' 
	client.post('statuses/update', status=info)

###############################################################################
if __name__=="__main__":
	postWeibo()
