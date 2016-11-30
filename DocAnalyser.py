#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Document Analyser
By Nicholas Robinson
"""

from DataTypes import Document as Doc
from DataTypes import User as User
from List import ListContainer as List

from collections import Counter

class DocAnalyser():

	def __init__(self, dl, ul):
		self.dl = dl
		self.ul = ul

	"""
	Task 2a
	"""
	def docCountries(self, docID):
		if self.dl.contains(docID):
			doc = self.dl.get(docID)
			return Counter(doc.getCountries()).most_common()
		else:
			return []

	"""
	Task 2b
	"""
	def docContinents(self, docID):
		if self.dl.contains(docID):
			doc = self.dl.get(docID)
			continentlist = []
			for country in doc.getCountries():
				continentlist.append(self.countryToContinent(country))
			return Counter(continentlist).most_common()
		else:
			return []

	"""
	Task 4
	"""
	def topTenReaders(self):
		topten = []
		for user in self.ul:
			if len(topten) < 10 or user.docTotalTime > topten[0][1]:
				topten.append((user,user.docTotalTime))
			topten.sort(key=lambda tup: tup[1], reverse=True)
		return [user[0] for user in topten]

	"""
	Task 5a
	"""
	def docReaders(self, docID):
		doc = self.dl.get(docID)
		return doc.usersRead

	"""
	Task 5b
	"""
	def readDocs(self, userID):
		user = self.ul.get(userID)
		return user.getDocs()

	"""
	Task 5d & 5e
	Parameters
		docID
		sortingFun
			Input tuple list of (Document, Time)
			Output Document list
		userID

	Output
		List of sorted documents
	"""
	def alsoLiked(self, docID, sortingFun="readerNum", userID=None):
		totalUsers = self.docReaders(docID)

		if not (userID is None):
			if sortingFun == "readerNum":
				doclist = []
				""" Get list of all documents read by similar users """
				for user in totalUsers:
					if user.id == userID: # Remove searching user from temp user list
						continue
					for doc in user.getDocs():
						if doc.id == docID:
							doclist = doclist + user.getDocs()
							break

				""" Sort list into most frequent doc items """
				counterlist =Counter(doclist).most_common(10)
				doclist = []
				""" Edit list of sorted top documents to only save doc """
				for doc in counterlist:
					doclist.append(doc[0])
				return doclist

			if sortingFun == "readerProfile":
				totalDocs = self.readDocs(userID)
				users = []
				docTimeListFull = []
				for user in totalUsers:
					if user.id == userID: # Remove searching user from temp user list
						continue
					for doc in user.getDocs():
						if doc[0].id == docID:
							docTimeListFull += user.getDocTimes()

				docTimeList = []
				for doctime in docTimeListFull:
					"""templist = (x[0] for x in docTimeList)""" #TO DO GENERATOR
					templist = [x[0] for x in docTimeList]
					if not (doctime[0] in templist):
						docTimeList.append(doctime)
					else:
						for item in docTimeList:
							if item[0] == doctime[0]:
								item[1] += doctime[1]
				docTimeList.sort(key=lambda tup: tup[1], reverse=True)
				return docTimeList[:10]


			if sortingFun == "closestReader":
				totalDocs = self.readDocs(userID)
				users = []
				for user in totalUsers:
					if user.id == userID: # Remove searching user from temp user list
						continue
					for doc in user.getDocs():
						if doc.id == docID:
							users.append(user)

				userFitnessList = []
				for user in users:
					sameDocs = 0
					for doc in totalDocs:
						if doc in user.docsRead:
							sameDocs += 1
					userFitnessList.append((user,sameDocs))
				userFitnessList.sort(key=lambda tup: tup[1], reverse=True)

				docslist = []
				index = 0
				while len(docslist) < 10:
					for doc in userFitnessList[index][0].docsRead:
						if not (doc in totalDocs):
							docslist.append(doc)
					index += 1
				return docslist[:10]

		else:
			if sortingFun == "closestReader":
				totalDocs = self.readDocs(userID)
				users = []
				for user in totalUsers:
					for doc in user.getDocs():
						if doc.id == docID:
							users.append(user)

				userFitnessList = []
				for user in users:
					sameDocs = 0
					for doc in totalDocs:
						if doc in user.readDocs:
							sameDocs = sameDocs + 1
					userFitnessList.append((user,sameDocs))
				userFitnessList.sort(key=lambda tup: tup[1], reverse=True)
				doclist = userFitnessList[0][0].docsRead
				doclist.remove(self.dl.get(docID))
				return doclist
			else:
				print("ERROR")
				return []

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
