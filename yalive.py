#!/usr/bin/env python
# coding: utf-8
import urllib2, time
import simplejson as json
from xml.dom.minidom import *

def yaLive():
  url = 'http://livequeries-front.corba.yandex.net/queries/?ll1=44.536113,22.172272&ll2=52.432819,39.548480&limit=50&nc=0.16124989045783877'
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	page = parseString(response.read())
	query = page.getElementsByTagName('at')

	for node in query:
		city = getCity(node.childNodes[0].getAttribute("lng"), node.childNodes[0].getAttribute("lat"))
		if u"Украина" in city:
			print '   \033[0;33m%s\033[1;m\t[%s]' % (node.childNodes[0].getAttribute("text"), city)
			time.sleep(1)


def getCity(lng, lat):
	try:
		url = 'https://geocode-maps.yandex.ru/1.x/?geocode=%s,%s' % (lng, lat)
		req = urllib2.Request(url)
		response = urllib2.urlopen(req)
		page = parseString(response.read())

		query = page.getElementsByTagName('GeocoderMetaData')
		text = query[0].getElementsByTagName('text')

		for val in text:
			return val.childNodes[0].nodeValue
	except:
		return 'Error!'

while True:
	yaLive()
