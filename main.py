#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

import webapp2

from google.appengine.ext import ndb
from google.appengine.api import mail
from datetime import datetime

from timesfriend import postWeibo
     
class DataRetriever(webapp2.RequestHandler):
    def get(self):
        postWeibo()


APP = webapp2.WSGIApplication(
        [
            ('/retrievedata', DataRetriever)
        ])
