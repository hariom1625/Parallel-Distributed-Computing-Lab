import threading
import time

def printSquare(n):

	sum=0;
	for i in range(1,n):
		sum = sum + (i*i)

	print("Sum of Squares of first %d natural numbers is " % n, sum)

def sleepFun():

	time.sleep(1);

if __name__ == "__main__":

	n = input("Enter the value of n:")
	n = int(n)
	startTime = time.time()
	thread1 = threading.Thread(target=printSquare(n))
	thread2 = threading.Thread(target=sleepFun())
	thread1.start()
	thread2.start()

	thread1.join()
	thread2.join()
	print("Multi-thread Time of Execution: %s seconds\n" % (time.time()-startTime))

	startTime = time.time()
	printSquare(n)
	sleepFun()
	print("Sequential Time of Execution: %s seconds" % (time.time()-startTime))
