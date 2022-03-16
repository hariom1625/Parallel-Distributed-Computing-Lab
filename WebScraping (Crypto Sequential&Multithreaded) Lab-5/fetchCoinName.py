from bs4 import BeautifulSoup
import requests
import threading
import time

coinNames = [] 

class fetchCoinName:

	def getTable(self):
		cyrptoHtmlPage = requests.get("https://crypto.com/price").text
		soup = BeautifulSoup(cyrptoHtmlPage,'html.parser')
		table = soup.find('table',{'class':'chakra-table css-1bveei3'})

		return table

	def getValue(self,row):
		tableData = row.find('td',{'class':'css-1sem0fc'})
		if tableData!=None:
			coinName = tableData.find('span',{'class':'chakra-text css-1mrk1dy'}).text
			coinNames.append(coinName)

	def sequential(self,table):

		for row in table.findAll('tr'):
			self.getValue(row)

		return coinNames


	def multithreaded(self,table):
		threadArr = []

		for row in table.findAll('tr'):
			thread = threading.Thread(target=self.getValue,args=(row,))
			threadArr.append(thread)

		for t in threadArr:
			t.start();

		for t in threadArr:
			t.join();

		return coinNames
