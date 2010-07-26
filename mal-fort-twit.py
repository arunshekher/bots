#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
#
# Malayalam Fortune Twitter program
#
#
# Copyright 2010 Hrishikesh K B <hrishi.kb@gmail.com>
# Copyright 2010 Ershad K <ershad92@gmail.com>
# Swathanthra Malayalam Computing(http://smc.org.in/)
#
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
# If you find any bugs or have any suggestions email: hrishi.kb@gmail.com
#
#
#            THANKS:-
#                   Ershad K <ershad92@gmail.com>
#                   Santhosh Thottingal <santhosh.thottingal@gmail.com>
#
#------------------------------------------------------------------------------------------------

import os, sys, codecs
import time
import twitter
import random

from jsonrpc import ServiceProxy

silpaService = ServiceProxy("http://smc.org.in/silpa/JSONRPC")

 
# Change the following values
username = 'USERNAME'
password = 'PASSWORD'
sleep_time = 1
fout = open('dataFile', 'a') #to create such a file
fout.close()
api = twitter.Api(username, password)
while True:
  time.sleep(sleep_time)
  word = ''
  timeline = api.GetReplies()
  for s in timeline:
	fort_keyword_find = -1
	check_duplicate = 0;
	tweet = s.user.name + "\t" + s.text
	fort_keyword_find = tweet.find("fortune") 
	if fort_keyword_find > 0:
		fin = open('dataFile', 'r')
		fin_contents = fin.read()
		check_duplicate = fin_contents.find(str(s.id))
		print check_duplicate
		fin.close()
	if check_duplicate < 0:
         	print "%s --> %s" % (s.user.name, s.text)
		fortun = silpaService.modules.Fortune.fortune('malayalam_proverbs')
		print fortun  #for debugging			
		fort = fortun [0:110]
		output = '@' + s.user.screen_name + ' ' + fort
		print output     
		api.PostUpdate (output)
		sleep_time = 30 #Adjusting time to make the bot twitter-server friendly
		fout = open('dataFile', 'a')
		text = '\n' #To write each status id in a new line
		text = text + str(s.id)
		fout.write(text)
		fout.close()


