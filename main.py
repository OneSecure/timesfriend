#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

import webapp2

from google.appengine.ext import ndb
from google.appengine.api import mail
from datetime import datetime

from timesfriend import postWeibo
from timesfriend import generateTweet
     
class DataRetriever(webapp2.RequestHandler):
	def get(self):
		info = generateTweet()
		postWeibo(info)

		from tweetpost import postTweet
		postTweet(info)

APP = webapp2.WSGIApplication(
        [
            ('/retrievedata', DataRetriever)
        ])
