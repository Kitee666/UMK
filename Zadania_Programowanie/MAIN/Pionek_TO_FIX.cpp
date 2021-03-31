#include <iostream>
#include <cstdio>
using namespace std;
long long sumax[4], sumay[4];
long long m = 0;

bool comp(int xn, int yn, int jaka)
{
	return ((sumax[jaka] + xn) * (sumax[jaka] + xn) + (sumay[jaka] + yn) * (sumay[jaka] + yn)) >= sumax[jaka] * sumax[jaka] + sumay[jaka] * sumay[jaka];
};

int main()
{
	int n, x, y;
	scanf("%d", &n);

	for (int i = 1; i <= n; i++)
	{
		scanf("%d %d", &x, &y);
		if (y > 0)
		{
			if (comp(x, y, 1))
			{
				sumax[1] += x;
				sumay[1] += y;
			}
		}
		else
		{
			if (comp(x, y, 3))
			{
				sumax[3] += x;
				sumay[3] += y;
			}
		}

		if (x > 0)
		{
			if (comp(x, y, 0))
			{
				sumax[0] += x;
				sumay[0] += y;
			}
		}
		else if (comp(x, y, 2))
		{
			sumax[2] += x;
			sumay[2] += y;
		}
	}

	for (int i = 0; i < 4; i++)
	{

		//	cout << sumax[i]*sumax[i] << " " <<sumay[i] << endl;
		if ((long long)sumax[i] * sumax[i] + sumay[i] * sumay[i] > m)
			m = sumax[i] * sumax[i] + sumay[i] * sumay[i];
	}
	cout << m;
	return 0;
}
