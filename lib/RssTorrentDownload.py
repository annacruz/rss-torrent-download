#!/usr/bin/python

import httplib
import zlib
import feedparser


class RssTorrentDownload(object):

	def get_rss(self):

		conn = httplib.HTTPConnection( "tokyotosho.info" )
		conn.request( "GET", "/rss.php?filter=1", {}, { "Accept-Encoding": "compress, gzip" } )
		response = conn.getresponse()

		data = ''
		if response.status == 200:
			data = zlib.decompress( response.read(), 16 + zlib.MAX_WBITS )
		# else:
		# 	data = ''

		data = file( 'test_rss.xml' ).read()

		self.rss = feedparser.parse(data)

		# conn.close()

		return self

	def process_list(self):

		for entry in self.rss.entries:
			self.entries_list.append([ entry.title, entry.link ])

		return self

	def __init__(self):
		self.entries_list = []
		self.rss = []
