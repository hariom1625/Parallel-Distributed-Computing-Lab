from bs4 import BeautifulSoup
import requests
import threading
import time

symbols = [] 

class fetchFromWiki:

	def getTable(self):
		wikiHtmlPage = requests.get("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies").text
		soup = BeautifulSoup(wikiHtmlPage,'html.parser')
		table = soup.find('table',{'class':'wikitable'})
		symbols = []

		return table

	def getValue(self,row):
		tableData = row.find('td')
		if tableData!=None:
			symbols.append(tableData.find('a').text)

	def sequential(self,table):

		for row in table.findAll('tr'):
			self.getValue(row)

		return symbols


	def multithreaded(self,table):
		threadArr = []

		for row in table.findAll('tr'):
			thread = threading.Thread(target=self.getValue,args=(row,))
			threadArr.append(thread)

		for t in threadArr:
			t.start();

		for t in threadArr:
			t.join();

		return symbols
