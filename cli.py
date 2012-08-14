#!/usr/bin/python

import sys
sys.path.append('./lib')

from pprint import pprint
from RssTorrentDownload import *

rtd = RssTorrentDownload()

rtd.get_rss().process_list()

print rtd.entries_list
