from bs4 import BeautifulSoup
import requests
import threading
import time

class fetchFromYahoo:

	def getValue(self,symbol):

		url = "https://finance.yahoo.com/quote/" + symbol

		yahooHtmlPage = requests.get(url).text
		soup = BeautifulSoup(yahooHtmlPage,'html.parser')
		div1 = soup.find('div',{'class':'D(ib) Mend(20px)'})
		if(div1!=None):
			currValue = div1.find('fin-streamer',{'class':'Fw(b) Fz(36px) Mb(-4px) D(ib)'})
			print(symbol,currValue.text)

	def sequential(self,symbols):
		
		for symbol in symbols[0:20]:
			self.getValue(symbol)

	
	def multithreaded(self,symbols):

		threadArr = []
		for symbol in symbols[0:20]:
			thread = threading.Thread(target=self.getValue,args=(symbol,))
			threadArr.append(thread)

		for t in threadArr:
			t.start();

		for t in threadArr:
			t.join();




				