#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
	int i, k, j, n, limit, max, x;
	cin >> x;
	for (k = 0; k < x; k++)
	{
		if (k > 0)
			printf("\n");
		scanf("%i %i", &n, &limit);
		int *waga, *wartosc;
		waga = new int[n];
		wartosc = new int[n];
		for (i = 1; i <= n; i++)
		{
			scanf("%i %i", &waga[i], &wartosc[i]);
			if (waga[i] > limit)
			{
				i--;
				n--;
			}
		}
		int **sumy;
		sumy = new int *[n + 1];
		for (i = 0; i <= n; i++)
		{
			sumy[i] = new int[limit + 1];
			sumy[i][0] = 0;
		}
		for (j = 0; j <= limit; j++)
			sumy[0][j] = 0;
		for (i = 1; i <= n; i++)
			for (j = 0; j <= limit; j++)
				if (waga[i] > j)
				{
					sumy[i][j] = sumy[i - 1][j];
				}
				else
				{
					max = sumy[i - 1][j - waga[i]] + wartosc[i];
					if (max < sumy[i - 1][j])
						sumy[i][j] = sumy[i - 1][j];
					else
						sumy[i][j] = max;
				}
		printf("%i", sumy[n][limit]);
	}
	return 0;
}
