#include <stdio.h>

void increasNum(void)
{
	for(long i = 0; i < 1000000; i++)
		printf("Thread : %d\n", i);
}
