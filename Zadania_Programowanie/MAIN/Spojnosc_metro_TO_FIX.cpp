#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

struct odlegosc
{
	int id, daleko;

	bool operator<(odlegosc drugi) const
	{
		// odwrotnie, bo priority_queue (uzyte dalej) sortuje odwrotnie
		return daleko < drugi.daleko;
	}
};

int tab[1 << 20], tab2[1 << 20], sumy[1 << 20], wypisz[1 << 20][3];
int main()
{
	int sumamin = 1 << 20, w, h = 0;
	int n;
	scanf("%d", &n);
	tab[1] = 0;
	tab2[n] = 0;
	for (int i = 2; i < n; i++)
	{
		scanf("%d", &tab[i]);
	}
	for (int i = 2; i < n; i++)
	{
		scanf("%d", &tab2[i]);
		if (tab2[i] + tab[i] < sumamin)
		{
			sumamin = tab2[i] + tab[i];
			w = 0;
			sumy[0] = i;
		}
		else if (tab2[i] + tab[i] == sumamin)
		{
			w++;
			sumy[w] = i;
		}
	}
	int temp = 0, pom = 0;
	tab[n] = sumamin;
	odlegosc *kregle;
	kregle = new odlegosc[w + 1];
	kregle[w + 1].id = 1;
	kregle[w + 1].daleko = 0;
	kregle[w + 2].daleko = sumamin;
	kregle[w + 2].id = n;
	for (int i = 0; i <= w; i++)
	{
		kregle[i].id = sumy[i];
		kregle[i].daleko = tab[sumy[i]];
	}
	sort(kregle, kregle + w + 2);

	for (int i = 1; i <= w + 2; i++)
	{

		//	printf("%d %d %d\n",kregle[i-1].id,kregle[i].id,kregle[i].daleko-kregle[i-1].daleko);
		wypisz[h][0] = kregle[i - 1].id;
		wypisz[h][1] = kregle[i].id;
		wypisz[h][2] = kregle[i].daleko - kregle[i - 1].daleko;
		h++;
	}

	//	cout <<"############33" << endl;
	int start, end, av;
	for (int i = 2; i < n; i++)
	{
		if (tab[i] + tab2[i] == sumamin)
			continue;
		//	cout <<"ELO" <<endl;
		start = -1;
		end = w + 3;
		temp = tab[i] - ((tab[i] + tab2[i] - sumamin) / 2);
		//cout << start << end << "XXXXX";
		//	cout << temp << "XXX" << endl;
		while (end - start > 1)
		{
			av = (start + end) / 2;
			//	cout << kregle[av].daleko << ";";
			if (temp < kregle[av].daleko)
				end = av;
			else
				start = av;
			if (temp == kregle[av].daleko)
				break;
		}
		//	cout << temp << " " << kregle[av].daleko<< endl;
		if (kregle[av].daleko == temp)
		{
			//	printf("%d %d %d\n",i,kregle[av].id,tab[i]-kregle[av].daleko);
			wypisz[h][0] = kregle[av].id;
			wypisz[h][1] = i;
			wypisz[h][2] = tab[i] - kregle[av].daleko;
			h++;
		}
		else
		{

			printf("NIE");
			return 0;
		}
	}
	printf("TAK\n");
	for (int i = 0; i < h; i++)
	{
		for (int j = 0; j < 3; j++)
		{
			printf("%d ", wypisz[i][j]);
		}
		printf("\n");
	}
}
