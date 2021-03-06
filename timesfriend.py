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
def postWeibo(info):
	from weibo_tiny import Client
	client = Client(APP_KEY, APP_SECRET, REDIRECT_URL, username=USERNAME, password=PASSWORD)
	client.post('statuses/update', status=info)

def generateTweet():
	gmt = datetime.datetime.now()
	chinaTime = gmt + datetime.timedelta(hours=8)
	chinaTime.ctime()

	out = chinaTime.strftime("%H:%M")

	# https://tw.answers.yahoo.com/question/index?qid=20110701000016KK09368
	# 古代中国将一昼夜分为 12 个时辰，每个时辰分为 八刻. 每刻相当于现在的 15 分钟，所以 15 分钟又叫一刻钟, 午时三刻指的是午初三刻, 即 11 点 45 分. 
	options = { 23:u"子初",  0:u"子正",  1:u"丑初",  2:u"丑正",  3:u"寅初",  4:u"寅正",  5:u"卯初",  6:u"卯正", 
				7: u"辰初",  8:u"辰正",  9:u"巳初", 10:u"巳正", 11:u"午初", 12:u"午正", 13:u"未初", 14:u"未正", 
				15:u"申初", 16:u"申正", 17:u"酉初", 18:u"酉正", 19:u"戍初", 20:u"戍正", 21:u"亥初", 22:u"亥正",  }

	return u'=====【' + options[chinaTime.hour] + u'】=  ' + out + u'  ====='


###############################################################################
if __name__=="__main__":
	info = generateTweet()
	print info
	postWeibo(info)

	from tweetpost import postTweet
	postTweet(info)	
