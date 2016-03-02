#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

import webapp2

from google.appengine.ext import ndb
from google.appengine.api import mail
from datetime import datetime

from timesfriend import postWeibo
from timesfriend import generateTweet

class PostTimeToWeibo(webapp2.RequestHandler):
	def get(self):
		info = generateTweet()
		postWeibo(info)


class PostTimeToTwitter(webapp2.RequestHandler):
	def get(self):
		info = generateTweet()
		from tweetpost import postTweet
		postTweet(info)


APP = webapp2.WSGIApplication(
		[
			('/posttimetoweibo', PostTimeToWeibo),
			('/posttimetotwitter', PostTimeToTwitter),
		])
