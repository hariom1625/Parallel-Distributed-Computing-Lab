from fetchFromWiki import fetchFromWiki
from fetchFromYahoo import fetchFromYahoo
import time

if __name__ == "__main__":

	
	fetchFromWikiObj = fetchFromWiki()
	fetchFromYahooObj = fetchFromYahoo()

	table = fetchFromWikiObj.getTable()

	# Sequential Execution 
	print("----- Sequential Execution -----")
	startTime = time.time()

	symbols = fetchFromWikiObj.sequential(table)
	fetchFromYahooObj.sequential(symbols)
	print("Sequential Time of Execution: ",time.time()-startTime)

	# Multithreaded Execution
	print("----- Multithreaded Execution -----")
	startTime = time.time()
	symbols = fetchFromWikiObj.multithreaded(table)
	fetchFromYahooObj.multithreaded(symbols)
	print("Multithreaded Time of Execution: ",time.time()-startTime)