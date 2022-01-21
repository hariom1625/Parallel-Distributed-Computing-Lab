// Write a C/C++/JAVA program to display the Thread Id of current running thread and total number of threads that are present.

#include <stdio.h>
#include <omp.h>

int main (int argc, char** argv) {

	int intermediateSum = 0, sum = 0, n;

	printf("Total Number of Threads present are: %d\n", omp_get_max_threads());

	#pragma omp parallel private(intermediateSum) shared(sum,n)
	{
		intermediateSum = 0;
		sum = 0;
		n = 10;
		#pragma omp for
		for (int i = 1; i <= n; i++) {
			intermediateSum += i;
		}

		printf("Intermediate Sum = %d ThreadId = %d\n", intermediateSum, omp_get_thread_num());

		#pragma omp critical
		{
			sum += intermediateSum;
		}

	}

	printf("Sum = %d\n", sum );
	return 0;

}
