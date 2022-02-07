# Q. Write separate thread classes that define the functionalities of computing sum of squares and sleep function.
# Import the classes in your main function and then check for execution time taken by both functions.

import threading
import time

def printSquare(n):

	sum=0;
	for i in range(1,n+1):
		sum = sum + (i*i)

	print("Sum of Squares of first %d natural numbers is " % n, sum)

def sleepFun(n):

	time.sleep(n);

def main():

	n = input("Enter the value of n:")
	n = int(n)

	startTime = time.time()
	threadArr1 = []
	for i in range(1,n+1):
		thread1 = threading.Thread(target=printSquare(i))
		thread1.start()
		threadArr1.append(thread1)

	for i in range(len(threadArr1)):
		threadArr1[i].join()

	print("Time of Execution of Sum of squares function is: %s seconds\n" % (time.time()-startTime))

	startTime = time.time()
	threadArr2 = []
	for i in range(1,n+1):
		thread2 = threading.Thread(target=sleepFun(i))
		thread2.start()
		threadArr2.append(thread2)

	for i in range(len(threadArr2)):
		threadArr2[i].join()

	print("Time of Execution of Sleep function is: %s seconds" % (time.time()-startTime))

if __name__ == "__main__":
	main()

