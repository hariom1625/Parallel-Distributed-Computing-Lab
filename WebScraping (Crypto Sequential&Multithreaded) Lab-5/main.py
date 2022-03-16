from fetchCoinName import fetchCoinName
from fetchCoinPrice import fetchCoinPrice
import time

if __name__ == "__main__":

	
	fetchCoinName = fetchCoinName()
	fetchCoinPrice = fetchCoinPrice()

	table = fetchCoinName.getTable()

	# Sequential Execution 
	print("----- Sequential Execution -----")
	startTime = time.time()
	coinNames = fetchCoinName.sequential(table)
	fetchCoinPrice.sequential(coinNames)
	sequentialTime = time.time()-startTime

	# Multithreaded Execution
	print("----- Multithreaded Execution -----")
	startTime = time.time()
	coinNames = fetchCoinName.multithreaded(table)
	fetchCoinPrice.multithreaded(coinNames)
	multithreadTime = time.time()-startTime

	print("Sequential Time of Execution: ",sequentialTime)
	print("Multithreaded Time of Execution: ",multithreadTime)