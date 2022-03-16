from bs4 import BeautifulSoup
import requests
import threading
import time
from threading import Lock

lockToPrint = Lock()

class fetchCoinPrice:

	def getValue(self,coinName):

		url = "https://crypto.com/price/" + (coinName.replace(" ","-").lower())

		cryptoHtmlPage = requests.get(url).text
		soup = BeautifulSoup(cryptoHtmlPage,'html.parser')
		div1 = soup.find('div',{'class':'css-owerj1'})
		if(div1!=None):
			currValue = div1.find('span',{'class':'chakra-text css-13hqrwd'})
			lockToPrint.acquire()
			print('{:20s} {:20s}'.format(coinName,currValue.text))
			lockToPrint.release()

	def sequential(self,coinNames):

		print("------------------------------------")
		print('{:20s} {:20s}'.format("Crypto Currency","Price"))
		print("------------------------------------")
		for coinName in coinNames[0:50]:
			self.getValue(coinName)

	
	def multithreaded(self,coinNames):

		threadArr = []
		print("------------------------------------")
		print('{:20s} {:20s}'.format("Crypto Currency","Price"))
		print("------------------------------------")
		for coinName in coinNames[0:50]:
			thread = threading.Thread(target=self.getValue,args=(coinName,))
			threadArr.append(thread)

		for t in threadArr:
			t.start();

		for t in threadArr:
			t.join();




				