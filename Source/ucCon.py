#    ucCon for Python, a class designed to make HTTP requests easy
#    Copyright (C) 2010 John Moore
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import httplib
import urllib

class ucCon:
	cookie = ''
	response = {"headers": "", "data": ""}

	def sendGET(self, host, url, cookie=''):
		conn = httplib.HTTPConnection(host)
		if not (cookie == ''):
			header = {"Cookie": cookie}
			conn.request("GET", url, "", header)
		else:
			conn.request("GET", url)
		response = conn.getresponse()
		self.response["headers"] = response.getheaders()
		self.cookie = self.ParseCookie(self.response['headers'])
		self.response["data"] = response.read()
	
	def sendPOST(self, host, url, data='', cookie=''):
		conn = httplib.HTTPConnection(host)
		a1 = a2 = []
		postdata = {}
		a1 = data.split("&")
		for p in a1:
			a2 = p.split("=", 2)
			postdata[a2[0]] = a2[1]
		params = urllib.urlencode(postdata)
		if not (cookie ==''):
			header = {"Cookie": cookie}
			conn.request("POST", url, params, header)
		else:
			conn.request("POST", url, params)
		response = conn.getresponse()
		self.response["headers"] = response.getheaders()
		self.cookie = self.ParseCookie(self.response['headers'])
		self.response["data"] = response.read()

	def __init__(self, cookie=''):
		self.cookie = cookie	

	def ParseCookie(self, headers):
		tempcookiename = tempcookievalue = cookiename = cookievalue = []
		cookiestr=''
		a1 = []
		for i in headers:
			if i[0] == 'set-cookie':
				a2 = a3 = a4 = []
				values = i[1].split(";")
				a2 = values[0].split(":")
				for v in a2:
					a3 = v.split("=", 1)
					tempcookiename.append(a3[0])
					tempcookievalue.append(a3[1])
		if (self.cookie.find(";") >= 0):
			a1 = a2 = a3 = []
			a1 = self.cookie.split("; ")
			for i in range(0, len(a1)):
				a2 = a1[i].split("=")
				tempcookiename.append(a2[0])
				a3 = a2[1].split(";")
				tempcookievalue.append(a4[0])
		for i in range(0, len(tempcookiename)):
			if not (tempcookiename[i] in cookiename):
				cookiename.append(tempcookiename[i])
				cookievalue.append(tempcookievalue[i])
		for i in range(0, len(cookiename)):
			cookiestr += cookiename[i] + "=" + cookievalue[i] +"; "
		return cookiestr[0:len(cookiestr)]