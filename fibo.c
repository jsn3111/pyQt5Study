/* 파이썬에서 사용할 C 라이브러리 파일의 소스 코드
   파이썬의 느린 성능을 C code가 커버한다.
*/

#include <stdio.h>
#include <time.h>

int fibo(int n)
{
	if(n==0)
		return 0;
	else if(n==1)
		return 1;
	else
		return fibo(n-1) + fibo(n-2);
}
