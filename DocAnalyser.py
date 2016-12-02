#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Document Analyser
By Nicholas Robinson
"""

from user_agents import parse
from collections import Counter
import re

from DataTypes import Document as Doc
from DataTypes import User as User
from IDDictionary import IDDictionary as Dic

class DocAnalyser():

	def __init__(self, dd, ud, al):
		self.dd = dd
		self.ud = ud
		self.al = al

	"""
	Task 2a
	"""
	def docCountries(self, docID):
		if self.dd.contains(docID):
			doc = self.dd.get(docID)
			return Counter(doc.getCountries()).most_common()
		else:
			raise BadIDException("ID %s does not exist"%(docID),str(docID))
			return None

	"""
	Task 2b
	"""
	def docContinents(self, docID):
		if self.dd.contains(docID):
			doc = self.dd.get(docID)
			continentlist = []
			for country in doc.getCountries():
				continentlist.append(self.countryToContinent(country))
			return Counter(continentlist).most_common()
		else:
			raise BadIDException("ID %s does not exist"%(docID),str(docID))
			return None

	"""
	Task 3
	"""
	def userAgents(self):
		tempal = (agent for agent in self.al)
		return Counter(tempal).most_common()

	"""
	Task 3a
	"""
	def userAgentsString(self):
		tempal = (str(parse(agent)) for agent in self.al)
		return Counter(tempal).most_common()

	"""
	Task 3b
	"""
	def userAgentsStringBrowser(self):
		tempal = (parse(agent).browser.family for agent in self.al)
		return Counter(tempal).most_common()

	"""
	Task 4
	"""
	def topTenReaders(self):
		topten = []
		userList = self.ud.getList()
		for user in userList:
			topten.append((user,user.docTotalTime))
		topten.sort(key=lambda tup: tup[1], reverse=True)
		return topten[:10]

	"""
	Task 5a
	"""
	def docReaders(self, docID):
		if not self.dd.contains(docID):
			raise BadIDException("ID %s does not exist"%(docID),str(docID))
			return None
		doc = self.dd.get(docID)
		return doc.usersRead

	"""
	Task 5b
	"""
	def readDocs(self, userID):
		if not self.ud.contains(userID):
			raise BadIDException("ID %s does not exist"%(userID),str(userID))
			return None
		user = self.ud.get(userID)
		return user.getDocs()

	"""
	Task 5d & 5e
	"""
	def alsoLiked(self, docID, sortFun=None, userID=None):
		if not self.dd.contains(docID):
			raise BadIDException("ID %s does not exist"%(docID),str(docID))
			return None
		if sortFun is None:
			sortFun = self.noSort
		totalUsers = self.docReaders(docID)
		docTimeListFull=[]
		doc = self.dd.get(docID)
		if userID is None:
			for user in totalUsers:
				tempDict = dict(user.getDocTimes())
				if doc in tempDict:
					del tempDict[doc]
				tempList = [(doc,tempDict[doc]) for doc in tempDict]
				docTimeListFull += tempList
		else:
			if not self.ud.contains(userID):
				raise BadIDException("ID %s does not exist"%(userID),str(userID))
				return None
			for user in totalUsers:
				if user.id == userID: # Remove searching user from temp user list
					continue
				tempDict = dict(user.getDocTimes())
				if doc in tempDict:
					del tempDict[doc]
				tempList = [(doc,tempDict[doc]) for doc in tempDict]
				docTimeListFull += tempList
		return sortFun(docTimeListFull)

	def noSort(self, data):
		return data

	def countryToContinent(self, country):
		country_to_continent = {
		'AF' : 'AS',
		'AX' : 'EU',
		'AL' : 'EU',
		'DZ' : 'AF',
		'AS' : 'OC',
		'AD' : 'EU',
		'AO' : 'AF',
		'AI' : 'NA',
		'AQ' : 'AN',
		'AG' : 'NA',
		'AR' : 'SA',
		'AM' : 'AS',
		'AW' : 'NA',
		'AU' : 'OC',
		'AT' : 'EU',
		'AZ' : 'AS',
		'BS' : 'NA',
		'BH' : 'AS',
		'BD' : 'AS',
		'BB' : 'NA',
		'BY' : 'EU',
		'BE' : 'EU',
		'BZ' : 'NA',
		'BJ' : 'AF',
		'BM' : 'NA',
		'BT' : 'AS',
		'BO' : 'SA',
		'BQ' : 'NA',
		'BA' : 'EU',
		'BW' : 'AF',
		'BV' : 'AN',
		'BR' : 'SA',
		'IO' : 'AS',
		'VG' : 'NA',
		'BN' : 'AS',
		'BG' : 'EU',
		'BF' : 'AF',
		'BI' : 'AF',
		'KH' : 'AS',
		'CM' : 'AF',
		'CA' : 'NA',
		'CV' : 'AF',
		'KY' : 'NA',
		'CF' : 'AF',
		'TD' : 'AF',
		'CL' : 'SA',
		'CN' : 'AS',
		'CX' : 'AS',
		'CC' : 'AS',
		'CO' : 'SA',
		'KM' : 'AF',
		'CD' : 'AF',
		'CG' : 'AF',
		'CK' : 'OC',
		'CR' : 'NA',
		'CI' : 'AF',
		'HR' : 'EU',
		'CU' : 'NA',
		'CW' : 'NA',
		'CY' : 'AS',
		'CZ' : 'EU',
		'DK' : 'EU',
		'DJ' : 'AF',
		'DM' : 'NA',
		'DO' : 'NA',
		'EC' : 'SA',
		'EG' : 'AF',
		'SV' : 'NA',
		'GQ' : 'AF',
		'ER' : 'AF',
		'EE' : 'EU',
		'ET' : 'AF',
		'FO' : 'EU',
		'FK' : 'SA',
		'FJ' : 'OC',
		'FI' : 'EU',
		'FR' : 'EU',
		'GF' : 'SA',
		'PF' : 'OC',
		'TF' : 'AN',
		'GA' : 'AF',
		'GM' : 'AF',
		'GE' : 'AS',
		'DE' : 'EU',
		'GH' : 'AF',
		'GI' : 'EU',
		'GR' : 'EU',
		'GL' : 'NA',
		'GD' : 'NA',
		'GP' : 'NA',
		'GU' : 'OC',
		'GT' : 'NA',
		'GG' : 'EU',
		'GN' : 'AF',
		'GW' : 'AF',
		'GY' : 'SA',
		'HT' : 'NA',
		'HM' : 'AN',
		'VA' : 'EU',
		'HN' : 'NA',
		'HK' : 'AS',
		'HU' : 'EU',
		'IS' : 'EU',
		'IN' : 'AS',
		'ID' : 'AS',
		'IR' : 'AS',
		'IQ' : 'AS',
		'IE' : 'EU',
		'IM' : 'EU',
		'IL' : 'AS',
		'IT' : 'EU',
		'JM' : 'NA',
		'JP' : 'AS',
		'JE' : 'EU',
		'JO' : 'AS',
		'KZ' : 'AS',
		'KE' : 'AF',
		'KI' : 'OC',
		'KP' : 'AS',
		'KR' : 'AS',
		'KW' : 'AS',
		'KG' : 'AS',
		'LA' : 'AS',
		'LV' : 'EU',
		'LB' : 'AS',
		'LS' : 'AF',
		'LR' : 'AF',
		'LY' : 'AF',
		'LI' : 'EU',
		'LT' : 'EU',
		'LU' : 'EU',
		'MO' : 'AS',
		'MK' : 'EU',
		'MG' : 'AF',
		'MW' : 'AF',
		'MY' : 'AS',
		'MV' : 'AS',
		'ML' : 'AF',
		'MT' : 'EU',
		'MH' : 'OC',
		'MQ' : 'NA',
		'MR' : 'AF',
		'MU' : 'AF',
		'YT' : 'AF',
		'MX' : 'NA',
		'FM' : 'OC',
		'MD' : 'EU',
		'MC' : 'EU',
		'MN' : 'AS',
		'ME' : 'EU',
		'MS' : 'NA',
		'MA' : 'AF',
		'MZ' : 'AF',
		'MM' : 'AS',
		'NA' : 'AF',
		'NR' : 'OC',
		'NP' : 'AS',
		'NL' : 'EU',
		'NC' : 'OC',
		'NZ' : 'OC',
		'NI' : 'NA',
		'NE' : 'AF',
		'NG' : 'AF',
		'NU' : 'OC',
		'NF' : 'OC',
		'MP' : 'OC',
		'NO' : 'EU',
		'OM' : 'AS',
		'PK' : 'AS',
		'PW' : 'OC',
		'PS' : 'AS',
		'PA' : 'NA',
		'PG' : 'OC',
		'PY' : 'SA',
		'PE' : 'SA',
		'PH' : 'AS',
		'PN' : 'OC',
		'PL' : 'EU',
		'PT' : 'EU',
		'PR' : 'NA',
		'QA' : 'AS',
		'RE' : 'AF',
		'RO' : 'EU',
		'RU' : 'EU',
		'RW' : 'AF',
		'BL' : 'NA',
		'SH' : 'AF',
		'KN' : 'NA',
		'LC' : 'NA',
		'MF' : 'NA',
		'PM' : 'NA',
		'VC' : 'NA',
		'WS' : 'OC',
		'SM' : 'EU',
		'ST' : 'AF',
		'SA' : 'AS',
		'SN' : 'AF',
		'RS' : 'EU',
		'SC' : 'AF',
		'SL' : 'AF',
		'SG' : 'AS',
		'SX' : 'NA',
		'SK' : 'EU',
		'SI' : 'EU',
		'SB' : 'OC',
		'SO' : 'AF',
		'ZA' : 'AF',
		'GS' : 'AN',
		'SS' : 'AF',
		'ES' : 'EU',
		'LK' : 'AS',
		'SD' : 'AF',
		'SR' : 'SA',
		'SJ' : 'EU',
		'SZ' : 'AF',
		'SE' : 'EU',
		'CH' : 'EU',
		'SY' : 'AS',
		'TW' : 'AS',
		'TJ' : 'AS',
		'TZ' : 'AF',
		'TH' : 'AS',
		'TL' : 'AS',
		'TG' : 'AF',
		'TK' : 'OC',
		'TO' : 'OC',
		'TT' : 'NA',
		'TN' : 'AF',
		'TR' : 'AS',
		'TM' : 'AS',
		'TC' : 'NA',
		'TV' : 'OC',
		'UG' : 'AF',
		'UA' : 'EU',
		'AE' : 'AS',
		'GB' : 'EU',
		'US' : 'NA',
		'UM' : 'OC',
		'VI' : 'NA',
		'UY' : 'SA',
		'UZ' : 'AS',
		'VU' : 'OC',
		'VE' : 'SA',
		'VN' : 'AS',
		'WF' : 'OC',
		'EH' : 'AF',
		'YE' : 'AS',
		'ZM' : 'AF',
		'ZW' : 'AF'
		}
		return country_to_continent[country]

class BadIDException(Exception):
	def __init__(self, message, error):
		self.message = message
		self.error = error
		#print("%s ID does not exist" % (error))
