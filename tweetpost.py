#!/usr/bin/python
# -*- coding: utf-8 -*-

import tweetpony

def postTweet(text):
	consumer_key = "consumer_key"
	consumer_secret = "consumer_secret"
	access_token = "access_token"
	access_token_secret = "access_token_secret"

	api = tweetpony.API(consumer_key = consumer_key, consumer_secret = consumer_secret, access_token = access_token, access_token_secret = access_token_secret)
	user = api.user
	try:
		api.update_status(status = text)
	except tweetpony.APIError as err:
		print "Oops, something went wrong! Twitter returned error #%i and said: %s" % (err.code, err.description)
	else:
		print "Yay! Your tweet has been sent!"
