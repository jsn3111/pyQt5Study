/* ���̽㿡�� ����� C ���̺귯�� ������ �ҽ� �ڵ�
   ���̽��� ���� ������ C code�� Ŀ���Ѵ�.
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
